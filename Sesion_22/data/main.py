import psycopg2


DB_HOST = "" # URL, like: project.test.us-east-1.rds.amazonaws.com
DB_NAME = "" # master_db_name
DB_USER = "" # master_username
DB_PASSWORD = "" # master_password

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)


def get_conn():
    return conn


def get_cursor():
    return conn.cursor()


def commit_db():
    return conn.commit()


def get_all_users():
    cursor = get_cursor()
    cursor.execute("SELECT * FROM users")

    col_names = [desc[0] for desc in cursor.description]
    users = []

    for row in cursor.fetchall():
        result_dict = {}
        for i in range(len(row)):
            result_dict[col_names[i]] = row[i]
        users.append(result_dict)

    cursor.close()

    print(users)


if __name__ == "__main__":
    get_all_users()
