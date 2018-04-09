class User:
    """The User model"""

    def __init__(self):
        self.remote_id = None
        self.active = None
        self.email = None
        self.firstname = None
        self.lastname = None
        self.language = None
        self.timezone = None
        self.channels = []

    @property
    def name(self):
        return f"{self.firstname} {self.lastname}"
