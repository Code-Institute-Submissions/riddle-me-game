import os
from flask import Flask, render_template, request, session, redirect
import guess
# this is importing flask, os and guess.py
app = Flask(__name__)
app.secret_key = b'_fsdfuuiwer324234'
#this allows you to set or access the session dictionary

@app.route('/', methods=('GET', 'POST'))
def index():
    session.permanent = False
    game_data = guess.get_game_data()
    print("game_data", game_data)
# this is printing the game data
# Jim helped me with this
    if request.args.get('reset', None):
        current_game = guess.start_game(max_number=10)
        session['current_game'] = current_game
        return render_template('index.html', current_game=current_game)
# this is reseting the game from the current session
# Jim helped me with this
    user_name = session.get('user_name', None)
    leaderboard = guess.get_leaderboard()
    answer = None
    result = None
    current_game = None
#game details
    if not user_name and request.method == 'POST' and request.form.get('user_name', None):
        user_name = request.form.get('user_name', None)
        session["user_name"] = user_name
# this is a flask request method
# Jim helped me do this 
    if user_name:
        current_game = session.get('current_game', None)
        #current game session
        if not current_game:
            current_game = guess.start_game(max_number=10)
            session['current_game'] = current_game
#if not current game session
# Jim helped me with this
        print(current_game)

        if request.method == 'POST' and request.form.get('answer', None):
            answer = request.form['answer']
            current_game["guesses"] += 1
            session['current_game'] = current_game
# this is getting the answer
            try:
                answer = int(answer)
            except:
                answer = -1

            right_answer = current_game["number"]
            print("right_answer", right_answer)
            # this prints the correct answer under the form
            # Jim helped me with this
            if answer == right_answer:
                player_results = game_data['players'].get(user_name, {})
                player_results[int(current_game['level'])] = current_game['guesses']
                game_data['players'][user_name] = player_results
                guess.save_game_data(game_data)
                current_game = guess.start_game(max_number=current_game["max"] + 10, level=current_game["level"] + 1)
                session['current_game'] = current_game
                result = "Right"
            # this is if the answer is correct, this also shows the users answers and the correct answers


            elif answer < right_answer:
                result = "Too Low"
            else:
                result = "Too High"
           
            if current_game["level"] == 4:   
                return render_template('gameover.html')
    
                # this is if the users answer is too high or too low, this will appear when the user has submitted an answer
    return render_template('index.html', answer=answer, result=result, user_name=user_name, current_game=current_game,
                           leaderboard=leaderboard)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
