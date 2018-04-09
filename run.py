from gorgias.api import FreshDeskClient, GorgiasClient
from gorgias.importer import Importer
from gorgias.db.database import Database
import json


def run():
    credentials = json.loads(open('credentials.json').read())
    gorgias_credentials = credentials["gorgias"]
    freshdesk_credentials = credentials["freshdesk"]

    freshdesk_client = FreshDeskClient(
        username=freshdesk_credentials["username"],
        password=freshdesk_credentials["password"],
        base_url="https://poiuytreza.freshdesk.com/api/v2"
    )

    gorgias_client = GorgiasClient(
        username=gorgias_credentials["username"],
        password=gorgias_credentials["password"],
        base_url="https://azertyuiop.gorgias.io/api"
    )

    database = Database("gorgias/db/data.json")
    importer = Importer(
        freshdesk_client=freshdesk_client,
        gorgias_client=gorgias_client,
        database=database
    )

    importer.run()


if __name__ == "__main__":
    run()
