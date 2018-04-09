from gorgias.models import Message


class ConversationUnserializer:
    """Handle the json parsing of the contact"""

    def load(self, json_data):
        message = Message()
        message.body_html = json_data["body"]
        message.sent_datetime = json_data["created_at"]
        message.sender = json_data["support_email"]
        message.recipient = json_data["to_emails"][0]
        return message
