# pip install psycopg2-binary
# pip install pandas

import psycopg2
import pandas as pd

class PostgreSQLConnection:
    def __init__(self, dbname, user, password, host="localhost", port=5432):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Connected to the PostgreSQL database!")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL:", error)

    def disconnect(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("Disconnected from the PostgreSQL database.")

    def execute_extract_query(self, query):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except (Exception, psycopg2.Error) as error:
            print("Error executing query:", error)

    def execute_load_query(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully.")
        except (Exception, psycopg2.Error) as error:
            self.connection.rollback()
            print("Error executing write query:", error)
            
if __name__ == "__main__":
    # replace the following values with your local database credentials
    dbname = "your_database_name"
    user = "your_username"
    password = "your_password"

    db_connection = PostgreSQLConnection(dbname, user, password)

    # connect to the database
    db_connection.connect()

    # example read query 
    READ_QUERY = "SELECT * FROM your_table_name LIMIT 10"   # change the name of the table
    result = db_connection.execute_extract_query(READ_QUERY)
    
    # print the read query results
    if result:
        for row in result:
            print(row)

    # convert the query result to a DataFrame
        if result:
            df = pd.DataFrame(result, columns=[desc[0] for desc in db_connection.cursor.description])
            print(df)
            
    
    # example write query (INSERT)
    insert_query = "INSERT INTO your_table_name (column1, column2) VALUES ('value1', 'value2')" # change the columns here also
    db_connection.execute_load_query(insert_query)

    
    # disconnect from the database after finish the work
    db_connection.disconnect()
