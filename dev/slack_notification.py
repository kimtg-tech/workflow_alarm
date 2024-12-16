import requests
import sys 
import json

def send_slack_message(webhook_url, message):
    title = ("New Incoming Message :zap:")
    slack_data = {
        "username" : "notice_boot",    
        "attachments" : [
                {
                    "color" : "#9733EE",
                    "fields" : [
                        {
                        "title" : title, 
                        "value" : message, 
                        "short" : "false",
                    }
                ]
            }        
        ]
    }

    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "appication.json", 'Content-Length' : byte_length}
    response = requests.post(webhook_url, data = json.dumps(slack_data), headers = headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
