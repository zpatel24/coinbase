import sqlite3
from datetime import datetime

# Set up the SQLite database
def setup_database():
    conn = sqlite3.connect('eth_balances.db')
    cursor = conn.cursor()

    # Create a table for balances if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS balances (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            balance REAL,
            timestamp TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Store balance in the database
def store_balance_in_db(balance):
    conn = sqlite3.connect('eth_balances.db')
    cursor = conn.cursor()

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO balances (balance, timestamp) VALUES (?, ?)', (balance, timestamp))

    conn.commit()
    conn.close()

# Query balances from the database
def query_balances():
    conn = sqlite3.connect('eth_balances.db')
    cursor = conn.cursor()

    # Fetch all balances and timestamps
    cursor.execute('SELECT balance, timestamp FROM balances ORDER BY timestamp')
    data = cursor.fetchall()

    conn.close()
    return data
