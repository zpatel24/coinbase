Overview
This is a Flask-based web appl that obtains the eth balance of a specified wallet address. The app periodically queries the Coinbase Developer API for the wallet’s ETH balance and stores the results in a sqllite database. The current schhedule to query the data is every 30 minutes. The balances are displayed in a graph using Plotly, allowing the user to view the balance over time. You can run the app locally and view the graph on your browser.

Project Structure
```plaintext
coinbase-project/
│
├── app.py                # Main Flask app
├── get_balance.py        # Function to fetch balance from api
├── database.py           # Handles database setup
├── requirements.txt      # List of Python dependencies
├── .gitignore            # Git ignore file
├── README.md             # Project documentation
│
├── templates/            # HTML templates
│   └── index.html        # Page to render graph
│
└── static/               # (CSS, JS, etc.)
    └── css/
        └── styles.css    # CSS for the web app
```


Prerequisites
- Python 3.x: Make sure you have Python installed. You can download it here.
- Coinbase Developer Account: You'll need to create an account at Coinbase Developer Platform to get the wallet balance. Sign up at Coinbase Developer.   
   https://portal.cdp.coinbase.com/products/onchain-data
- pyenv (optional): Help manage Python versions and create virtual environments.

Steps to run Project

1) Clone this repo locally
2) Head to this project directory and create a virtual env by running the following commands
```plaintext
python3 -m venv venv
source venv/bin/activate  # On Linux
```
3) Download dependencies from requirements.txt (pip install -r requirements.txt)
4) Run the application by running (python app.py)
5) Open a browser and go to http://127.0.0.1:5000/ to view the eth balance graph locally

