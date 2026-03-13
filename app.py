import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, app
from config import Config
from extensions import db
from werkzeug.middleware.proxy_fix import ProxyFix
from utils.language import translate

os.environ["LOKY_MAX_CPU_COUNT"] = "4"
def create_app():
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

    database_url = os.getenv("DATABASE_URL")

    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)

    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # Needs a secret key for session management
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "fallback_secret_key")

    db.init_app(app)
    
    from routes.auth_routes import auth_bp, init_oauth
    from routes.recommendation_routes import recommendation_bp
    
    init_oauth(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(recommendation_bp)

    # Disable automatic seed_all since we are running it manually
    with app.app_context():
        try:
            from models import CPU, GPU, RAM, SSD, Motherboard, PSU, Laptop
            db.create_all()
        except Exception as e:
            print("Database INIT skipped:", e)
            
    # Make the 't' function available to all Jinja templates for translation
    @app.context_processor
    def inject_translator():
        return dict(t=translate)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
