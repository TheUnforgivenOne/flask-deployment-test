import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)


@app.route('/')
def sample_route():
  env_value = os.environ.get('ENV_KEY')
  return f'<h1>Hello world! {env_value}</h1>'


if __name__ == "__main__":
    app.run(debug=True)
