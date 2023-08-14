from pprint import pprint

from flask_app.models.ninja import Ninja
from flask_app.config.mysqlconnection import connect_to_mysql

DATABASE = "dojos_and_ninjas_schema"


class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.ninjas = []

    # Create
    @classmethod
    def create(cls, form_data):
        """Create an dojo in the dojos table."""

        query = """
        INSERT INTO dojos (name)
        VALUES (%(name)s);
        """

        dojo_id = connect_to_mysql(DATABASE).query_db(query, form_data)
        return dojo_id

    # Read All
    @classmethod
    def get_all(cls):
        """Retrieve all dojos in the dojos table."""

        query = "SELECT * FROM dojos;"

        results = connect_to_mysql(DATABASE).query_db(query)
        pprint(results)

        dojos = []

        for dictionary in results:
            dojos.append(Dojo(dictionary))

        return dojos

    # Read One
    @classmethod
    def get_one(cls, dojo_id):
        """Retrieve one dojo from the dojos table."""

        query = """
        SELECT * FROM dojos
        JOIN ninjas ON dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(dojo_id)s;
        """

        data = {"dojo_id": dojo_id}

        results = connect_to_mysql(DATABASE).query_db(query, data)
        dojo = Dojo(results[0])

        for result in results:
            ninja = Ninja.get_one(result["ninjas.id"])
            dojo.ninjas.append(ninja)

        return dojo
