from IPython.display import clear_output


def display_board(board):
    """Prints the game board """
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

    
def display_sample_board(player):
    '''Display the game board with index values for reference'''
    print('7|8|9')
    print('4|5|6')
    print('1|2|3')
    print('\n')
    print(f'{player}, choose your marker position')
    print('\n')
   
    
def player_name():
    '''Takes in input from the user for their names'''
    name1 = ''
    name2 = ''
    name1 = input('Who is the first person playing today? ')
    name2 = input('Who us the second person playing today? ')
    return (name1,name2)

def player_marker(player1_name):
    '''assigns wither X or O to the players as their markers'''
    
    marker = ''
    #Take valid marker inputs.. either X or O.. else keep asking till valid input is provided
    while not (marker == 'X' or marker == 'O'):
        marker = input(f'Please choose either X or O for {player1_name} :').upper()
        
    
    #Assign marker to player 1 and player 2 based on the user choice
    if marker == 'X':
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'
        
    return (player1,player2)

def user_input(plyr_ky):
    '''Takes in valid user input for the game'''
    
    usr_in = int(input())
    #Check if the input is a valid value, else ask again
    if usr_in not in range(1,10):
        clear_output()
        display_board(tic_tac_toe)
        print('please provide a valid position')
        user_input(plyr_ky)
    #Check if the input position is available, then update the marker.     
    elif tic_tac_toe[usr_in] == ' ':
        tic_tac_toe[usr_in] = plyr_ky
    #Check if the position is already taken, then ask again for input    
    else:
        clear_output()
        display_board(tic_tac_toe)
        print(f'Position {usr_in} is already taken.. please provide a valid position')
        user_input(plyr_ky)
      
            
def play_game():

    '''Main function which initializes the game and calls all other dependent functions'''
    
    global tic_tac_toe
    
    tic_tac_toe = [' ']*11
    
    clear_output()
    #get player names
    player1_name, player2_name = player_name()

    clear_output()
    #get player markers
    player1_key, player2_key = player_marker(player1_name)

    clear_output()
    
    print(f' Welcome! {player1_name}, you have chosen marker {player1_key} and {player2_name}, you have chosen marker {player2_key}.. All the best!')
    input("Press 'Enter' key to begin")
    display_sample_board(player1_name)

    #start game
    for i in range(1,10):
        clear_output()
        #alternate between the two players for their respective turns
        if i%2 == 0:
            cur_player_name = player2_name
            cur_player_key = player2_key
        else:
            cur_player_name = player1_name
            cur_player_key = player1_key

        display_sample_board(cur_player_name)
        display_board(tic_tac_toe)
        #get position from user for the marker
        user_input(cur_player_key)

        # check if any of the winning conditions are met for the current player-- rows, columns or diagonals
        if tic_tac_toe[1:4] == [cur_player_key]*3 or tic_tac_toe[4:7] == [cur_player_key]*3 or tic_tac_toe[7:10] == [cur_player_key]*3 or tic_tac_toe[1:8:3] == [cur_player_key]*3 or tic_tac_toe[2:9:3] == [cur_player_key]*3 or tic_tac_toe[3:10:3] == [cur_player_key]*3 or tic_tac_toe[1:10:4] == [cur_player_key]*3 or tic_tac_toe[3:8:2] == [cur_player_key]*3:
            clear_output()
            display_board(tic_tac_toe)
            print('\n')
            print(f'******* Congratulations! {cur_player_name} wins! *******')
            break

    else:
        #if no winning conditions are met, then its a draw
        clear_output()
        display_board(tic_tac_toe)
        print("Game Over. It's a Draw.. ")
        print('\n')
        
    play_again = input(" Enter 'Y' to play again :").upper()
    if str(play_again) == 'Y':
        play_game()

            
            
#execute the game here

play_game()