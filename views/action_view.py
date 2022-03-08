import json
from flask import Blueprint, jsonify, request


action_page = Blueprint('action_page', __name__)

class ActionView():
    """
    A class that represent the actions
    ...
    Methods
    -------
    create_action
        Create a action and save in actions.json
    get_all_actions
        List all the actions in actions.json
    get_action
        Return a specific action from actions.json
    delete_action
        Delete a specific action from actions.json
    """

    @action_page.route('/api/actions', methods=['POST'])
    def create_action():
        """
        Create a new action

        Raises
        ------
        400
            If Json is empty
            If you pass the wrong key name
            When creating action for a player that already has a action
            When creating action for a nonexistent player
        """
        data = request.json

        if not data:
            return jsonify({'message': 'data can not be empty.'}), 400

        verify_name_key = ''
        try:
            verify_name_key = data['name']
        except:
            return jsonify({'message': f'wrong key name: {verify_name_key}'}), 400

        actions = []
        try:
            with open('files/actions.json', 'r') as json_file:
                actions = json.load(json_file)
        except FileNotFoundError:
            with open('files/actions.json', 'w') as json_file:
                json.dump([], json_file, indent=2)

        for action in actions:
            if action['name'] == data['name']:
                return jsonify({'message': 'this player already has a action.'}), 400

        try:
            with open('files/players.json', 'r') as json_file:
                players = json.load(json_file)
        except FileNotFoundError:
            return jsonify({'message': 'there is no players registered.'}), 400
        
        players = [player['name'] for player in players]
        if data['name'] not in players:
            return jsonify({'message': 'there is no player with this name.'}), 400

        with open('files/actions.json', 'w') as json_file:
            actions.append(data)
            json.dump(actions, json_file, indent=2)

        return jsonify({'Action': data}), 201
    
    @action_page.route('/api/actions', methods=['GET'])
    def get_all_actions():
        """
        List all actions

        If the actions file don't exist, create a empty action.json file
        """
        try:
            with open('files/actions.json', 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            with open('files/actions.json', 'w') as json_file:
                json.dump([], json_file, indent=2)
                return jsonify({'Actions': []}), 200

        return jsonify({'Actions': data}), 200

    @action_page.route('/api/actions/<string:player_name>', methods=['GET'])
    def get_action(player_name):
        """
        Return a specific action

        If the actions file don't exist, create the file and return a empty list

        Parameters
        ----------
        player_name : str

        """
        try:
            with open('files/actions.json', 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            with open('files/actions.json', 'w') as json_file:
                json.dump([], json_file, indent=2)
                return jsonify({'Actions': []}), 400

        for action in data:
            if action['name'].lower() == player_name.lower():
                return jsonify({'Action': action}), 200

        return jsonify({'Actions': []}), 400

    @action_page.route('/api/actions/<string:player_name>', methods=['DELETE'])
    def delete_action(player_name):
        """
        Delete a specific action

        Parameters
        ----------
        player_name : str

        Raises
        ------
        400
            If the actions file is empty
        404
            If the player_name don't exist
        """
        try:
            with open('files/actions.json', 'r') as json_file:
                actions = json.load(json_file)
                if not actions:
                    return jsonify({'message': 'actions is empty.'}), 400
        except FileNotFoundError:
            return jsonify({'message': 'there is no action registered.'}), 400

        for action in actions:
            if action['name'].lower() == player_name.lower():
                actions.remove(action)
                with open('files/actions.json', 'w') as json_file:
                    json.dump(actions, json_file, indent=2)
                    return '', 204

        return jsonify({'message': 'there is no player with this name.'}), 404