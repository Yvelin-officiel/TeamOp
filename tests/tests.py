import os
import sys
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../example')))

import client

PORT = 8080
URL = f"http://127.0.0.1:{PORT}"
username = "testuser"
game = client.Game(username)
with open(f"./{username}.json", "r") as f:
    data = json.load(f)
player_id = data["playerId"]
station_id = data["stationId"]

def test_game_init():
    assert isinstance(game, client.Game)
    print("Game initialized with username: testuser")


def test_player_initial_money():
    status = game.get(f"/player/{player_id}")
    assert status["money"] == 72000.0, "Initial money should be 72000.0"
    print (f"Player money: {status["money"]}")

def test_ship_buying():
    ship = game.buy_first_ship(player_id, self.sta)
    assert ship is not None, "Ship should be bought successfully"
    print(f"Ship bought: {ship}")
    
def scenario_player_starting():
    test_game_init()
    test_player_initial_money()
    test_ship_buying()

scenario_player_starting()

