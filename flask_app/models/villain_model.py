from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import database


class Villain:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.real_name = data['real_name']
        self.quirk = data['quirk']
        self.quirk_description = data['quirk_description']
        self.description = data['description']
        self.birthday = data['birthday']
        self.age = data['age']
        self.height = data['height']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_one_villain(cls, data):
        query = "SELECT * FROM villains WHERE name = %(name)s;"
        single_result = connectToMySQL(database).query_db(query, data)

        if len(single_result) > 0:
            return cls(single_result[0])
        else:
            return None

    @classmethod
    def get_all_villains(cls):
        query = 'SELECT * FROM villains;'
        results = connectToMySQL(database).query_db(query)

        list_villains = []

        if len(results) > 0:
            for villain in results:
                list_villains.append(cls(villain))
        return list_villains