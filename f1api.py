import requests
import json

constructors_championship = []

response = requests.get("http://ergast.com/api/f1/current/constructorStandings.json") 
json_data = json.loads(response.text)
data = json_data['MRData']
table = data['StandingsTable']
lists = table['StandingsLists']
for standinglist in lists:
    standings = standinglist['ConstructorStandings']
for standing in standings:  
    position = standing['position']
    points = standing['points']
    wins = standing['wins']
    constructors = standing['Constructor']
    constructorname = constructors['name']
    get_constructors = (f"{position} - {constructorname} {points} Points")
    constructors_championship.append(get_constructors)

drivers_championship = []

response = requests.get("http://ergast.com/api/f1/current/driverStandings.json") 
json_data = json.loads(response.text)
data = json_data['MRData']
table = data['StandingsTable']
lists = table['StandingsLists']
for standinglist in lists:
    standings = standinglist['DriverStandings']
for standing in standings:  
    position = standing['position']
    points = standing['points']
    wins = standing['wins']
    drivers = standing['Driver']
    code = drivers['code']
    number = drivers['permanentNumber']
    drivername = drivers['familyName']
    givenname = drivers['givenName']
    get_drivers = (f"{position} {code} {number} - {givenname} {drivername}  {points} Points - {wins} Wins")
    drivers_championship.append(get_drivers)

last_race = []

response = requests.get("http://ergast.com/api/f1/current/last/results.json") 
json_data = json.loads(response.text)
data = json_data['MRData']
table = data['RaceTable']
lists = table['Races'][0]
info = lists
racename = info['raceName']
season = info['season']
rounds = info['round']
circuit = info['Circuit']
date = info['date']
trackname = circuit['circuitName']
location = circuit['Location']
region = location['locality']
country = location['country']
raceinfo = (f"{season} {racename} - {trackname} - {region} - {country} - {date} - Round: {rounds}")
last_race.append(raceinfo)
results = info['Results']
for result in results:
    res = result
    position = res['position']
    number = res['number']
    driver = res['Driver']
    points = res['points']
    constructor = res['Constructor']
    code = driver['code']
    givenname = driver['givenName']
    familyname = driver['familyName']
    time = result.get('Time', {}).get('time')
    averagespeed = result.get('FastestLap', {}).get('AverageSpeed',{}).get('speed')
    get_race = (f"{position} {code} {number} {givenname} {familyname} - {time} - {averagespeed} kph - {points} Points")
    last_race.append(get_race)