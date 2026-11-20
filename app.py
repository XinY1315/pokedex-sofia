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
types = open("./types", encoding = "utf10")
print(types)

def x(pokemon):
    x == len(pokedex)

def get_pokemon(pokedex):
    return pokedex

def get_moves(moves):
    x = get_moves(data)
    return moves

def get_types(types):
    return types


def words(data):
    language = input("What language do you want to see? Choose from English, Chinese, Japanese, and French.")
    if language == "English":
        print(pokedex[1])
    elif language == "Chinese":
        print(pokedex[2])
    elif language == "Japanese":
        print(pokedex[3])
    elif language == "French":
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
            print("They can do this;" + [data[2]])
        elif types == "fighting":
            print("They can do this;" + [data[2]])
        elif types == "flying":
            print("They can do this;" + [data[2]])
        elif types == "poison":
            print("They can do this;" + [data[2]])   
        elif types == "ground":
            print("They can do this;" + [data[2]])
        elif types == "rock":
            print("They can do this;" + [data[2]])
        elif types == "bug":
            print("They can do this;" + [data[2]])
        elif types == "ghost":
            print("They can do this;" + [data[2]])
        elif types == "steel":
            print("They can do this;" + [data[2]])
        elif types == "fire":
            print("They can do this;" + [data[2]])
             

def attributes(data):
    types = input("What type do you want to see? If you want to quit, type quit.")
    if types == "quit":
        print("a lying liar who lies")
    elif types == "normal":
        print([get_pokemon])
    elif types == "fighting":
        print([get_pokemon])
    elif types == "flying":
        print([get_pokemon])
    elif types == "poison":
        print([get_pokemon])
    elif types == "ground":
        print([get_pokemon])
    elif types == "rock":
        print([get_pokemon])
    elif types == "bug":
        print([get_pokemon])
    elif types == "ghost":
        print([get_pokemon])
    elif types == "steel":
        print([get_pokemon])
    elif types == "fire":
        print([get_pokemon])
    elif types == "water":
        print([get_pokemon])
    elif types == "grass":
        print([get_pokemon])
    elif types == "electric":
        print([get_pokemon])
    elif types == "psychic":
        print([get_pokemon])
    elif types == "ice":
        print([get_pokemon])
    elif types == "dragon":
        print([get_pokemon])
    elif types == "dark":
        print([get_pokemon])
    elif types == "fairy":
        print([get_pokemon])
    else:
        print("so thats not a type, try again")
    return types

def get_pokemon(pokemon):
    return pokemon
def get_moves(pokemon):
    x = get_moves(pokemon)

#inside get moves, accept argument for pokemon being searched for, call get pokemon, now make x get pokemon