from flask import Flask, app
from config import Config
from extensions import db
import os
from utils.language import translate

os.environ["LOKY_MAX_CPU_COUNT"] = "4"




def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    
    from routes.auth_routes import auth_bp, init_oauth
    init_oauth(app)
    app.register_blueprint(auth_bp)
    app.jinja_env.globals.update(t=translate)

    with app.app_context():
        import models   # just import module (no *)
        db.create_all()

        from routes.recommendation_routes import recommendation_bp
        app.register_blueprint(recommendation_bp)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
