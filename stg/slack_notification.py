# shared/slack_notification.py
import requests
import json


def send_slack_message(webhook_url, message):
    """
    Send a message to Slack using a webhook URL.

    :param webhook_url: Slack Incoming Webhook URL
    :param message: Message content to send
    """
    try:
        headers = {'Content-Type': 'application/json'}
        payload = {'text': message}
        response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending message to Slack: {e}")
