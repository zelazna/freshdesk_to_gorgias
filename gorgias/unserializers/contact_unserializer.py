from gorgias.models import User


class ContactUnserializer:
    """Handle the json parsing of the contact"""

    def load(self, json_data):
        user = User()
        user.remote_id = json_data.get("id")
        user.active = json_data["active"]
        if len(json_data["name"].split()) > 1:
            user.firstname, user.lastname = json_data["name"].split()
        else:
            user.firstname = json_data["name"]
        user.email = json_data["email"]
        user.language = json_data["language"]
        return user
