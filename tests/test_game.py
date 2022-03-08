import json
from config import create_app


BASE = 'http://127.0.0.1:5000/api'
client = create_app()

with open('tests/fixture_players.json', 'r') as json_file:
    players = json.load(json_file)

with open('tests/fixture_actions.json', 'r') as json_file:
    actions = json.load(json_file)


class TestGame:
    """
    Save the current data from actions.json and clean the actions file
    """
    with open('files/actions.json', 'r') as json_file:
        actions_current_data = json.load(json_file)

    def clean_actions_file(self):
        with open('files/actions.json', 'w') as json_file:
            json.dump([], json_file, indent=2)
        return True
    
    def create_player_and_action(self, player, action):
        client.test_client().post(BASE + '/players', json=player)
        client.test_client().post(BASE + '/actions', json=action)
        return player, action

    def delete_player(self, players):
        for player in players:
            player_name = player['name']
            client.test_client().delete(BASE + f'/players/{player_name}')
        
        return True

    """
    ACTIONS: ROCK and PAPER
    RESULT: PAPER
    """
    def test_game_rock_paper(self):
        expected_result = {
            "Action": "Papel",
            "Winners": [
                'Jogador Teste 2'
            ]
        }
        self.create_player_and_action(players[0], actions[0])
        self.create_player_and_action(players[1], actions[1])
        response = client.test_client().get(BASE + '/game')
        assert json.loads(response.data.decode('utf-8')) == expected_result
        assert response.status_code == 200
        self.delete_player([players[0], players[1]])
        self.clean_actions_file()

    """
    ACTIONS: ROCK and SCISSOR
    RESULT: ROCK
    """
    def test_game_rock_scissor(self):
        expected_result = {
            "Action": "Pedra",
            "Winners": [
                'Jogador Teste 1'
            ]
        }
        self.create_player_and_action(players[0], actions[0])
        self.create_player_and_action(players[2], actions[2])
        response = client.test_client().get(BASE + '/game')
        assert json.loads(response.data.decode('utf-8')) == expected_result
        assert response.status_code == 200
        self.delete_player([players[0], players[2]])
        self.clean_actions_file()

    """
    ACTIONS: ROCK and SPOCK
    RESULT: SPOCK
    """
    def test_game_rock_spock(self):
        expected_result = {
            "Action": "Spock",
            "Winners": [
                'Jogador Teste 4'
            ]
        }
        self.create_player_and_action(players[0], actions[0])
        self.create_player_and_action(players[3], actions[3])
        response = client.test_client().get(BASE + '/game')
        assert json.loads(response.data.decode('utf-8')) == expected_result
        assert response.status_code == 200
        self.delete_player([players[0], players[3]])
        self.clean_actions_file()

    """
    ACTIONS: ROCK and LIZARD
    RESULT: ROCK
    """
    def test_game_rock_lizard(self):
        expected_result = {
            "Action": "Pedra",
            "Winners": [
                'Jogador Teste 1'
            ]
        }
        self.create_player_and_action(players[0], actions[0])
        self.create_player_and_action(players[4], actions[4])
        response = client.test_client().get(BASE + '/game')
        assert json.loads(response.data.decode('utf-8')) == expected_result
        assert response.status_code == 200
        self.delete_player([players[0], players[4]])
        self.clean_actions_file()

    """
    ACTIONS: PAPPER and SCISSOR
    RESULT: SCISSOR
    """
    def test_game_paper_scissor(self):
        expected_result = {
            "Action": "Tesoura",
            "Winners": [
                'Jogador Teste 3'
            ]
        }
        self.create_player_and_action(players[1], actions[1])
        self.create_player_and_action(players[2], actions[2])
        response = client.test_client().get(BASE + '/game')
        assert json.loads(response.data.decode('utf-8')) == expected_result
        assert response.status_code == 200
        self.delete_player([players[1], players[2]])
        self.clean_actions_file()

    """
    ACTIONS: PAPEL and SPOCK
    RESULT: PAPEL
    """
    def test_game_paper_spock(self):
        expected_result = {
            "Action": "Papel",
            "Winners": [
                'Jogador Teste 2'
            ]
        }
        self.create_player_and_action(players[1], actions[1])
        self.create_player_and_action(players[3], actions[3])
        response = client.test_client().get(BASE + '/game')
        assert json.loads(response.data.decode('utf-8')) == expected_result
        assert response.status_code == 200
        self.delete_player([players[1], players[3]])
        self.clean_actions_file()

    """
    ACTIONS: PAPEL and LIZARD
    RESULT: LIZARD
    """
    def test_game_paper_lizard(self):
        expected_result = {
            "Action": "Lagarto",
            "Winners": [
                'Jogador Teste 5'
            ]
        }
        self.create_player_and_action(players[1], actions[1])
        self.create_player_and_action(players[4], actions[4])
        response = client.test_client().get(BASE + '/game')
        assert json.loads(response.data.decode('utf-8')) == expected_result
        assert response.status_code == 200
        self.delete_player([players[1], players[4]])
        self.clean_actions_file()

    """
    ACTIONS: SCISSOR and SPOCK
    RESULT: SPOCK
    """
    def test_game_scissor_spock(self):
        expected_result = {
            "Action": "Spock",
            "Winners": [
                'Jogador Teste 4'
            ]
        }
        self.create_player_and_action(players[2], actions[2])
        self.create_player_and_action(players[3], actions[3])
        response = client.test_client().get(BASE + '/game')
        assert json.loads(response.data.decode('utf-8')) == expected_result
        assert response.status_code == 200
        self.delete_player([players[2], players[3]])
        self.clean_actions_file()

    """
    ACTIONS: SCISSOR and LIZARD
    RESULT: SCISSOR
    """
    def test_game_scissor_lizard(self):
        expected_result = {
            "Action": "Tesoura",
            "Winners": [
                'Jogador Teste 3'
            ]
        }
        self.create_player_and_action(players[2], actions[2])
        self.create_player_and_action(players[4], actions[4])
        response = client.test_client().get(BASE + '/game')
        assert json.loads(response.data.decode('utf-8')) == expected_result
        assert response.status_code == 200
        self.delete_player([players[2], players[4]])
        self.clean_actions_file()

    """
    ACTIONS: SPOCK and LIZARD
    RESULT: LIZARD
    """
    def test_game_spock_lizard(self):
        expected_result = {
            "Action": "Lagarto",
            "Winners": [
                'Jogador Teste 5'
            ]
        }
        self.create_player_and_action(players[3], actions[3])
        self.create_player_and_action(players[4], actions[4])
        response = client.test_client().get(BASE + '/game')
        assert json.loads(response.data.decode('utf-8')) == expected_result
        assert response.status_code == 200
        self.delete_player([players[3], players[4]])
        self.clean_actions_file()

    """
    ACTIONS: PAPER and SPOCK and LIZARD
    RESULT: LIZARD
    """
    def test_game_paper_spock_lizard(self):
        expected_result = {
            "Action": "Lagarto",
            "Winners": [
                'Jogador Teste 5'
            ]
        }
        self.create_player_and_action(players[1], actions[1])
        self.create_player_and_action(players[3], actions[3])
        self.create_player_and_action(players[4], actions[4])
        response = client.test_client().get(BASE + '/game')
        assert json.loads(response.data.decode('utf-8')) == expected_result
        assert response.status_code == 200
        self.delete_player([players[1], players[3], players[4]])
        self.clean_actions_file()

    """
    ACTIONS: PAPER and SCISSOR and LIZARD
    RESULT: SCISSOR
    """
    def test_game_paper_spock_lizard(self):
        expected_result = {
            "Action": "Tesoura",
            "Winners": [
                'Jogador Teste 3'
            ]
        }
        self.create_player_and_action(players[1], actions[1])
        self.create_player_and_action(players[2], actions[2])
        self.create_player_and_action(players[4], actions[4])
        response = client.test_client().get(BASE + '/game')
        assert json.loads(response.data.decode('utf-8')) == expected_result
        assert response.status_code == 200
        self.delete_player([players[1], players[2], players[4]])
        self.clean_actions_file()

    """
    ACTIONS: PAPER and ROCK and SPOCK
    RESULT: PAPER
    """
    def test_game_paper_spock_lizard(self):
        expected_result = {
            "Action": "Papel",
            "Winners": [
                'Jogador Teste 2'
            ]
        }
        self.create_player_and_action(players[1], actions[1])
        self.create_player_and_action(players[0], actions[0])
        self.create_player_and_action(players[3], actions[3])
        response = client.test_client().get(BASE + '/game')
        assert json.loads(response.data.decode('utf-8')) == expected_result
        assert response.status_code == 200
        self.delete_player([players[1], players[0], players[3]])
        self.clean_actions_file()

    """
    ACTIONS: ROCK and SCISSOR and SPOCK
    RESULT: SPOCK
    """
    def test_game_paper_spock_lizard(self):
        expected_result = {
            "Action": "Spock",
            "Winners": [
                'Jogador Teste 4'
            ]
        }
        self.create_player_and_action(players[0], actions[0])
        self.create_player_and_action(players[2], actions[2])
        self.create_player_and_action(players[3], actions[3])
        response = client.test_client().get(BASE + '/game')
        assert json.loads(response.data.decode('utf-8')) == expected_result
        assert response.status_code == 200
        self.delete_player([players[0], players[2], players[3]])
        self.clean_actions_file()

    """
    ACTIONS: ROCK and SCISSOR and LIZARD
    RESULT: ROCK
    """
    def test_game_paper_spock_lizard(self):
        expected_result = {
            "Action": "Pedra",
            "Winners": [
                'Jogador Teste 1'
            ]
        }
        self.create_player_and_action(players[0], actions[0])
        self.create_player_and_action(players[2], actions[2])
        self.create_player_and_action(players[4], actions[4])
        response = client.test_client().get(BASE + '/game')
        assert json.loads(response.data.decode('utf-8')) == expected_result
        assert response.status_code == 200
        self.delete_player([players[0], players[2], players[4]])
        self.clean_actions_file()

    def test_game_without_actions(self):
        data = {
            'message': 'need at least 2 actions to play the game.'
        }
        self.clean_actions_file()
        response = client.test_client().get(BASE + '/game')
        assert json.loads(response.data.decode('utf-8')) == data
        assert response.status_code == 400
    
    with open('files/actions.json', 'w') as json_file:
        json.dump(actions_current_data, json_file, indent=2)