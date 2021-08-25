#read nba data , lets pic players currently active
import requests
import json
import pandas as pd
import nba.team as t
import nba.player as p
from ast import literal_eval
import pandasql as ps

def getPlayers(per_page,page_num):
    response = requests.get(f"https://www.balldontlie.io/api/v1/players?per_page={per_page}&page={page_num}").json()
    return response["data"]

def getAllPlayers():
    data = []
    for i in range(1,30):
        data_array = getPlayers(100,i)
        for player in data_array:
            if "id" in player.keys():
                data.append(player)
    file1 = open("players.json",'w')
    file1.write(str(data))

def read_files_from_file(file_name):
    players_obj = []
    with open(file_name,'r') as players:
        line = literal_eval(players.readline())
        for player in line:
            players_obj.append(p.Player(player))
    return players_obj

def df_files_from_file(file_name):
    players_obj = None
    with open(file_name,'r') as players:
        players_obj = pd.DataFrame.from_records(literal_eval(players.readline()))
    return players_obj

def getTeamId(row):
    team = literal_eval(row['team'])
    return team['id']

def main():
    getAllPlayers()
    #p = read_files_from_file("players.json")
    c = df_files_from_file("players.json")
    full_players_details = c.applymap(str)
    full_players_details["team_id"] = full_players_details.apply (lambda row: getTeamId(row), axis=1)
    full_players_details
    team = pd.json_normalize(full_players_details.team.apply(literal_eval))

    print(full_players_details.groupby(['team_id']).count())

    #print(p.count)
    #print(p[:5])

if __name__ == '__main__':
    main()
