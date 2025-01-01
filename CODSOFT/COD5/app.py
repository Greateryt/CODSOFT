from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'rockpaperscissors' 

@app.before_request
def initialize_game():
    if 'score' not in session:
        session['score'] = {'wins': 0, 'losses': 0, 'draws': 0}

@app.route('/')
def home():
    return render_template('index/home.html', score=session['score'], result=None)

@app.route('/play/<choice>')
def play(choice):
    moves = ['rock', 'paper', 'scissors']
    if choice not in moves:
        return redirect(url_for('home'))

    computer_choice = random.choice(moves)
    if choice == computer_choice:
        result = "It's a draw!"
        session['score']['draws'] += 1
    elif (choice == 'rock' and computer_choice == 'scissors') or \
         (choice == 'paper' and computer_choice == 'rock') or \
         (choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
        session['score']['wins'] += 1
    else:
        result = "You lose!"
        session['score']['losses'] += 1

    session.modified = True
    return render_template('index/home.html', score=session['score'], result=f"{result} (Computer chose {computer_choice})")

@app.route('/reset')
def reset():
    session.pop('score', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
