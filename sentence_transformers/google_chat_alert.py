from json import dumps
from httplib2 import Http


class GoogleChatAlert():
    def __init__(self, url):
        self.url = url

    def send_alert(self, message):
        """
        send alert to gchat space
        """
        bot_message = {
            'text': message
            }
        message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
        http_obj = Http()
        response = http_obj.request(
            uri=self.url,
            method='POST',
            headers=message_headers,
            body=dumps(bot_message),
        )
        return response[0].get('status')
