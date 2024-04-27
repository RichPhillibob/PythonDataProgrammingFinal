import sqlite3
from contextlib import closing
from objects import Player, Lineup

conn = None

def connect():
    global conn
    if not conn:
        DB_FILE = 'player_db.sqlite'
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()

def make_player(row):
    return Player(row['batOrder'], row['firstName'], row['lastName'],
                  row['position'], row['atBats'], row['hits'])

def make_player_list(results):
    players = []
    for row in results:
        players.append(make_player(row))
    return players

def get_players():
    query = '''SELECT *
               FROM Player'''
    with closing(conn.cursor()) as c:
        c.execute(query)
        results = c.fetchall()

    return make_player_list(results)

def get_player(number):
    query = '''SELECT *
               FROM Player
               WHERE PlayerID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (number))
        row = c.fetchone()
        if row:
            return make_player(row)
        else:
            return None

def add_player(player):
    query = '''INSERT INTO Player (batOrder, firstName, lastName, position, atBats, hits)
               VALUES (?, ?, ?, ?, ?, ?)'''
    with closing(conn.cursor()) as c:
        c.execute(query, (player.batOrder, player.firstName, player.lastName,
                          player.position, player.atBats, player.hits))
        conn.commit()

def delete_player(number):
    query = '''DELETE FROM Player
               WHERE PlayerID = ?'''
    with closing(conn.cursor()) as c:
        c.execute(query, (number))
        conn.commit()

def update_bat_order(number):
    query = '''UPDATE Players
               SET batOrder = ?
               WHERE PlayerID = ?'''
    new_bat_order = input('New bat number: ')
    with closing(conn.cursor()) as c:
        c.execute(query, (number, new_bat_order))
        conn.commit()

























    
