from datetime import datetime


from data.main import get_cursor, commit_db


class User():
    def __init__(self, name, email, password) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.last_login = datetime.isoformat( datetime.now() )
        self.created_at = datetime.isoformat( datetime.now() )
        self.updated_at = datetime.isoformat( datetime.now() )

        cursor = get_cursor()

        statement = f"INSERT INTO users (name, email, password, last_login, created_at, updated_at) VALUES ('{ self.name }', '{ self.email }', '{ self.password }', '{ self.last_login }', '{ self.created_at }', '{ self.updated_at }')"

        cursor.execute(statement)
        cursor.close()

        commit_db()


    @staticmethod
    def login(email, password):
        cursor = get_cursor()
        cursor.execute(f"SELECT * FROM users WHERE email = '{ email }' AND password = '{ password }'")
        result = cursor.fetchone()

        if not result: return None

        col_names = [desc[0] for desc in cursor.description]

        cursor.close()

        result_dict = {}

        for i in range(len(result)):
            result_dict[col_names[i]] = result[i]

        return result_dict
