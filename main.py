print('Welcome To Game...')
player1 = 0
player2 = 0
while True:
    question = input('Do You Want To Play ?')
    if question == 'yes' or question == 'y':
        choice1 = input('Please Choose One👤! Rock,Paper Or Scissors :')
        choice2 = input('Please Choose One👥! Rock,Paper Or Scissors :')
        if choice1 == choice2:
            print('Equal')
        elif choice1 == 'rock' and choice2 == 'paper':
            print('Player 2 Won! 🥳')
            player2 += 1
            print(f"Player 👤 :{player1} - Player 👥 :{player2}")
        elif choice1 == 'rock' and choice2 == 'scissors':
            print('Player 1 Won! 🥳')
            player1 += 1
            print(f"Player 👤 :{player1} - Player 👥 :{player2}")
        elif choice1 == 'scissors' and choice2 == 'paper':
            print('Player 1 Won! 🥳')
            player1 += 1
            print(f"Player 👤 :{player1} - Player 👥 :{player2}")
        elif choice1 == 'paper' and choice2 == 'scissors':
            print('Player 2 Won! 🥳')
            player2 += 1
            print(f"Player 👤 :{player1} - Player 👥 :{player2}")
        elif choice1 == 'scissors' and choice2 == 'rock':
            print('Player 2 Won! 🥳')
            player2 += 1
            print(f"Player 👤 :{player1} - Player 👥 :{player2}")
        elif choice1 == 'paper' and choice2 == 'rock':
            print('Player 1 Won! 🥳')
            player1 += 1
            print(f"Player 👤 :{player1} - Player 👥 :{player2}")
        else:
            print('Invalid Choice! 🥲')
    elif player1 == 3:
        print('Player 1 Winner!😍')
        break
    elif player2 == 3:
        print('Player 2 Winner! 😍')
        break
    else:
        print('The Winner Needs 3 Points😊')
        break
