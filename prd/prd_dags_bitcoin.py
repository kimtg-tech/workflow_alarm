from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
# common.slack_notification에서 send_slack_message 함수 가져오기
from slack_notification import slackAlert
import requests

def fetch_bitcoin_price_and_notify(webhook_url):
    
    """
    Fetch the current Bitcoin price and send a notification to Slack.
    """
    try:
        # Fetch Bitcoin price
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json")
        response.raise_for_status()
        price = response.json()["bpi"]["USD"]["rate"]

        # Send Slack notification
        message = f"The current Bitcoin price is ${price}."
        send_slack_message(message)

    except Exception as e:
        print(f"Error fetching Bitcoin price: {e}")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 12, 16),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id='prd_dags_bitcoin_price',  # Update to stg/prd for respective environments
    default_args=default_args,
    description='Fetch Bitcoin price and send Slack notifications',    
    schedule_interval="0 * * * *",  # 1시간마다 실행
    is_paused_upon_creation=False,   # DAG 활성화 상태로 생성
)



fetch_price_task = PythonOperator(
    task_id='fetch_bitcoin_price',
    python_callable=fetch_bitcoin_price_and_notify,
    dag=dag,
)
