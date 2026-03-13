from flask import Blueprint, redirect, url_for, session
from authlib.integrations.flask_client import OAuth
import os

auth_bp = Blueprint("auth", __name__)

oauth = OAuth()

def init_oauth(app):
    oauth.init_app(app)

    oauth.register(
        name='google',
        client_id=os.getenv("GOOGLE_CLIENT_ID"),
        client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
        server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

@auth_bp.route("/login")
def login():
    redirect_uri = url_for("auth.callback", _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

from flask import session, redirect, current_app
from authlib.integrations.flask_client import OAuth


@auth_bp.route("/auth/callback")
def callback():
    token = oauth.google.authorize_access_token()

    # Safely fetch user info
    user_info = token.get("userinfo")

    if not user_info:
        user_info = oauth.google.parse_id_token(token)

    session["user"] = {
        "name": user_info.get("name", "User"),
        "email": user_info.get("email"),
        "picture": user_info.get("picture", "https://via.placeholder.com/32")
    }

    return redirect("/category")



@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")
