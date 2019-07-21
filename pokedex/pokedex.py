# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 20:39:52 2019

@author: Allie
"""
import random

pokemon = {
    "1": {"Name": "Bulbasaur", "Type": "Grass/Poison", "Weakness": "Flying/Fire/Psychic/Ice", "Evolution": "First Evolution"},
    "2": {"Name": "Ivysaur", "Type": "Grass/Poison", "Weakness": "Flying/Fire/Psychic/Ice", "Evolution": "Second Evolution"},
    "3": {"Name": "Venusaur", "Type": "Grass/Poison", "Weakness": "Flying/Fire/Psychic/Ice", "Evolution": "Third Evolution"},
    "4": {"Name": "Charmander", "Type": "Fire", "Weakness": "Ground/Rock/Water", "Evolution": "First Evolution"},
    "5": {"Name": "Charmeleon", "Type": "Fire", "Weakness": "Ground/Rock/Water", "Evolution": "Second Evolution"},
    "6": {"Name": "Charizard", "Type": "Fire/Flying", "Weakness": "Rock(4x)/Water/Electric", "Evolution": "Third Evolution"},
    "7": {"Name": "Squirtle", "Type": "Water", "Weakness": "Grass/Electric", "Evolution": "First Evolution"},
    "8": {"Name": "Wartortle", "Type": "Water", "Weakness": "Grass/Electric", "Evolution": "Second Evolution"},
    "9": {"Name": "Blastoise", "Type": "Water", "Weakness": "Grass/Electric", "Evolution": "Third Evolution"},
    "10": {"Name": "Caterpie", "Type": "Bug", "Weakness": "Flying/Rock/Fire", "Evolution": "First Evolution"},
    "11": {"Name": "Metapod", "Type": "Bug", "Weakness": "Flying/Rock/Fire", "Evolution": "Second Evolution"},
    "12": {"Name": "Butterfree", "Type": "Bug/Flying", "Weakness": "Flying/Rock(4x)/Fire/Electric/Ice", "Evolution": "Third Evolution"},
    "13": {"Name": "Weedle", "Type": "Bug/Poison", "Weakness": "Flying/Rock/Fire/Psychic", "Evolution": "First Evolution"},
    "14": {"Name": "Kakuna", "Type": "Bug/Poison", "Weakness": "Flying/Rock/Fire/Psychic", "Evolution": "Second Evolution"},
    "15": {"Name": "Beedrill", "Type": "Bug/Poison", "Weakness": "Flying/Rock/Fire/Psychic", "Evolution": "Third Evolution"},
    "16": {"Name": "Pidgey", "Type": "Normal/Flying", "Weakness": "Rock/Electric/Ice", "Evolution": "First Evolution"},
    "17": {"Name": "Pidgeotto", "Type": "Normal/Flying", "Weakness": "Rock/Electric/Ice", "Evolution": "Second Evolution"},
    "18": {"Name": "Pidgeot", "Type": "Normal/Flying", "Weakness": "Rock/Electric/Ice", "Evolution": "Third Evolution"},
    "19": {"Name": "Rattata", "Type": "Normal", "Weakness": "Fighting", "Evolution": "First Evolution"},
    "20": {"Name": "Raticate", "Type": "Normal", "Weakness": "Fighting", "Evolution": "Second Evolution"},
    "21": {"Name": "Spearow", "Type": "Normal/Flying", "Weakness": "Rock/Electric/Ice", "Evolution": "First Evolution"},
    "22": {"Name": "Fearow", "Type": "Normal/Flying", "Weakness": "Rock/Electric/Ice", "Evolution": "Second Evolution"},
    "23": {"Name": "Ekans", "Type": "Poison", "Weakness": "Ground/Psychic", "Evolution": "First Evolution"},
    "24": {"Name": "Arbok", "Type": "Poison", "Weakness": "Ground/Psychic", "Evolution": "Second Evolution"},
    "25": {"Name": "Pikachu", "Type": "Electric", "Weakness": "Ground", "Evolution": "First Evolution"},
    "26": {"Name": "Raichu", "Type": "Electric", "Weakness": "Ground", "Evolution": "Second Evolution"},
    "27": {"Name": "Sandshrew", "Type": "Ground", "Weakness": "Water/Grass/Ice", "Evolution": "First Evolution"},
    "28": {"Name": "Sandslash", "Type": "Ground", "Weakness": "Water/Grass/Ice", "Evolution": "Second Evolution"},
    "29": {"Name": "Nidoran♀", "Type": "Poison", "Weakness": "Ground/Psychic", "Evolution": "First Evolution"},
    "30": {"Name": "Nidorina", "Type": "Poison", "Weakness": "Ground/Psychic", "Evolution": "Second Evolution"},
    "31": {"Name": "Nidoqueen", "Type": "Poison/Ground", "Weakness": "Ground/Water/Psychic/Ice", "Evolution": "Third Evolution"},
    "32": {"Name": "Nidoran♂", "Type": "Poison", "Weakness": "Ground/Psychic", "Evolution": "First Evolution"},
    "33": {"Name": "Nidorino", "Type": "Poison", "Weakness": "Ground/Psychic", "Evolution": "Second Evolution"},
    "34": {"Name": "Nidoking", "Type": "Poison/Ground", "Weakness": "Ground/Water/Psychic/Ice", "Evolution": "Third Evolution"},
    "35": {"Name": "Clefairy", "Type": "Fairy", "Weakness": "Poison/Steel", "Evolution": "First Evolution"},
    "36": {"Name": "Clefable", "Type": "Fairy", "Weakness": "Poison/Steel", "Evolution": "Second Evolution"},
    "37": {"Name": "Vulpix", "Type": "Fire", "Weakness": "Ground/Rock/Water", "Evolution": "First Evolution"},
    "38": {"Name": "Ninetales", "Type": "Fire", "Weakness": "Ground/Rock/Water", "Evolution": "Second Evolution"},
    "39": {"Name": "Jigglypuff", "Type": "Normal/Fairy", "Weakness": "Poison/Steel", "Evolution": "First Evolution"},
    "40": {"Name": "Wigglytuff", "Type": "Normal/Fairy", "Weakness": "Poison/Steel", "Evolution": "Second Evolution"},
    "41": {"Name": "Zubat", "Type": "Poison/Flying", "Weakness": "Rock/Electric/Psychic/Ice", "Evolution": "First Evolution"},
    "42": {"Name": "Golbat", "Type": "Poison/Flying", "Weakness": "Rock/Electric/Psychic/Ice", "Evolution": "Second Evolution"},
    "43": {"Name": "Oddish", "Type": "Grass/Poison", "Weakness": "Flying/Fire/Psychic/Ice", "Evolution": "First Evolution"},
    "44": {"Name": "Gloom", "Type": "Grass/Poison", "Weakness": "Flying/Fire/Psychic/Ice", "Evolution": "Second Evolution"},
    "45": {"Name": "Vileplume", "Type": "Grass/Poison", "Weakness": "Flying/Fire/Psychic/Ice", "Evolution": "Third Evolution"},
    "46": {"Name": "Paras", "Type": "Bug/Grass", "Weakness": "Flying(4x)/Poison/Rock/Bug/Fire/Ice", "Evolution": "First Evolution"},
    "47": {"Name": "Parasect", "Type": "Bug/Grass", "Weakness": "Flying(4x)/Poison/Rock/Bug/Fire/Ice", "Evolution": "Second Evolution"},
    "48": {"Name": "Venonat", "Type": "Bug/Poison", "Weakness": "Flying/Rock/Fire/Psychic", "Evolution": "First Evolution"},
    "49": {"Name": "Venomoth", "Type": "Bug/Poison", "Weakness": "Flying/Rock/Fire/Psychic", "Evolution": "Second Evolution"},
    "50": {"Name": "Diglett", "Type": "Ground", "Weakness": "Water/Grass/Ice", "Evolution": "First Evolution"},
    "51": {"Name": "Dugtrio", "Type": "Ground", "Weakness": "Water/Grass/Ice", "Evolution": "Second Evolution"},
    "52": {"Name": "Meowth", "Type": "Normal", "Weakness": "Fighting", "Evolution": "First Evolution"},
    "53": {"Name": "Persian", "Type": "Normal", "Weakness": "Fighting", "Evolution": "Second Evolution"},
    "54": {"Name": "Psyduck", "Type": "Water", "Weakness": "Grass/Electric", "Evolution": "First Evolution"},
    "55": {"Name": "Golduck", "Type": "Water", "Weakness": "Grass/Electric", "Evolution": "Second Evolution"},
    "56": {"Name": "Mankey", "Type": "Fighting", "Weakness": "Flying/Psychic/Fairy", "Evolution": "First Evolution"},
    "57": {"Name": "Primeape", "Type": "Fighting", "Weakness": "Flying/Psychic/Fairy", "Evolution": "Second Evolution"},
    "58": {"Name": "Growlithe", "Type": "Fire", "Weakness": "Ground/Rock/Water", "Evolution": "First Evolution"},
    "59": {"Name": "Arcanine", "Type": "Fire", "Weakness": "Ground/Rock/Water", "Evolution": "Second Evolution"},
    "60": {"Name": "Poliwag", "Type": "Water", "Weakness": "Grass/Electric", "Evolution": "First Evolution"},
    "61": {"Name": "Poliwhirl", "Type": "Water", "Weakness": "Grass/Electric", "Evolution": "Second Evolution"},
    "62": {"Name": "Poliwrath", "Type": "Water/Fighting", "Weakness": "Flying/Grass/Electric/Psychic/Fairy", "Evolution": "Third Evolution"},
    "63": {"Name": "Abra", "Type": "Psychic", "Weakness": "Bug/Ghost/Dark", "Evolution": "First Evolution"},
    "64": {"Name": "Kadabra", "Type": "Psychic", "Weakness": "Bug/Ghost/Dark", "Evolution": "Second Evolution"},
    "65": {"Name": "Alakazam", "Type": "Psychic", "Weakness": "Bug/Ghost/Dark", "Evolution": "Third Evolution"},
    "66": {"Name": "Machop", "Type": "Fighting", "Weakness": "Flying/Psychic/Fairy", "Evolution": "First Evolution"},
    "67": {"Name": "Machoke", "Type": "Fighting", "Weakness": "Flying/Psychic/Fairy", "Evolution": "Second Evolution"},
    "68": {"Name": "Machamp", "Type": "Fighting", "Weakness": "Flying/Psychic/Fairy", "Evolution": "Third Evolution"},
    "69": {"Name": "Bellsprout", "Type": "Grass/Poison", "Weakness": "Flying/Fire/Psychic/Ice", "Evolution": "First Evolution"},
    "70": {"Name": "Weepinbell", "Type": "Grass/Poison", "Weakness": "Flying/Fire/Psychic/Ice", "Evolution": "Second Evolution"},
    "71": {"Name": "Victreebel", "Type": "Grass/Poison", "Weakness": "Flying/Fire/Psychic/Ice", "Evolution": "Third Evolution"},
    "72": {"Name": "Tentacool", "Type": "Water/Poison", "Weakness": "Ground/Electric/Psychic", "Evolution": "First Evolution"},
    "73": {"Name": "Tentacruel", "Type": "Water/Poison", "Weakness": "Ground/Electric/Psychic", "Evolution": "Second Evolution"},
    "74": {"Name": "Geodude", "Type": "Rock/Ground", "Weakness": "Fighting/Ground/Steel/Water/Grass/Ice", "Evolution": "First Evolution"},
    "75": {"Name": "Graveler", "Type": "Rock/Ground", "Weakness": "Fighting/Ground/Steel/Water/Grass/Ice", "Evolution": "Second Evolution"},
    "76": {"Name": "Golem", "Type": "Rock/Ground", "Weakness": "Fighting/Ground/Steel/Water/Grass/Ice", "Evolution": "Third Evolution"},
    "77": {"Name": "Ponyta", "Type": "Fire", "Weakness": "Ground/Rock/Water", "Evolution": "First Evolution"},
    "78": {"Name": "Rapidash", "Type": "Fire", "Weakness": "Ground/Rock/Water", "Evolution": "Second Evolution"},
    "79": {"Name": "Slowpoke", "Type": "Water/Psychic", "Weakness": "Bug/Ghost/Grass/Electric/Dark", "Evolution": "First Evolution"},
    "80": {"Name": "Slowbro", "Type": "Water/Psychic", "Weakness": "Bug/Ghost/Grass/Electric/Dark", "Evolution": "Second Evolution"},
    "81": {"Name": "Magnemite", "Type": "Electric/Steel", "Weakness": "Fighting/Ground/Fire", "Evolution": "First Evolution"},
    "82": {"Name": "Magneton", "Type": "Electric/Steel", "Weakness": "Fighting/Ground/Fire", "Evolution": "Second Evolution"},
    "83": {"Name": "Farfetch'd", "Type": "Normal/Flying", "Weakness": "Rock/Electric/Ice", "Evolution": "First Evolution"},
    "84": {"Name": "Doduo", "Type": "Normal/Flying", "Weakness": "Rock/Electric/Ice", "Evolution": "First Evolution"},
    "85": {"Name": "Dodrio", "Type": "Normal/Flying", "Weakness": "Rock/Electric/Ice", "Evolution": "Second Evolution"},
    "86": {"Name": "Seel", "Type": "Water", "Weakness": "Grass/Electric", "Evolution": "First Evolution"},
    "87": {"Name": "Dewgong", "Type": "Water/Ice", "Weakness": "Fighting/Rock/Grass/Electric", "Evolution": "Second Evolution"},
    "88": {"Name": "Grimer", "Type": "Poison", "Weakness": "Ground/Psychic", "Evolution": "First Evolution"},
    "89": {"Name": "Muk", "Type": "Poison", "Weakness": "Ground/Psychic", "Evolution": "Second Evolution"},
    "90": {"Name": "Shellder", "Type": "Water", "Weakness": "Grass/Electric", "Evolution": "First Evolution"},
    "91": {"Name": "Cloyster", "Type": "Water/Ice", "Weakness": "Fighting/Rock/Grass/Electric", "Evolution": "Second Evolution"},
    "92": {"Name": "Gastly", "Type": "Ghost/Poison", "Weakness": "Ghost/Psychic/Dark", "Evolution": "First Evolution"},
    "93": {"Name": "Haunter", "Type": "Ghost/Poison", "Weakness": "Ghost/Psychic/Dark", "Evolution": "Second Evolution"},
    "94": {"Name": "Gengar", "Type": "Ghost/Poison", "Weakness": "Ground/Ghost/Psychic/Dark", "Evolution": "Third Evolution"},
    "95": {"Name": "Onix", "Type": "Rock/Ground", "Weakness": "Fighting/Ground/Steel/Water/Grass/Ice", "Evolution": "First Evolution"},
    "96": {"Name": "Drowzee", "Type": "Psychic", "Weakness": "Bug/Ghost/Dark", "Evolution": "First Evolution"},
    "97": {"Name": "Hypno", "Type": "Psychic", "Weakness": "Bug/Ghost/Dark", "Evolution": "Second Evolution"},
    "98": {"Name": "Krabby", "Type": "Water", "Weakness": "Grass/Electric", "Evolution": "First Evolution"},
    "99": {"Name": "Kingler", "Type": "Water", "Weakness": "Grass/Electric", "Evolution": "Second Evolution"},
    "100": {"Name": "Voltorb", "Type": "Electric", "Weakness": "Ground", "Evolution": "First Evolution"},
    "101": {"Name": "Electrode", "Type": "Electric", "Weakness": "Ground", "Evolution": "Second Evolution"},
    "102": {"Name": "Exeggcute", "Type": "Grass/Psychic", "Weakness": "Flying/Poison/Bug(4x)/Ghost/Fire/Ice/Dark", "Evolution": "First Evolution"},
    "103": {"Name": "Exeggutor", "Type": "Grass/Psychic", "Weakness": "Flying/Poison/Bug(4x)/Ghost/Fire/Ice/Dark", "Evolution": "Second Evolution"},
    "104": {"Name": "Cubone", "Type": "Ground", "Weakness": "Water/Grass/Ice", "Evolution": "First Evolution"},
    "105": {"Name": "Marowak", "Type": "Ground", "Weakness": "Water/Grass/Ice", "Evolution": "Second Evolution"},
    "106": {"Name": "Hitmonlee", "Type": "Fighting", "Weakness": "Flying/Psychic/Fairy", "Evolution": "First Evolution"},
    "107": {"Name": "Hitmonchan", "Type": "Fighting", "Weakness": "Flying/Psychic/Fairy", "Evolution": "First Evolution"},
    "108": {"Name": "Lickitung", "Type": "Normal", "Weakness": "Fighting", "Evolution": "First Evolution"},
    "109": {"Name": "Koffing", "Type": "Poison", "Weakness": "Psychic", "Evolution": "First Evolution"},
    "110": {"Name": "Weezing", "Type": "Poison", "Weakness": "Psychic", "Evolution": "Second Evolution"},
    "111": {"Name": "Rhyhorn", "Type": "Ground/Rock", "Weakness": "Fighting/Ground/Steel/Water(4x)/Grass(4x)/Ice", "Evolution": "First Evolution"},
    "112": {"Name": "Rhydon", "Type": "Ground/Rock", "Weakness": "Fighting/Ground/Steel/Water(4x)/Grass(4x)/Ice", "Evolution": "Second Evolution"},
    "113": {"Name": "Chansey", "Type": "Normal", "Weakness": "Fighting", "Evolution": "First Evolution"},
    "114": {"Name": "Tangela", "Type": "Grass", "Weakness": "Flying/Poison/Bug/Fire/Ice", "Evolution": "First Evolution"},
    "115": {"Name": "Kangaskhan", "Type": "Normal", "Weakness": "Fighting", "Evolution": "First Evolution"},
    "116": {"Name": "Horsea", "Type": "Water", "Weakness": "Grass/Electric", "Evolution": "First Evolution"},
    "117": {"Name": "Seadra", "Type": "Water", "Weakness": "Grass/Electric", "Evolution": "Second Evolution"},
    "118": {"Name": "Goldeen", "Type": "Water", "Weakness": "Grass/Electric", "Evolution": "First Evolution"},
    "119": {"Name": "Seaking", "Type": "Water", "Weakness": "Grass/Electric", "Evolution": "Second Evolution"},
    "120": {"Name": "Staryu", "Type": "Water", "Weakness": "Grass/Electric", "Evolution": "First Evolution"},
    "121": {"Name": "Starmie", "Type": "Water/Psychic", "Weakness": "Bug/Ghost/Grass/Electric/Dark", "Evolution": "Second Evolution"},
    "122": {"Name": "Mr. Mime", "Type": "Psychic/Fairy", "Weakness": "Poison/Ghost/Steel", "Evolution": "First Evolution"},
    "123": {"Name": "Scyther", "Type": "Bug/Flying", "Weakness": "Flying/Rock/Fire/Electric/Ice", "Evolution": "First Evolution"},
    "124": {"Name": "Jynx", "Type": "Ice/Psychic", "Weakness": "Rock/Bug/Ghost/Steel/Fire/Dark", "Evolution": "First Evolution"},
    "125": {"Name": "Electabuzz", "Type": "Electric", "Weakness": "Ground", "Evolution": "First Evolution"},
    "126": {"Name": "Magmar", "Type": "Fire", "Weakness": "Ground/Rock/Water", "Evolution": "First Evolution"},
    "127": {"Name": "Pinsir", "Type": "Bug", "Weakness": "Flying/Rock/Fire", "Evolution": "First Evolution"},
    "128": {"Name": "Tauros", "Type": "Normal", "Weakness": "Fighting", "Evolution": "First Evolution"},
    "129": {"Name": "Magikarp", "Type": "Water", "Weakness": "Grass/Electric", "Evolution": "First Evolution"},
    "130": {"Name": "Gyarados", "Type": "Water/Flying", "Weakness": "Rock/Electric", "Evolution": "Second Evolution"},
    "131": {"Name": "Lapras", "Type": "Water/Ice", "Weakness": "Fighting/Rock/Grass/Electric", "Evolution": "First Evolution"},
    "132": {"Name": "Ditto", "Type": "Normal", "Weakness": "Fighting", "Evolution": "First Evolution"},
    "133": {"Name": "Eevee", "Type": "Normal", "Weakness": "Fighting", "Evolution": "First Evolution"},
    "134": {"Name": "Vaporeon", "Type": "Water", "Weakness": "Grass/Electric", "Evolution": "Second Evolution"},
    "135": {"Name": "Jolteon", "Type": "Electric", "Weakness": "Ground", "Evolution": "Second Evolution"},
    "136": {"Name": "Flareon", "Type": "Fire", "Weakness": "Ground\Rock\Water", "Evolution": "Second Evolution"},
    "137": {"Name": "Porygon", "Type": "Normal", "Weakness": "Fighting", "Evolution": "First Evolution"},
    "138": {"Name": "Omanyte", "Type": "Rock/Water", "Weakness": "Fighting/Ground/Grass(4x)/Electric", "Evolution": "First Evolution"},
    "139": {"Name": "Omastar", "Type": "Rock/Water", "Weakness": "Fighting/Ground/Grass(4x)/Electric", "Evolution": "Second Evolution"},
    "140": {"Name": "Kabuto", "Type": "Rock/Water", "Weakness": "Fighting/Ground/Grass(4x)/Electric", "Evolution": "First Evolution"},
    "141": {"Name": "Kabutops", "Type": "Rock/Water", "Weakness": "Fighting/Ground/Grass(4x)/Electric", "Evolution": "Second Evolution"},
    "142": {"Name": "Aerodactyl", "Type": "Rock/Flying", "Weakness": "Rock/Steel/Water/Electric/Ice", "Evolution": "First Evolution"},
    "143": {"Name": "Snorlax", "Type": "Normal", "Weakness": "Fighting", "Evolution": "First Evolution"},
    "144": {"Name": "Articuno", "Type": "Ice/Flying", "Weakness": "Rock/Steel/Fire/Electric", "Evolution": "First Evolution"},
    "145": {"Name": "Zapdos", "Type": "Electric/Flying", "Weakness": "Rock/Ice", "Evolution": "First Evolution"},
    "146": {"Name": "Moltres", "Type": "Fire/Flying", "Weakness": "Rock/Water/Electric", "Evolution": "First Evolution"},
    "147": {"Name": "Dratini", "Type": "Dragon", "Weakness": "Ice/Dragon/Fairy", "Evolution": "First Evolution"},
    "148": {"Name": "Dragonair", "Type": "Dragon", "Weakness": "Ice/Dragon/Fairy", "Evolution": "Second Evolution"},
    "149": {"Name": "Dragonite", "Type": "Dragon/Flying", "Weakness": "Rock/Ice(4x)/Dragon/Fairy", "Evolution": "First Evolution"},
    "150": {"Name": "Mewtwo", "Type": "Psychic", "Weakness": "Bug/Ghost/Dark", "Evolution": "First Evolution"},
    "151": {"Name": "Mew", "Type": "Psychic", "Weakness": "Bug/Ghost/Dark", "Evolution": "First Evolution"},
    }

def pokemoninformation(choice, pokedex_choice):
    print("\nThe Pokemon's Name is: %s!\n" % pokemon[choice]["Name"])
    while pokedex_choice != 4:
        try:
            pokedex_choice = int(input("Please choose from the following options: \n"
                                   "1.) Pokemon's Type\n"
                                   "2.) Pokemon's Weakness\n"
                                   "3.) Pokemon's Evolution Level\n"
                                   "4.) Exit to Main Menu\n"))
            if pokedex_choice == 1:
                print("%s's type is: %s!\n" % (pokemon[choice]["Name"], pokemon[choice]["Type"]))
            elif pokedex_choice == 2:
                print("%s is weak to: %s!\n" % (pokemon[choice]["Name"], pokemon[choice]["Weakness"]))
            elif pokedex_choice == 3:
                print("%s is a %s!\n" % (pokemon[choice]["Name"], pokemon[choice]["Evolution"]))
            elif pokedex_choice == 4:
                print("Returning to Main Menu!")
                break
            else:
                print("Invalid Choice! Please choose a valid option: 1 through 4!\n")
                sub_choice = int(input("1.) Pokemon's Type\n"
                                       "2.) Pokemon's Weakness\n"
                                       "3.) Pokemon's Evolution Level\n"
                                       "4.) Exit to Main Menu\n"))
        except ValueError:
            print("That is not a value of 1-4!")


if __name__ == '__main__':
    choice = 0
    while choice != "-1":
        choice = input("Please enter a Pokedex Number, Type in '0' for a random Pokemon, or type '-1' to exit!: ")
        if choice == "-1":
            print("Goodbye Trainer!")
            break
        elif choice == "0":
            choice = str(random.randint(1, 151))
            pokemoninformation(choice, pokedex_choice=0)
        elif choice in pokemon.keys():
            pokemoninformation(choice, pokedex_choice=0)
        else:
            print("You typed in %s. Correct?" % choice)
