import json
from config import create_app


BASE = 'http://127.0.0.1:5000/api'
client = create_app()

class TestPlayer():

    def test_get_all_players(self):
        data = {}
        with open('files/players.json', 'r') as json_file:
            data['Players'] = json.load(json_file)

        response = client.test_client().get(BASE + '/players')
        assert json.loads(response.data.decode('utf-8')) == data
        assert response.status_code == 200

    def test_get_player_by_name(self):
        data = {
            'Player': {
                "name": "Jogador 1"
            }
        }
        client.test_client().post(BASE + '/players', json={"name":"Jogador 1"})
        player_name = 'jogador 1'
        response = client.test_client().get(BASE + f'/players/{player_name}')
        assert json.loads(response.data.decode('utf-8')) == data
        assert response.status_code == 200
        client.test_client().delete(BASE + '/players/Jogador%201')

    def test_create_player(self):
        payload = {
            "name": "Jogador Teste 1000"
        }

        data = {
            "Player": {
                "name": "Jogador Teste 1000"
            }
        }

        response = client.test_client().post(BASE + '/players', json=payload)
        assert json.loads(response.data.decode('utf-8')) == data
        assert response.status_code == 201
        client.test_client().delete(BASE + f"/players/{'jogador Teste 1000'}")

    def test_create_players_existing_name(self):
        payload = {
            "name": "Jogador Teste 1000"
        }

        data = {
            "message": "there is already a player with this name."
        }

        client.test_client().post(BASE + '/players', json=payload)
        response = client.test_client().post(BASE + '/players', json=payload)
        assert json.loads(response.data.decode('utf-8')) == data
        assert response.status_code == 400
        client.test_client().delete(BASE + f"/players/{'jogador Teste 1000'}")

    def test_create_player_with_wrong_key(self):
        payload = {
            "nameeee": "Jogador Teste 1000"
        }
        data = {
            'message': 'can not create player with the key.'
        }
        response = client.test_client().post(BASE + '/players', json=payload)
        assert json.loads(response.data.decode('utf-8')) == data
        assert response.status_code == 400

    def test_create_player_empty_name(self):
        payload = {
            "name": ""
        }
        data = {
            'message': 'can not create player with a empty name.'
        }
        response = client.test_client().post(BASE + '/players', json=payload)
        assert json.loads(response.data.decode('utf-8')) == data
        assert response.status_code == 400

    def test_delete_player(self):
        payload = {
            "name": "Jogador Teste 1000"
        }
        client.test_client().post(BASE + '/players', json=payload)
        response = client.test_client().delete(BASE + "/players/jogador Teste 1000")
        assert response.status_code == 204