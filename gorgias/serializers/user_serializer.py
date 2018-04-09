class UserSerializer:
    """Transform a contact object into json user data"""

    def dump(self, contact):
        return {
            "active": contact.active,
            "lastname": contact.lastname,
            "name": contact.name,
            "roles": [{
                "name": "user"
            }],
            "external_id": str(contact.remote_id),
            "language": contact.language,
            "email": contact.email
        }
