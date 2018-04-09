from gorgias.serializers import UserSerializer, TicketSerializer

from . import HTTPClient


class GorgiasClient(HTTPClient):
    def __init__(self, **kwargs):
        self._user_serializer = UserSerializer()
        self._ticket_serializer = TicketSerializer()
        super(GorgiasClient, self).__init__(**kwargs)

    def create_user(self, user):
        data = self._user_serializer.dump(user)
        return self.post("/users", data)

    def create_ticket(self, ticket):
        data = self._ticket_serializer.dump(ticket)
        return self.post("/tickets", data)

    def get_user_by(self, param, param_value):
        result = self.get(f"/?{param}={param_value}")
        if not result.data:
            return False
        else:
            return result.data[0]
