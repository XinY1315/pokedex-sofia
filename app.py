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
print(data[1])

import json
types = open("./types", encoding = "utf10")
data += json.load(types)
print(data[2])

def searching(n):
    start = input("What pokemon do you wanna see? Type a name to begin, type no to stop.")
    for pokemon in data(n):
        print(data[pokemon])
        if start == "no":
            print("fairs")
        else:
            start == data
            print(pokedex)
            language = input("What language do you want to see? Choose from English, Chinese, Japanese, and French.")
            if language == "English":
                print(data[1])
            elif language == "Chinese":
                print(data[2])
            elif language == "Japanese":
                print(data[3])
            elif language == "French":
                print(data[4])
searching()





