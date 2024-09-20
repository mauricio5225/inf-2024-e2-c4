import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def fetch_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

# Ejemplo de uso
if __name__ == "__main__":
    connection = create_connection("localhost", "root", "root", "test")

    # Consulta de ejemplo para crear una tabla
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(100) NOT NULL,
      age INT,
      gender VARCHAR(50),
      nationality VARCHAR(50)
    );
    """
    execute_query(connection, create_table_query)

    # Consulta de ejemplo para insertar datos
    insert_query = """
    INSERT INTO users (name, age, gender, nationality)
    VALUES ('Tomas Burgos', 20, 'Male', 'Argentino');
    """
    execute_query(connection, insert_query)

    # Consulta de ejemplo para obtener datos
    select_query = "SELECT * FROM users;"
    users = fetch_query(connection, select_query)

    for user in users:
        print(user)
