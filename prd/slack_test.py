import json 
import sys 
import requests 





# Fetch Bitcoin price
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json")
response.raise_for_status()
price = response.json()["bpi"]["USD"]["rate"]

# Send Slack notification
message = f"The current Bitcoin price is ${price}."

print(message)


url = "https://hooks.slack.com/services/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"

title = ("New Incoming Message :zap:")
#message = ("안녕하세요!")


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

print("끝났을까여?")
print(response.status_code)
print("전송 되었나요?")

#if response.status_code != 200:
#   raise Exception(response.status_code, response.text)