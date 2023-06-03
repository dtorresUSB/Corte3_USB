from main import get_conn, get_cursor


def init_database():
    conn = get_conn()

    with open('./data/script.sql', 'r') as f:
        script = f.read()

    # Split the script into individual statements
    statements = script.split(';')

    # Remove any empty statements
    statements = [stmt.strip() for stmt in statements if stmt.strip()]

    # Execute each statement
    for stmt in statements:
        cur = get_cursor()
        cur.execute(stmt)
        cur.close()

    conn.commit()
    conn.close()


if __name__ == "__main__":
    warning = input("By executing this script you are going to delete all the data in the DB. Are you sure to continue? y/N: ")

    if warning == "y":
        init_database()

    else:
        print("No executed")
