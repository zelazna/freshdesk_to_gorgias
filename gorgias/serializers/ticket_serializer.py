from .message_serializer import MessageSerializer


class TicketSerializer:
    """Transform a ticket object into json ticket data"""

    def __init__(self):
        self._messages_serializer = MessageSerializer()

    def dump(self, ticket):
        return {
            "channel": "api",
            "via": "api",
            "messages": [self._messages_serializer.dump(message) for message in ticket.messages],
            "receiver": {
                "name": ticket.receiver.name,
                "firstname": ticket.receiver.firstname,
                "email": ticket.receiver.email,
                "lastname": ticket.receiver.lastname
            },
            "sender": {
                "name": ticket.sender.name,
                "firstname": ticket.sender.firstname,
                "email": ticket.sender.email,
                "lastname": ticket.sender.lastname
            },
            "requester": {
                "name": ticket.requester.name,
                "firstname": ticket.requester.firstname,
                "email": ticket.requester.email,
                "lastname": ticket.requester.lastname,
                "channels": [
                    {
                        "type": "email",
                        "address": ticket.requester.email
                    }
                ]
            }
        }
