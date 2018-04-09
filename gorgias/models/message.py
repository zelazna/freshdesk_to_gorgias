class Message:
    def __init__(self):
        self.body_html = None
        self.via = "api"
        self.channel = "email"
        self.type = "email"
        self.sent_datetime = None
        self.sender = None
        self.recipient = None
