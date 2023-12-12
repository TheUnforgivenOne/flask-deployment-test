import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)


@app.route('/')
def sample_route():
  return '<h1>Hello world!</h1>'


if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    app.run(debug=True, host='0.0.0.0', port=port)
