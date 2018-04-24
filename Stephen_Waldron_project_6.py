#-----------------------------------------------------------------------------------
#Program name - Stephen_Waldron_project_6.py
#Written by - Stephen Waldron
#Date 4/15/2014
#This program is my answer to the Role Play game.
#-------------------------------------------------------------------------------
import random
import time

# set up the board max x and y veriables
MAX_X = 10
MAX_Y = 9

# Set the max number of rooms
MAX_ROOMS = 5


#-----------------------------------------------------------------------------------
#Function name - initializeBoard
#This function initializes the board
#Parameters - board
#Returns - none
#-----------------------------------------------------------------------------------
def initializeBoard(board):
    # Initialize the board
    for y in range(MAX_Y):
        board.append([])
        for x in range(MAX_X):
            # Each row will have [--------]
            board[y].append('-')

#-----------------------------------------------------------------------------------
#Function name - printBoard
#This function is the printing of the board
#Parameters - board
#Returns - none
#-----------------------------------------------------------------------------------
def printBoard(board):
    # format the board
    print(' ', end = '')
    # print the numbers of the coords across the top
    for x in range(MAX_X):
        print(x, end = '')
    print()
    # print the numbers of the coords down the sides
    for y in range(MAX_Y):
        print(y, end = '')
        boardRows = ''
        for x in range(MAX_X):
            boardRows = boardRows + board[y][x]
        print(boardRows)
    print('R are the rooms. I is the player.')

#-----------------------------------------------------------------------------------
#Function name - generateRooms
#This function is the room generation
#Parameters - rooms
#Returns - none
#-----------------------------------------------------------------------------------
def generateRooms(rooms):
    for room_number in range(MAX_ROOMS):
        place = False
        while not place:
            room = [random.randint(0, MAX_Y - 1), random.randint(0, MAX_X - 1)]
            if room not in rooms:
                rooms.append(room)
                place = True


#-----------------------------------------------------------------------------------
#Function name - placeRooms
#This function is the room placement
#Parameters - rooms, board
#Returns - none
#-----------------------------------------------------------------------------------
def placeRooms(rooms, board):   
    # Place rooms on the board
    for room in rooms:
        board[room[0]][room[1]] = 'R'

#-----------------------------------------------------------------------------------
#Function name - generatePlayer
#This function is the player generation.
#Parameters - rooms
#Returns - player
#-----------------------------------------------------------------------------------
def generatePlayer(rooms):
    playerPlaced = False
    while not playerPlaced:
        player = [random.randint(0, MAX_Y - 1), random.randint(0, MAX_X - 1)]
        if player not in rooms:
            playerPlaced = True
            #print(player)
    return player
    
#-----------------------------------------------------------------------------------
#Function name - playerInRoom
#This function is to check if the player is in a room or not.
#Parameters - player, rooms
#Returns - none
#-----------------------------------------------------------------------------------
def playerInRoom(player, rooms):
    #print(player)
    #print(rooms)
    if player in rooms:
        return True
    else:
        return False


#-----------------------------------------------------------------------------------
#Function name - placePlayer
#This function is to place the player on the board
#Parameters - player, board
#Returns - none
#-----------------------------------------------------------------------------------
def placePlayer(player, board):
    # Place the player on the board
    board[player[0]][player[1]] = 'I'

#-----------------------------------------------------------------------------------
#Function name - displayIntroduction
#This function is the introduction for this game
#Parameters - none
#Returns - none
#-----------------------------------------------------------------------------------
def displayIntroduction():
    # Indroduce the user to the game
    print('This is a role playing game.  In this game you will see things that may be')
    print('good or may be bad.  As you play the game check the random things going on.')
    print()
    time.sleep(2)
    print('You come to an area in a land far away and looks in the past.  You')
    print('look around the area and see a field with green grass.  Off in the')
    print('distance there are trees and a river.  After a further look you see')
    print('a field.')
    print()
    time.sleep(5)
    print('You enter the field and see a dragon.')
    print()
    time.sleep(2)
    print('This dragon is a good and powerful dragon and gives you 10 gold'
          + ' and 10 life.')

#-----------------------------------------------------------------------------------
#Function name - getDirection
#This function is the choice of direction
#Parameters - player             
#Returns - direction
#-----------------------------------------------------------------------------------
def getDirection(player):
    # get the player to choose a direction of travil
    print('You are now given a choice of where to go.')
    print()
    time.sleep(2)
    north = ['north', 'n']
    south = ['south', 's']
    east = ['east', 'e']
    west = ['west', 'w']
    direction = 'F'
    while not (direction in north or direction in south or direction in east
               or direction in west):
        print('Please pick a direction of travel: north, south, east or west:')
        direction = input().lower()
    return direction

#-----------------------------------------------------------------------------------
#Function name - tellRiddle
#This function is the riddle part of the game.
#Parameters - None
#Returns - correct
#-----------------------------------------------------------------------------------
def tellRiddle():
    # riddles
    print('To get to the room behind me you must first correctly answer the '
          + 'riddle.')
    print()
    time.sleep(2)
    riddles = {'I once said “Wise men speak because they have something to say,'
               + ' fools because \nthey have to say something.”  Who am I?':
               'plato', 'I have 4 paws and fur all over my body and sometimes '
               + 'play with mice. What am I?':['cat', 'a cat'],
               'Once I was small and planted in the earth.  '
               + 'Now I am tall and can feel the wind all around me. What am I?': 
               ['tree', 'a tree'], 'I am large and mostly blue.  I have many '
               + 'animals that live within me. \nWhat am I?':['ocean',
                                                              'an ocean'
                                                              'the ocean'],
               'I eat grass and was used to transport people over '
               + 'distances in the past.  What am I?':['horse', 'a horse'],
               'High in the air I go.  Fast as the wind I travel.  What am I?': 
               ['airplane', 'an airplane'], 'I protect my family by warning '
               + 'people who don’t belong around my family that \nI am there. '
               + 'What am I?':['dog', 'a dog'],
               'I once said “One of the penalties for refusing to participate '
               + 'in politics is \nthat you end up being governed by your '
               + 'inferiors.” Who am I?':'plato', 'I once said “Only the dead '
               + 'have seen the end of the war.” Who am I?':'plato',
               'I once said “My advice to you is get married: if you find a '
               + 'good wife you’ll be \nhappy; if not, you’ll become a '
               + 'philosopher.” Who am I?':'socrates'}
    questions = list(riddles.keys())
    theQuestion = random.choice(questions)
    print(theQuestion)
    theAnswer = riddles[theQuestion]
    playerAnswer = input().lower()
    if playerAnswer in theAnswer:
        print('correct')
        correct = 1
    else:
        print('incorrect')
        correct = 0
    #print(theAnswer)
    return correct

#-----------------------------------------------------------------------------------
#Function name - checkCave
#This function is the cave that the player moves into.
#Parameters - money, How much gold the player has
#             health, How much life the player has
#Returns - money and health
#-----------------------------------------------------------------------------------
def checkCave(money, health):
    # Determ weather the player gets a gift or penetly
    gift = random.randint(1, 4)
    # Next line is just for testing purposes
    #gift = 3
    # Next line is a special test line tied to the riddles
    #gift = 1
    if gift == 1:
        print('This room has a magical item that gives you life.')
        healthGain = random.randint(1, 2)
        health = health + healthGain
        print('You gain ' + str(healthGain) + ' life.')
    if gift == 2:
        print('This room has a box of gold.')
        postiveMoney = random.randint(1, 5)
        money = money + postiveMoney
        print('You gain ' + str(postiveMoney) + ' gold.')
    if gift == 3:
        print('This room has poisonous gas in it.')
        healthLoss = random.randint(1, 2)
        health = health - healthLoss
        print('You lose ' + str(healthLoss) + ' life.')
    if gift == 4:
        print('This room is full of thieves.')
        lostMoney = random.randint(1, 5)
        # Determ if the player has gold that can not go into the negitive range
        if money < 5:
            money = 0
            print('A theif steels all of your gold.')
        else:
            money = money - lostMoney
            print('You lose ' + str(lostMoney) + ' gold.')
    return money, health


#-----------------------------------------------------------------------------------
#Function name - statusLine
#This function is the status of the players health and gold.
#Parameters - money, How much gold the player has
#             health, How much life the player has
#Returns - none
#-----------------------------------------------------------------------------------
def statusLine(statusMoney, statusHealth):
    # give the player their status
    print()
    print('------------------------- Player Status --------------------------------')
    print()
    print('Gold = ' + str(statusMoney) + '     Life = ' + str(statusHealth))
    print()
    print('------------------------------------------------------------------------')
    print()
    time.sleep(2)

#-----------------------------------------------------------------------------------
#Function name - movePlayer
#This function is to move the player around the board.
#Parameters - board, rooms, player, dir
#Returns - player
#-----------------------------------------------------------------------------------
def movePlayer(board, rooms, player, dir):
    # if the player goes north
    if dir.startswith('n'):
        # if move is allowed
        # update the old location with either - if empty or R if room used in
        # all directions
        if player in rooms:
            board[player[0]][player[1]] = 'R'
        else:
            board[player[0]][player[1]] = '-'
        # update the player used in all directions
        player[0] = player[0] - 1
        # Check to make sure the player is still on the board used in all
        # directions
        if checkPlayeronBoard(player):
            player[0] = random.randint(0, MAX_Y - 1)
        # place player on board
        board[player[0]][player[1]] = 'I'
    # if the player goes south
    if dir.startswith('s'):
        if player in rooms:
            board[player[0]][player[1]] = 'R'
        else:
            board[player[0]][player[1]] = '-'
        player[0] = player[0] + 1
        if checkPlayeronBoard(player):
            player[0] = random.randint(0, MAX_Y - 1)
        board[player[0]][player[1]] = 'I'
    # if the player goes east
    if dir.startswith('e'):
        if player in rooms:
            board[player[0]][player[1]] = 'R'
        else:
            board[player[0]][player[1]] = '-'
        player[1] = player[1] + 1
        if checkPlayeronBoard(player):
            player[1] = random.randint(0, MAX_X - 1)
        board[player[0]][player[1]] = 'I'
    # if the player goes west
    if dir.startswith('w'):
        if player in rooms:
            board[player[0]][player[1]] = 'R'
        else:
            board[player[0]][player[1]] = '-'
        player[1] = player[1] - 1
        if checkPlayeronBoard(player):
            player[1] = random.randint(0, MAX_X - 1)
        board[player[0]][player[1]] = 'I'
    return player

#-----------------------------------------------------------------------------------
#Function name - checkPlayeronBoard
#This function is to make sure the player remains on the board.
#Parameters - player
#Returns - True or False
#-----------------------------------------------------------------------------------
def checkPlayeronBoard(player):
    if player[1] < 0 or player[1] > (MAX_X - 1):
        print('You are trying to leave the board I will not place you '
                + 'in a random spot on the board.')
        return True
    if player[0] < 0 or player[0] > (MAX_Y - 1):
        print('You are trying to leave the board I will not place you '
                + 'in a random spot on the board.')
        return True
    else:
        return False
        
    
# Main program
# Initialize the variables
theBoard = []
theRooms = []
thePlayer = []
gold = 10
life = 10

# Set up the board
initializeBoard(theBoard)
generateRooms(theRooms)
placeRooms(theRooms, theBoard)

thePlayer = generatePlayer(theRooms)

placePlayer(thePlayer, theBoard)

# Display the intro
displayIntroduction()

# Show the board
printBoard(theBoard)

# Show player status
statusLine(gold, life)
# Play again loop

playAgain = 'yes'
incorrect = 0
while playAgain == 'yes' or playAgain == 'y':
    # Get move from player
    direction = getDirection(thePlayer)

    # Move the player
    thePlayer = movePlayer(theBoard, theRooms, thePlayer, direction)
    # If the player is in a room ask them a riddle
    if thePlayer in theRooms:
        if incorrect < 5:
            print()
            correction = 0
            correction = tellRiddle()
            # If the riddle answer is correct let the player into the room
            if correction == 1:
                gold, life = checkCave(gold, life)
            # If the riddle answer is incorrect take life from the player
            else:
                print('You are disliked by the Riddler and he takes 3 life')
                incorrect = incorrect + 1
                life = life - 3
        # if the player has answered 4 riddles incorrect do not let the player
        # continue playing weather they want to or not
        else:
            print('You may want to continue but you have answered too many')
            print('riddles incorrect; therefor, you are not worthy to continue.')
            life = 0
    # Show the board
    printBoard(theBoard)

    # Show status
    statusLine(gold, life)
    # Determ if the player has life and wants to continue playing
    if life > 0:
        print('Are you brave enough to continue? yes y or no n')
        playAgain = input()
    # If the player has no health or does not want to continue they are dead
    else:
        print('You are dead.')
        break
