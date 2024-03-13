import sqlite3

def create_activities_table():
    conn = sqlite3.connect("routine.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS activities(id INTEGER NOT NULL PRIMARY KEY, name TEXT NOT NULL, freq TEXT NOT NULL, check BOOLEAN)")
    conn.commit()
    conn.close()

def create_goals_table():
    conn = sqlite3.connect("routine.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS goals (
        id INTEGER PRIMARY KEY,
        name TEXT,
        freq TEXT,
        check BOOLEAN
    )
    """)
    conn.commit()
    conn.close()

def create_rewards_table():
    conn = sqlite3.connect("routine.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS rewards (
        id INTEGER PRIMARY KEY,
        name TEXT,
        freq TEXT,
        check BOOLEAN
    )
    """)
    conn.commit()
    conn.close()


class Connect(object):
    def __init__(self, db_name):
        try:
            # connect
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            print("Banco:", db_name)
            # Read SQLite version
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            print("SQLite version: %s" % self.data)
        except sqlite3.Error:
            print("Error to open database.")
            return False

    def close_db(self):
        if self.conn:
            self.conn.close()
            print("Close connection.")


class RoutineDb(object):
    def __init__(self):
        self.db = Connect('routine.db')

    def close_connection(self):
        self.db.close_db()

if __name__ == '__main__':
    routine = RoutineDb()
    #create_activities_table()
    routine.close_connection()


