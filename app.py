import os
from flask import Flask
from extensions import db

os.environ["LOKY_MAX_CPU_COUNT"] = "4"


def create_app():
    app = Flask(__name__)

    database_url = os.getenv("DATABASE_URL")

    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)

    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

        # Run seed script
        try:
            import seed_all
        except Exception as e:
            print("Seed skipped:", e)

    # register routes
    from routes.main_routes import main_bp
    from routes.auth_routes import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)