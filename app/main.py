from dotenv import load_dotenv
load_dotenv(verbose=True)
from app.flask_app.flask_app import run_flask_app

if __name__ == '__main__':
    run_flask_app()