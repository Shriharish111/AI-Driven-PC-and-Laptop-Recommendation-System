from flask import Flask, app
from config import Config
from extensions import db
import os
from utils.language import translate

os.environ["LOKY_MAX_CPU_COUNT"] = "4"

import os
from flask import Flask
from extensions import db

def create_app():
    app = Flask(__name__)

    database_url = os.getenv("DATABASE_URL")

    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)

    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # run seed_all automatically
    with app.app_context():
        try:
            db.create_all()
            import seed_all
        except Exception as e:
            print("Seed skipped:", e)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)