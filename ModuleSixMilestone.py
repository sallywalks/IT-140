#******************#
#JoAnn Olney       #
#10/12/2024        #
#IT-140            #
#Mod Six Milestone #
#******************#

#A dictionary for the simplified dragon text game
#The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

#Avaible directions for user
directions = ['North', 'South', 'East', 'West']
#Starting room
starting_room = ['Great Hall']

#To go the correct way
while True:
    if starting_room == ['name'] == 'Cellar':
        print('You have have won and reached the Cellar')
        break
elif starting_room['name'] == 'Exit':
    print('Game ended!!')

#Get the user input
send = input('\Where do you want to go?')
if send in starting_room:
    starting_room = starting_room[send]
else:
    #Going the wrong way
    print('Oops, you can not that way')
#To use exit command
elif send == 'exit':
    starting_room = rooms['Exit']