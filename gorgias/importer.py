class Importer:
    """The main application class handle the persistence"""

    def __init__(self, gorgias_client, freshdesk_client, database):
        self._gorgias_client = gorgias_client
        self._freshdesk_client = freshdesk_client
        self._database = database

    def run(self):
        self._import_contacts()
        self._import_tickets()

    def _import_contacts(self):
        contacts = self._freshdesk_client.get_contacts()
        for contact in contacts:
            if not self._database.find("contact", contact.remote_id):
                self._gorgias_client.create_user(contact)
                self._database.save("contact", contact.remote_id)
        print('users successfully imported')

    def _import_tickets(self):
        tickets = self._freshdesk_client.get_tickets()
        for ticket in tickets:
            if not self._database.find("ticket", ticket.id):
                self._gorgias_client.create_ticket(ticket)
                self._database.save("ticket", ticket.id)
        print('tickets successfully imported')
