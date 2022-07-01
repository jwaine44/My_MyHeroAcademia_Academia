from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import database


class Hero:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.real_name = data['real_name']
        self.rank = data['rank']
        self.quirk = data['quirk']
        self.quirk_description = data['quirk_description']
        self.description = data['description']
        self.birthday = data['birthday']
        self.age = data['age']
        self.height = data['height']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def display_hero(cls, data):
        query = "SELECT * FROM heroes LEFT JOIN students ON heroes.id = students.hero_id WHERE heroes.name = %(name)s;"
        single_result = connectToMySQL(database).query_db(query, data)[0]
        hero = cls(single_result)
        hero.mentee_name = single_result["students.name"]

        return hero

    @classmethod
    def get_all_heroes(cls):
        query = 'SELECT * FROM heroes;'
        results = connectToMySQL(database).query_db(query)

        list_heroes = []

        if len(results) > 0:
            for hero in results:
                list_heroes.append(cls(hero))
        return list_heroes