import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 

#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

import json
moves = open("./moves.json", encoding = "utf9")
data += json.load(moves)
print(moves)

import json
types = open("./types", encoding = "utf7")
print(types)

def x(pokemon):
    x == len(pokedex)

def get_pokemon(pokedex):
    return pokedex

def get_moves(utf9):
    x = get_moves(data)
    return utf9

def get_types(utf8):
    x == types[utf8][data]
    return utf8


def words(data):
    language = input("What language do you want to see? Choose from English, Chinese, Japanese, and French.")
    if language.lower or language.upper == "English":
        print(pokedex[1])
    elif language.lower or language.upper == "Chinese":
        print(pokedex[2])
    elif language.lower or language.upper == "Japanese":
        print(pokedex[3])
    elif language.lower or language.upper == "French":
        print(pokedex[4])
    else:
        print("that wasn't an option try again")
        language = input("What language do you want to see? Choose from English, Chinese, Japanese, and French.")
    return language

def searching(n):
    start = input("What pokemon do you wanna see? Type a name to begin, type no to stop.")
    for pokemon in data(n):
        print(data[pokemon])
        if start == "no":
            print("fairs")
        elif start == False[data]:
            print("Not a pokemon, try again")
        elif start == [pokedex+x]:
            print([data[n]])
        else:
            start == data
            print(pokedex)
    return start

def attack(data):
    moves = input("Would you like to see the moves your pokemon can learn? If not, type no.")
    if moves == "no":
        print("la true")
    elif moves == "yes":
        if types == "normal":
            print(moves)
            print("look what they can do")
             

def attributes(data):
    types = input("What type do you want to see? If you want to quit, type quit.")
    if types == "quit":
        print("a lying liar who lies")
    elif types == pokedex("type"):
        print("name"[words])
    else:
        print("not a pokemon, try again.")
        print(types = input("What type do you want to see? If you want quit, type quit."))
    return types

def get_pokemon(pokemon):
    return pokemon
def get_moves(pokemon):
    x = get_moves(pokemon)

#inside get moves, accept argument for pokemon being searched for, call get pokemon, now make x get pokemon