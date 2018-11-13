import random
import json
# this is importing a random number and json    
def start_game(max_number=10, level=1):
#start of game    
    game = {
        "number": random.randint(1,max_number),
        "max": max_number,
        "level": level, 
        "guesses": 0,
    }
    #this is how the game will work for instance the answers would be a randomized number
    return game
    
def save_game_data(data):
    with open("game_data.json", 'wb') as f:
        f.write(json.dumps(data, indent=4))
# this is saving the game data
# Jim helped me put this in place as i didnt understand how to store my data
def get_game_data():
    try:
        with open("game_data.json", 'rb') as f:
            return json.loads(f.read())
    except Exception:
        return {"players": {}}
    # this is getting and returning data
    # Jim helped me get and return the data
def get_leaderboard():
    game_data = get_game_data()
    leaders = []
    for k,v in game_data['players'].items():
        player = {"player": k, "results": v}
        player["total_guesses"] = v.get("1", 0) + v.get("2", 0) + v.get("3", 0)
        leaders.append(player)
        #this is getting the game data
        # Jim helped me with this part
    # this is calculating the answer to be put in the leaderboard
    leaders = sorted(leaders, key= lambda p: p["total_guesses"])    
    leaders = leaders[:10]
    print("leaders", leaders)
    return leaders
     # this is calculating the total guesses and putting the users in the correct place on the leaderboard
     # Jim helped me with this as i struggled to get my answers on to the leaderboard
    
    
    # end of project