import random
def play():
    player = input
    opponent = random.choice
    print("Choose Your Pokémon!")
    print("(Select Type)")
    input()
    Pokémon = {
        "Bug": {
    "name": "Genesect",
    "quick attack": "Fury Cutter",
    "charge attack": "X-Scissor",
},
        "Dark": {
    "name": "Mega Tyranitar",
    "quick attack": "Bite",
    "charge attack": "Brutal Swing",
},
        "Dragon": {
     "name": "Mega Rayquaza",
    "quick attack": "Dragon Tail",
    "charge attack": "Breaking Swipe",
},
        "Electric": {
    "name": "Zekrom",
    "quick attack": "Charge Beam",
    "charge attack": "Fusion Bolt",
},
        "Fairy": {
    "name": "Zacian (Crowned Sword)",
    "quick attack": "Snarl",
    "charge attack": "Play Rough",
},
        "Fighting": {
    "name": "Zamazenta (Crowned Shield)",
    "quick attack": "Snarl",
    "charge attack": "Close Combat",
},
        "Fire": {
    "name": "Primal Groudon",
    "quick attack":  "Mudshot",
    "charge attack":  "Pricipice Blades",
},
        "Flying": {
    "name": "Rayquaza",
    "quick attack": "Air Slash",
    "charge attack": "Dragon Ascent",
},
        "Ghost": {
    "name": "Giratina",
    "quick attack": "Shadow Claw",
    "charge attack": "Shadow Force",
},
        "Grass": {
    "name": "Celebi",
    "quick attack": "Magical",
    "charge attack": "Leaf Storm",
},
        "Ground": {
    "name": "Groudon",
    "quick attack": "Mud Shot",
    "charge attack": "Precipice Blades",
},
        "Ice": {
    "name": "Kyurem",
    "quick attack": "Dragon Breath",
    "charge attack": "Glaciate",
},
        "Normal": {
    "name":  "Arceus",
    "quick attack": "Iron Tail",
    "charge attack": "Hyper Beam",
},
        "Poison": {
    "name": "Eternatus",
    "quick attack": "Poison Jab",
    "charge attack": "Cross Poison",
},
        "Psychic": {
    "name": "Mewtwo",
    "quick attack": "Confusion",
    "charge attack": "Psystrike",
},
        "Rock": {
    "name": "Lycanroc (Midday)",
    "quick attack": "Rock Throw",
    "charge attack": "Stone Edge",
},
        "Steel": {
    "name": "Zamazenta (Crowned Shield)",
    "quick attack": "Metal Claw",
    "charge attack": "Iron Head"
},
        "Water": {
    "name": "Primal Kyogre",
    "quick attack": "Waterfall",
    "charge attack": "Origin Pulse", 
}
    }
    is_win = (player == "Bug" and opponent == "Dark", "Grass", "Psychic") or (player == "Dark" and opponent == "Ghost", "Psychic") or (player == "Dragon" and opponent == "Dragon") or (player == "Electric" and opponent == "Flying", "Water") or (player == "Fairy" and opponent == "Dark", "Dragon", "Fighting") or (player == "Fighting" and opponent == "Dark", "Ice", "Normal", "Rock", "Steel") or (player == "Fire" and opponent == "Bug", "Grass", "Ice", "Steel") or (player == "Flying" and opponent == "Bug", "Fighting", "Grass") or (player == "Ghost" and opponent == "Ghost", "Psychic") or (player == "Grass" and opponent == "Ground", "Rock", "Water") or (player == "Ground" and opponent == "Electric", "Fire", "Poison", "Rock", "Steel") or (player == "Ice" and opponent == "Dragon", "Flying", "Grass", "Ground") or (player == "Poison" and opponent == "Fairy", "Grass") or (player == "Psychic" and opponent == "Fighting", "Poison") or (player == "Rock" and opponent == "Bug", "Fire", "Flying", "Ice") or (player == "Steel" and opponent == "Ice", "Fairy", "Rock") or (player == "Water" and opponent == "Fire", "Ground", "Rock")
    is_loss = (player == "Bug" and opponent == "Fire", "Flying", "Rock") or (player == "Dark" and opponent == "Bug", "Fairy", "Fighting") or (player == "Dragon" and opponent == "Dragon", "Fairy", "Ice") or (player == "Electric" and opponent == "Ground") or (player == "Fairy" and opponent == "Poison", "Steel") or (player == "Fighting" and "Fairy", "Flying", "Psychic") or (player == "Flying" and opponent == "Electric", "Ice", "Rock") or (player == "Ghost" and opponent == "Dark", "Ghost") or (player == "Grass" and opponent == "Bug", "Fire", "Flying", "Ice", "Poison") or (player == "Ground" and opponent == "Grass", "Ice", "Water") or (player == "Ice" and opponent == "Fighting", "Fire", "Rock", "Steel") or (player == "Normal" and opponent == "Fighting") or (player == "Poison" and opponent == "Ground", "Psychic") or (player == "Psychic" and opponent == "Bug", "Dark", "Ghost") or (player == "Rock" and opponent == "Fighting", "Grass", "Ground", "Steel", "Water") or (player == "Steel" and opponent == "Fighting", "Fire", "Ground") or (player == "Water" and opponent == "Electric", "Grass")
    is_tie = player == opponent
    def script():
        restart = input("Play Again?" )
        if restart == "Yes" or restart == "yes":
            play()
            script()
        elif restart == "No" or restart == "no":
            print ("Thanks for playing!")
            quit()
    if is_win:
        print("Opponent's Pokémon has fainted!")
        script()
    if is_loss:
        print("Your Pokémon has fainted!")
        script()
    if is_tie:
        print("Pokémon too evenly matched!")
        script()
play()  