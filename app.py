from flask import Flask, jsonify, render_template, make_response
import database
from apscheduler.schedulers.background import BackgroundScheduler
from get_balance import get_eth_balance
import time

app = Flask(__name__)

# Flask route to render the graph page
@app.route('/')
def index():
    return render_template('index.html')

# API route to fetch balance data
@app.route('/api/balances')
def balances():
    data = database.query_balances()
    response = make_response(jsonify(data))
    response.headers['Cache-Control'] = 'no-store'  # This disables caching of the response
    return response

# Function to fetch and store ETH balance
def fetch_and_store_balance():
    try:
        balance = get_eth_balance()  # Fetch balance using the function in get_balance.py
        database.store_balance_in_db(balance)  
        print(f"Stored balance: {balance} ETH")
    except Exception as e:
        print(f"Error: {e}")

# Schedule the balance fetching
def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_and_store_balance, 'interval', minutes=30)  # Run every 30 minutes
    scheduler.start()
    print("Scheduler started to get balance every 30 minutes")

if __name__ == '__main__':
    # Ensure the database is initialized and the table exists
    print("Setting up the database...")
    database.setup_database() 
    print("Database setup complete.")
    
    # Start the scheduler
    start_scheduler()

    # Run the Flask app
    app.run(debug=True)
