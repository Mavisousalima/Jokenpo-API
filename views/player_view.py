import json
from flask import request, jsonify, Blueprint


player_page = Blueprint('player_page', __name__)

class PlayerView():
    """
    A class that represent the players
    ...
    Methods
    -------
    create_player
        Create a player and save in players.json
    get_all_players
        List all the players in players.json
    get_player
        Return a specific player from players.json
    delete_player
        Delete a specific player from players.json
    """

    @player_page.route('/api/players', methods=['POST'])
    def create_player():
        """
        Create a new player

        If the players.json file don't exist, create the file

        Raises
        ------
        400
            If json is empty
            If the name is not passed
            If creating a player with a already used name

        """
        data = request.json
        if not data:
            return jsonify({'message': 'data can not be empty.'}), 400

        try:
            player_name = data['name']
            if not player_name:
                return jsonify({f'message': 'can not create player with a empty name.'}), 400
        except:
            return jsonify({f'message': 'can not create player with the key.'}), 400

        players = []
        try:
            with open('files/players.json', 'r') as json_file:
                players = json.load(json_file)
        except FileNotFoundError:
            with open('files/players.json', 'w') as json_file:
                json.dump([], json_file, indent=2)

        for player in players:
            if player['name'].lower() == data['name'].lower():
                return jsonify({'message': 'there is already a player with this name.'}), 400

        with open('files/players.json', 'w') as json_file:
            players.append(data)
            json.dump(players, json_file, indent=2)
        

        return jsonify({'Player': data}), 201

    @player_page.route('/api/players', methods=['GET'])
    def get_all_players():
        """
        List all the players in players.json

        If the players file don't exist, create a empty players.json file
        """
        try:
            with open('files/players.json', 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            with open('files/players.json', 'w') as json_file:
                json.dump([], json_file, indent=2)
                return jsonify({'Players': []}), 200

        return jsonify({'Players': data}), 200

    @player_page.route('/api/players/<string:name>', methods=['GET'])
    def get_player(name):
        """
        Return a specific player

        Parameters
        ----------
        name : str

        Raises
        ------
        404
            If the player don't exist
        """
        try:
            with open('files/players.json', 'r') as json_file:
                players = json.load(json_file)
        except FileNotFoundError:
            return jsonify({'message': 'there is no player with this name.'}), 404

        for player in players:
            if player['name'].lower() == name.lower():
                return jsonify({'Player': player}), 200

        return jsonify({'message': 'there is no player with this name.'}), 404

    @player_page.route('/api/players/<string:name>', methods=['DELETE'])
    def delete_player(name):
        """
        Delete a specific player

        Parameters
        ----------
        name : str

        Raises
        ------
        400
            If players.json file don't exist
        404
            If the player don't exist
        """
        try:
            with open('files/players.json', 'r') as json_file:
                players = json.load(json_file)
        except FileNotFoundError:
            return jsonify({'message': 'there is no player with this name.'}), 400

        for player in players:
            if player['name'].lower() == name.lower():
                with open('files/players.json', 'w') as json_file:
                    players.remove(player)
                    json.dump(players, json_file, indent=2)

                with open('files/actions.json', 'r') as json_file:
                    actions = json.load(json_file)
                for action in actions:
                    if action['name'].lower() == name.lower():
                        with open('files/actions.json', 'w') as json_file:
                            actions.remove(action)
                            json.dump(actions, json_file, indent=2)
                
                return '', 204
        return jsonify({'message': 'there is no player with this name.'}), 404