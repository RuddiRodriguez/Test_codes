# a class using singleton to connect to a sql server database and query it.

import mysql.connector
from mysql.connector import errorcode

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

class Database(Singleton):

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cnx = None
        self.cursor = None

    def connect(self):
        try:
            self.cnx = mysql.connector.connect(user=self.user, password=self.password,
                                               host=self.host,
                                               database=self.database)
            self.cursor = self.cnx.cursor()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            print("Connected to database")

    def query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.cnx.close()

if __name__ == "__main__":
    db = Database
    db.connect()
    print(db.query("SELECT * FROM table"))
    db.close()

    


