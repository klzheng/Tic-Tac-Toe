#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='https://www.udemy.com/user/joseportilla/'><img src='../Pierian_Data_Logo.png'/></a>
# ___
# <center><em>Content Copyright by Pierian Data</em></center>

# # Milestone Project 1: Walkthrough Steps Workbook
# 
# Below is a set of steps for you to follow to try to create the Tic Tac Toe Milestone Project game!

# #### Some suggested tools before you get started:
# To take input from a user:
# 
#     player1 = input("Please pick a marker 'X' or 'O'")
#     
# Note that input() takes in a string. If you need an integer value, use
# 
#     position = int(input('Please enter a number'))
#     
# <br>To clear the screen between moves:
# 
#     from IPython.display import clear_output
#     clear_output()
#     
# Note that clear_output() will only work in jupyter. To clear the screen in other IDEs, consider:
# 
#     print('\n'*100)
#     
# This scrolls the previous board up out of view. Now on to the program!

# **Step 1: Write a function that can print out a board. Set up your board as a list, where each index 1-9 corresponds with a number on a number pad, so you get a 3 by 3 board representation.**

# In[1]:


from IPython.display import clear_output

def display_board():
    
    print(board[0]+'|'+board[1]+'|'+board[2])
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(board[6]+'|'+board[7]+'|'+board[8])


# **TEST Step 1:** run your function on a test version of the board list, and make adjustments as necessary

# In[2]:


test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# **Step 2: Write a function that can take in a player input and assign their marker as 'X' or 'O'. Think about using *while* loops to continually ask until you get a correct answer.**

# In[39]:


import random
        
def player_input():
    global marker
    first = random.randint(1,2)
    if first == 1:
        print('Player 1 goes first')
        player = input('Player ' + str(first) + ', please choose X or O: ')
        while player != 'X' and player != 'O':
            player = input('Player ' + str(first) + ', please choose X or O: ')
        if player == 'X':
            marker = player
            print('Player 1 is X, Player 2 is O')
        elif player == 'O':
            marker = player
            print('Player 1 is O, Player 2 is X')
    elif first == 2:
        print('Player 2 goes first')
        player = input('Player ' + str(first) + ', please choose X or O: ')
        while player != 'X' and player != 'O':
            player = input('Player ' + str(first) + ', please choose X or O: ')
        if player == 'X':
            marker = player
            print('Player 2 is X, Player 1 is O')
        elif player == 'O':
            marker = player
            print('Player 2 is O, Player 1 is X')
        
""""    else:
        first == 2
        print('Player 2 goes first')

    player = input('Player ' + str(first) + ', please choose X or O: ')
    while player != 'X' and player !='O':
        player = input('Please choose a valid input: ')
    if player == 'X':
        marker = player
        print('Player 1 is' + player + ', Player 2 is O') #why is this line not printing
    elif player == 'O':
        marker = player
        print('Player 1 is O, Player 2 is X') # why is this line not printing
    elif player 
"""


# **TEST Step 2:** run the function to make sure it returns the desired output

# In[4]:


player_input()


# **Step 3: Write a function that takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board.**

# In[3]:


def place_marker(board):
    global marker
    position = input('What position would you like to place your marker (1-9): ')
    board[int(position)-1] = marker


# **TEST Step 3:** run the place marker function using test parameters and display the modified board

# In[ ]:


place_marker(test_board,'$',8)
display_board(test_board)


# **Step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won. **

# In[15]:


def win_check(board):
    global marker
    if marker==board[0]==board[1]==board[2] or marker==board[0]==board[3]==board[6] or marker==board[0]==board[4]==board[8] or marker==board[1]==board[4]==board[7] or marker==board[2]==board[5]==board[8] or marker==board[3]==board[4]==board[5] or marker==board[6]==board[7]==board[8] or marker==board[2]==board[4]==board[6]:
        return True
    else:
        return False


# **TEST Step 4:** run the win_check function against our test_board - it should return True

# In[ ]:


win_check(test_board,'X')


# **Step 5: Write a function that uses the random module to randomly decide which player goes first. You may want to lookup random.randint() Return a string of which player went first.**

# In[5]:


import random

def choose_first():
    first = random.randint(1,2)
    if first == 1:
        print('Player 1 goes first')
    else:
        first == 2
        print('Player 2 goes first')
    


# **Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.**

# In[6]:


def space_check(board, position):
    if board[int(position)-1] == ' ':
        return True
    else:
        return False


# **Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.**

# In[7]:


def full_board_check(board):
    if ' ' not in board:
        return True
    else:
        return False


# **Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.**

# In[8]:


def player_choice(board):
    global marker
    position = input('Please input your next position: ')

    if int(position) in range(1,9):
        if space_check(board,position) == True:
            board[int(position)-1] = marker
            display_board()
        elif space_check(board,position) == False:
            position = input('That position is not free, please input another position: ')
    else: # position not in range(1,9):
        position = input('Please re-enter a valid position: ')


# **Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.**

# In[9]:


def replay():
    if input('Do you want to play again? Y or N: ') == 'Y':
        return True


# **Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!**

# In[51]:


print('Welcome to Tic Tac Toe!')
marker = '0'
player_input() 

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
display_board()

place_marker(board)
display_board()

def game_run():
    global board
    global marker
    while win_check(board) == False:
        if marker == 'X':
            marker = 'O'
            position = input('Please input your next position: ')

            if int(position) in range(1,10):
                if space_check(board,position) == True:
                    board[int(position)-1] = marker
                    display_board()
                elif space_check(board,position) == False:
                    position = input('That position is not free, please input another position: ')
            else: # position not in range(1,9):
                position = input('Please re-enter a valid position: ')

        elif marker == 'O':
            marker = 'X'
            position = input('Please input your next position: ')

            if int(position) in range(1,10):
                if space_check(board,position) == True:
                    board[int(position)-1] = marker
                    display_board()
                elif space_check(board,position) == False:
                    position = input('That position is not free, please input another position: ')
            else: # position not in range(1,9):
                position = input('Please re-enter a valid position: ')

        elif full_board_check(board) == True:
            tie = input('Tie! Do you want to play again? Y or N')

            if tie == 'Y':
                clear_output()
                player_input() 

            elif tie == 'N':
                break


    if win_check(board) == True:
        print(marker + ' has won the game!')
        again = input('Do you want to play again? Y or N: ')
        if again == 'Y':
            clear_output()
            print('Welcome to Tic Tac Toe!')
            marker = '0'
            player_input() 

            board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            display_board()

            place_marker(board)
            display_board()
            
            game_run()
        elif again == 'N':
            clear_output()
            board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            print('Okay, no worries')
        else:
            again = input('Please enter Y or N: ')

    if full_board_check(board) == True:
        tie = input('Tie! Do you want to play again? Y or N: ')
        if tie == 'Y':
            clear_output()
            print('Welcome to Tic Tac Toe!')
            marker = '0'
            player_input() 

            board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            display_board()

            place_marker(board)
            display_board()
        elif tie == 'N':
            print('Okay')
        else: 
            tie = input('Please type Y or N: ')
game_run()


# ## Good Job!

# In[ ]:





# In[ ]:





# In[ ]:




