import json
from config import create_app


BASE = 'http://127.0.0.1:5000/api'
client = create_app()

class TestAction():

    def test_get_all_actions(self):
        data = {}
        with open('files/actions.json', 'r') as json_file:
            data['Actions'] = json.load(json_file)

        response = client.test_client().get(BASE + '/actions')
        assert json.loads(response.data.decode('utf-8')) == data
        assert response.status_code == 200

    def test_get_action_by_name(self):
        payload = {
            "name": "Jogador Teste 1001",
            "action": "Pedra"
        }
        expected_result = {
            "Action": {
                "name": "Jogador Teste 1001",
                "action": "Pedra"
            }
        }
        client.test_client().post(BASE + '/players', json={"name": "Jogador Teste 1001"})
        client.test_client().post(BASE + '/actions', json=payload)
        response = client.test_client().get(BASE + '/actions/Jogador Teste 1001')
        assert json.loads(response.data.decode('utf-8')) == expected_result
        assert response.status_code == 200
        client.test_client().delete(BASE + '/players/Jogador Teste 1001')

    def test_create_action(self):
        payload = {
            "name": "Jogador Teste 1001",
            "action": "Pedra"
        }
        expected_result = {
            "Action": {
                "name": "Jogador Teste 1001",
                "action": "Pedra"
            }
        }
        client.test_client().post(BASE + '/players', json={"name": "Jogador Teste 1001"})
        response = client.test_client().post(BASE + '/actions', json=payload)
        assert json.loads(response.data.decode('utf-8')) == expected_result
        assert response.status_code == 201
        client.test_client().delete(BASE + '/players/Jogador Teste 1001')

    def test_delete_action(self):
        payload_player = {
            "name": "Jogador Teste 1001"
        }
        payload_action = {
            "name": "Jogador Teste 1001",
            "action": "Papel"
        }
        client.test_client().post(BASE + '/players', json=payload_player)
        client.test_client().post(BASE + '/actions', json=payload_action)
        response = client.test_client().delete(BASE + "/actions/jogador Teste 1001")
        assert response.status_code == 204
        client.test_client().delete(BASE + '/players/Jogador Teste 1001')

    def test_delete_action_noexistent_player(self):
        payload_player = {
            "name": "Jogador Teste 1001"
        }
        payload_action = {
            "name": "Jogador Teste 1001",
            "action": "Papel"
        }
        expected_result = {
            "message": "there is no player with this name."
        }
        client.test_client().post(BASE + '/players', json=payload_player)
        client.test_client().post(BASE + '/actions', json=payload_action)
        response = client.test_client().delete(BASE + "/actions/jogador Teste 1002")
        client.test_client().delete(BASE + '/players/Jogador Teste 1001')
        assert json.loads(response.data.decode('utf-8')) == expected_result
        assert response.status_code == 404
        
    def test_create_action_without_player(self):
        payload = {
            "action": "Papel"
        }
        expected_result = {
            "message": "wrong key name: "
        }
        response = client.test_client().post(BASE + "/actions", json=payload)
        assert json.loads(response.data.decode('utf-8')) == expected_result
        assert response.status_code == 400