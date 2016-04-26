from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from games_list import GAMES_LIST

app = Flask(__name__)
bootstrap = Bootstrap(app)

def get_games(source):
    games = []
    for row in source:
        game = row["Game"]
        games.append(game)
    return games


def get_gamedata(source, game):
    for row in source:
        if game == row["Game"]:
            number = row["Number"]
            score = row["Metascore"]
            link = row["Link"]
            date = row["Release Date"]
            length = row["Length"]
    return game, number, score, link, date, length

@app.route('/')
def home():
    games = get_games(GAMES_LIST)
    return render_template('index.html', games=games)

@app.route('/<game>')
def details(game):
    game, number, score, link, date, length = get_gamedata(GAMES_LIST, game)
    return render_template('details.html', game=game, number=number, score=score, link=link, date=date, length=length)

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
