import requests
import sys 
import json

class slackAlert:
    def __init__(self, channel):
        self.channel = channel
        
    def send_slack_message(self, context):
        title = ("New Incoming Message :zap:")
        url = "https://hooks.slack.com/services/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"
        message = str(context)
        
        headers = {'Content-Type': "appication.json"}
        data = { "username": "notice_bot", "text": message}
        response = request.post(url, json=data, headers=headers)

        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
    
    