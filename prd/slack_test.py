import json 
import sys 
import requests 



url = "https://hooks.slack.com/services/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"

title = ("New Incoming Message :zap:")
message = ("안녕하세요!")


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
response = requests.post(url, data = json.dumps(slack_data), headers = headers)
if response.status_code != 200:
    raise Exception(response.status_code, response.text)