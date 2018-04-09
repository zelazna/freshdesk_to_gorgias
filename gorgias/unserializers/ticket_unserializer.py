from gorgias.models import Ticket


class TicketUnserializer:
    def load(self, json_data, sender, receiver, messages):
        ticket = Ticket()
        ticket.id = json_data["id"]
        ticket.receiver = receiver
        ticket.sender = sender
        ticket.requester = sender
        ticket.messages = messages
        return ticket
