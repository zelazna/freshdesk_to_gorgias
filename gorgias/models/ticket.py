class Ticket:
    def __init__(self):
        self.channel = "api"
        self.via = "api"
        self.status = "closed"
        self.messages = None
        self.receiver = None
        self.sender = None
        self.requester = None
