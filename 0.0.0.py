import sqlite3

def connect_db(db_name="vocabulary.db"):
    return sqlite3.connect(db_name)

def create_table(conn):
    with conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS vocabulary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            tag TEXT NOT NULL
        );
        """)

def insert_word(conn, word, tag):
    with conn:
        conn.execute("INSERT INTO vocabulary (word, tag) VALUES (?, ?)", (word, tag))

def fetch_words(conn):
    with conn:
        return conn.execute("SELECT * FROM vocabulary").fetchall()

# Example usage
conn = connect_db()
create_table(conn)
insert_word(conn, 'hello', 'greeting')
words = fetch_words(conn)
print(words)
