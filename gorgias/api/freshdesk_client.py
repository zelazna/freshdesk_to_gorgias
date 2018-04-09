from gorgias.unserializers import (ContactUnserializer,
                                   ConversationUnserializer,
                                   TicketUnserializer)

from . import HTTPClient


class FreshDeskClient(HTTPClient):
    """FreshDesk Client to get tickets and contacts"""

    def __init__(self, **kwargs):
        self._contact_unserializer = ContactUnserializer()
        self._ticket_unserializer = TicketUnserializer()
        self._conversations_unserializer = ConversationUnserializer()
        super(FreshDeskClient, self).__init__(**kwargs)

    def get_tickets(self):
        result = self.get("/tickets")
        return [self._handle_tickets(ticket) for ticket in result]

    def get_contacts(self):
        result = self.get("/contacts")
        return [self._contact_unserializer.load(contact) for contact in result]

    def get_contact(self, user_id):
        result = self.get(f"/contacts/{user_id}")
        return self._contact_unserializer.load(result)

    def get_agent(self, user_id):
        result = self.get(f"/agents/{user_id}")
        return self._contact_unserializer.load(result["contact"])

    def get_conversations(self, ticket_id):
        result = self.get(f"/tickets/{ticket_id}/conversations")
        return [self._conversations_unserializer.load(conv) for conv in result]

    def _handle_tickets(self, ticket_data):
        sender = self.get_contact(ticket_data["requester_id"])
        if ticket_data["responder_id"]:
            receiver = self.get_agent(ticket_data["responder_id"])
        else:
            receiver = sender
        return self._ticket_unserializer.load(
            json_data=ticket_data,
            sender=sender,
            receiver=receiver,
            messages=self.get_conversations(ticket_data["id"])
        )
