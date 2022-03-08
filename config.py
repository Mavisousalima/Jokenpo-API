from flask import Flask
from views.player_view import player_page
from views.action_view import action_page
from views.game_view import game_page


def create_app():

    app = Flask(__name__)

    app.register_blueprint(player_page)
    app.register_blueprint(action_page)
    app.register_blueprint(game_page)

    return app