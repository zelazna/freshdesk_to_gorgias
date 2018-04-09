class MessageSerializer:
    """Transform a message object into json message data"""

    def dump(self, message):
        return {
            "body_html": message.body_html,
            "via": "api",
            "channel": "email",
            "sent_datetime": message.sent_datetime,
            "source": {
                "to": [
                    {
                        "name": message.sender,
                        "address": message.sender
                    }
                ],
                "from": {
                    "name": message.recipient,
                    "address": message.recipient,
                    "type": "email"
                },
                "type": "email"
            }
        }
