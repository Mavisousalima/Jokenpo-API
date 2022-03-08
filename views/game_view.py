import json
from flask import jsonify, Blueprint


game_page = Blueprint('game_page', __name__)

class GameView():
    """
    A class that calculate the result of the game
    ...

    Methods
    -------
    play_game
        Get the actions in actions.json and return the winner(s)
    """

    @game_page.route('/api/game', methods=['GET'])
    def play_game():
        """
        Get the actions in actions.json and return the winner(s)
        
        Raises
        ------
        400
            If there is less then 2 actions
        """
        with open('files/actions.json', 'r') as json_file:
            data = json.load(json_file)
    
        if not data or len(data) < 2:
            return jsonify({'message': 'need at least 2 actions to play the game.'}), 400

        paper = False # True if someone choose paper
        rock = False  # True if someone choose rock
        scissor = False # True if someone choose scissor
        spock = False # True if someone choose spock
        lizard = False # True if someone choose lizard

        paper_winners = [] # List all the players name that choose paper
        rock_winners = [] # List all the players name that choose rock
        scissor_winners = [] # List all the players name that choose scissor
        spock_winners = [] # List all the players name that choose spock
        lizard_winners = [] # List all the players name that choose lizard

        for action in data:
            if action['action'].lower() == 'papel':
                paper_winners.append(action['name'])
                paper = True
            elif action['action'].lower() == 'pedra':
                rock_winners.append(action['name'])
                rock = True
            elif action['action'].lower() == 'tesoura':
                scissor_winners.append(action['name'])
                scissor = True
            elif action['action'].lower() == 'spock':
                spock_winners.append(action['name'])
                spock = True
            elif action['action'].lower() == 'lagarto':
                lizard_winners.append(action['name'])
                lizard = True

        if paper == True and spock == True and lizard == True:
            return jsonify({'Winners': lizard_winners, 'Action': 'Lagarto'})
        elif paper == True and scissor == True and lizard == True:
            return jsonify({'Winners': scissor_winners, 'Action': 'Tesoura'})
        elif paper == True and rock == True and spock == True:
            return jsonify({'Winners': paper_winners, 'Action': 'Papel'})
        elif rock == True and scissor == True and spock == True:
            return jsonify({'Winners': spock_winners, 'Action': 'Spock'})
        elif rock == True and scissor == True and lizard == True:
            return jsonify({'Winners': rock_winners, 'Action': 'Pedra'})
        elif paper == True and rock == True:
            return jsonify({'Winners': paper_winners, 'Action': 'Papel'})
        elif paper == True and scissor == True:
            return jsonify({'Winners': scissor_winners, 'Action': 'Tesoura'})
        elif paper == True and spock == True:
            return jsonify({'Winners': paper_winners, 'Action': 'Papel'})
        elif paper == True and lizard == True:
            return jsonify({'Winners': lizard_winners, 'Action': 'Lagarto'})
        elif rock == True and scissor == True:
            return jsonify({'Winners': rock_winners, 'Action': 'Pedra'})
        elif rock == True and spock == True:
            return jsonify({'Winners': spock_winners, 'Action': 'Spock'})
        elif rock == True and lizard == True:
            return jsonify({'Winners': rock_winners, 'Action': 'Pedra'})
        elif scissor == True and spock == True:
            return jsonify({'Winners': spock_winners, 'Action': 'Spock'})
        elif scissor == True and lizard == True:
            return jsonify({'Winners': scissor_winners, 'Action': 'Tesoura'})
        elif spock == True and lizard == True:
            return jsonify({'Winners': lizard_winners, 'Action': 'Lagarto'})

        # EVERYTHING ELSE IS A DRAW
        return jsonify({'Winner': 'EMPATE!'})
        