from slackclient import SlackClient
import os

slack_client = SlackClient(os.environ['SLACK_TOKEN'])

# ERRORメッセージ専用フォーマット
error_message_format = """
*[ERROR]: Failed update weather!*
```
params:
id = {}, api_result = {}
```
"""

def send_error_message(text):
    slack_client.api_call(
            "chat.postMessage",
            channel="#test",
            icon_emoji=":rage:",
            username="lambda_bot",
            text=text
    )
