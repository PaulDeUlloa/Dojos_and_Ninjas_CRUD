from pprint import pprint
from flask_app.config.mysqlconnection import connect_to_mysql

DATABASE = "dojos_and_ninjas_schema"


class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.dojo_id = data["dojo_id"]
        self.dojo = None

    # Create
    @classmethod
    def create(cls, form_data):
        """Create an ninja in the ninjas table."""

        query = """
        INSERT INTO ninjas (first_name, last_name, age, dojo_id )
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s );
        """

        ninja_id = connect_to_mysql(DATABASE).query_db(query, form_data)
        return ninja_id

    # Read All
    @classmethod
    def get_all(cls):
        """Retrieve all ninjas in the ninjas table."""

        query = "SELECT * FROM ninjas;"

        results = connect_to_mysql(DATABASE).query_db(query)
        pprint(results)

        ninjas = []

        for dictionary in results:
            ninjas.append(Ninja(dictionary))

        return ninjas

    # Read One
    @classmethod
    def get_one(cls, ninja_id):
        """Retrieve one ninja from the ninjas table."""

        query = """
        SELECT * FROM ninjas
        WHERE id= %(ninja_id)s;
        """

        data = {"ninja_id": ninja_id}

        results = connect_to_mysql(DATABASE).query_db(query, data)

        ninja = Ninja(results[0])
        # dojo = Dojo.get_one(results[0]["dojo_id"])
        # ninja.dojo = dojo

        return ninja
