#************#
#JoAnn Olney #
#10/21/2024  #
#IT-140      #
#************#


#Welcome screen
print('         *Welcome!*         ')
print('****************************')
print('A Text Based Adventure Game ')
print('****************************')
print('     Dancing with Anna      ')
print('****************************')
print(' Presented to you by JoAnn  ')
print('****************************')
print('         *2024*             ')
print('****************************')



def main():
#Dictionary of connecting rooms with their items
    game_rooms = {
        'Library' : {'East': 'Dinning Room', 'West': 'Pool', 'North': 'Theater', 'South': 'Foyer'},
        'Pool' : {'East': 'Library', 'item': 'Hand cuffs'},
        'Look Out' : {'East': 'Pool', 'item': 'Shank'},
        'Foyer' : {'East':'Bedroom', 'North': 'Library', 'item': 'Magic dance shoes'},
        'Bedroom' : {'West': 'Foyer', 'item': 'Up-n-Atomizer'},
        'Dinning Room' : {'West': 'Library', 'North': 'Casino', 'item': 'Knuckle dusters'},
        'Theater' : {'South': 'Library', 'East': 'Ballroom', 'item': 'Gold key'},
        'Ballroom' : {'West': 'Theater'} #Villain room
    }

def main():
    #Item powers
    item_pow = {
        'Hand cuffs' : 3,
        'Shank' : 16,
        'Magic dance shoes' : 38,
        'Up-n-Atomizer' : 17,
        'Knuckle dusters' : 21,
        'Gold key' : 5
    }

def print_master(event):
#Adds a master repo for 'print' text
    messages = {
    'game_intro' : "Anna Delvey is on the run and is hiding in your hotel.\n"
              "You must collect all the items within the hotel to defeat her. \n"
              "Anna must be alive for you to receive the $500,000 bounty on her. \n"
              "Dance your way through the hotel before having to take down Anna before the police get to her!. \n"
              "The only way to catch Anna is to out dance her in the locked ballroom."
              "If Anna dies you loose and the police win the money."
              "-----*Good Luck*-----\n",
    'game_rules' : "To move throughout the hotel, type: 'm'. \n"
              "Then type the direction you want to go. \n"
              "Directions allowed: North, South, East and West. \n"
              "To pick up an item, type: 'pick up'. \n "
              "To use an item when attacking type 'A'. \n"
              "To read the rules again, type: 'HELP'. \n"
              "To end the game, type: 'STOP'. \n",
    'moved_rooms' : "You have moved to [new room name]. \n",
    'no_room' : "OOPS, you can't go that way!! \n",
    'item_pick' : "You have {item} to still be picked up before moving on. \n",
    'item_room' : "You already have collected this item. \n",
    'item_added' : "You have collected the item in this room. \n",
    'item_error' : "ITEM UNAVAILABLE!! \n",
    'item_use' : "You have used [item name]. \n",
    'gold_key' : "A beautiful gold key that unlocks the ballroom. \n",
    'h_e' : "Do you want to (A) attack or (E) esacpe? \n",
    'user_health' : "Your player health is: {use_health}. \n",
    'villain_heaalth' : "Annas health is: {villian_health}. \n",
    'sighting_villain' :"Anna is in sight, do you have anything you can use to help you? \n",
    'rules_villain' : "To begin the dance battle against Anna, type: 'battle'. \n"
                      "To run from Anna, type: 'E'. \n "
                     "You must have the dance shoes on to be able to dance against Anna or use any other inventory against her. \n"
                     "Anna must be alive for you to receive the $500,000 bounty on her. \n",
    'item_villain' : "You will need these items to be able to battle and capture Anna. \n",
    'fight_villain' : "Anna awaits as you break into the ballroom. \n"
                      "She is prepared with special dance shoes and and is ready to battle. \n"
                      "She is ready to cha-cha against you, bring your other items out to help you! \n",
    'attack_villain' : "You attacked Anna and dealt {damage}. \n",
    'anna_attacks' : 'Anna has attacked you and dealt {damage}. \n',
    'capture_villain' : "Congratulations, you have captured Anna and won the bounty!! \n",
    'escape_villain' : "You have escaped back to the Theater.",
    'player_dead' : "You have died, GAME OVER!! \n",
    'invalid_com' : "Try again please, if you need to see the rules again, type 'HELP'. \n",
    }
    return messages[event]

#Variable initialization
#List for storing player inventory
dance_bag = []
items_used = []
#Character
user_name = input('Enter your name: ')
self_health = health
self_attack_pow = attack_power

def __init__(self):
    #User life out of 100
    #Villian life out of 100
    self.user_name = 100
    self.villain = 100

def switch_room(self, move, current_room):
    #Move to corresponding room
    if move in game_rooms[current_room].keys():
        return current_room == game_rooms[current_room][move]
        print(master_print('moved_rooms'))
    else:
        return (current_room, game_rooms[current_room]['item'])
        print(master_print('no_room'))

def pick_up_item(self, item, current_room):
    #If there is an item availible in the room pick it up
    #If there is not an item availible in the room report that to user
    if item == game_rooms[current_room][item] and item not in dance_bag:
        print('Item:', game_rooms[current_room][item])
        dance_bag.append(item)
        if grab_item == 'Aviable':
            dance_bag.append(game_rooms[current_room][item])
            title_message = print_master('item_added')
        elif game_rooms[current_room][item] in inventory:
            title_message = print_master('item_room')

def use_item(self, item):
    #If item is in dance bag, move to used items and remove from dance bag
    #If there is item return message
    if item == 'Unavailable':
        print(print_master('item_error'))
        return False
    elif item in dance_bag: #Use the item
        title_message = print_master('item_use')
        dance_bag.remove(item)
        items_used.append(item)
        return True

def use_gold_key(self, gold_key):
    #Use the gold key to get into the Ballroom, unlock door/ lock door
    gold_key = 'Gold key'
    use_gold_key = use_item(gold_key)
    print(print_master('gold_key'))
    if 'Ballroom' in game_rooms[current_room] is locked:
        dance_bag.remove(gold_key)
        door_unlock()
        door_unlocked('Ballroom')
        items_used.append(gold_key)
        title_message = print_master('sighting_villain')
    else:
        title_message = print_master('item_error')
        door_locked()
        door_locked('Ballroom')

def attack(self, other):
    damage = random.randint(1, self_attack_pow)
    other.health -= damage
    return damage

def fight_villain():
    #Here is the fight with the villain laid out
    #The user uses items out of their inventory that are available or not
    #The user captuers the villain or the user is defeated

    #Variable initialization
    user_go = ''
    user_go != 'E'
    title_message = master_print('fighting_villain')
    title_message = master_print('rules_villain')

    title_message = '' #Clear the prompt

    while villain_health > 0 and user_health > 0:
        action == print(print_master('h_e'))
        if action == 'A':
            damage = user_attack(villain)
            title_message = print_master('attack_villain')
        elif action == 'E':
            switch_room('West', current_room)
            title_message = print_master('escape_villian')

        if villian_health > 0 and user_health > 0:
            damage = villain_attack(user)
            print(print_master('anna_attacks'))
            print(print_master('user_health'))
            print(print_master('villain_health'))

            if user_health <= 0:
                title_messsage = print_master('player_dead')
            else:
                title_messsage = print_master('villain_capture')

def game_start():
    #Variable init
    title_message = ''
    user_go = ''
    current_room = 'Library'

    #Start the game
    print('Lets Dance!')
    print('To start game hit enter')

    #Get user name
    user_name = input('Enter your name: ')
    villain = Anna_Delvey

#Main game loop
while user_go != 'E' and not fail_game:

    #Greet the user with introduction
    title_message = master_print('game_intro')
    #Greet the user with the rules of the game
    title_message = master_print('game_rules')

    user_go = input('Enter your command: ').lower().strip()
    print()

    #Move user
    if user_go == 'm':
        switch_room = input('Type which direction you want to go: ')
        title_message = print_master('moved_rooms')
    else:
        #What happens if the user goes the wrong way
        title_message = print_master('no_room')

    #Preform check on items in dance bag
    if item in dance_bag:
        title_message = print_master('item_room')
    else:
        title_message = print_master('item_pick')

    #Capture the villian or be ccaptured by the villain
    user_go = ''
    #Title message for fighting with the villain (Anna)
    title_message = master_print('rules_villain')

    #Creating loop for fighting the villain (Anna)
    while user_health > 0 and villian_health > 0 and user_go != 'E' and not fail_game:
        title_message = print_master('fighting_villain')
        title_message = ''

    #User must enter a command to begin fight with Anna
    if current_room == 'Ballroom':
        print(print_master('item_villain'))
        print(dance_bag)
        villian_health -= item_pow(items_used.title()) #Annas health decreases x amount from users attack
        print(print_master('item_used'))
    #Anna attacks the user
    else:
        user_health -= 10 #users health decreases from Annas attack
        title_message = print_master('anna_attacks')
    if user_go == 'E':
        title_message = print_master('rules')
        break

else: #If the player types an invalid move
    title_message = print_master('invalid_com')

   #Did the user win or did Anna win?
while user_health > 0 and villian_health > 0:
       villian_attack(user_name)
       if user_health <= 0:
          title_message = print_master('player_dead')
       user_go = input('Enter your command: ').lower().strip()
       if villian_health <= 0:
          title_message = print_master('capture_villain')
          print('You won!')

       user_name = Charater("Hero", 100,  random.randint(10,20))
       villain = Charater("Villain", 100, random.randint(10,20))

       result = game_result(user_name, villain)
       print(result)





            




        


        
