# teams = ["Barcelona", "Arsenal", "4030", "Liverpool"]
# print(teams)
# print(type(teams))

# cars = list(("RR", "Audi", "Aston Martin", "Ford"))
# print(cars)
# print(type(cars))

# teams[2] = "Bayern"
# print(teams)

# name = 'Ali'
# name[0] = "B" #ERROR Because Strings Imutable

# teams2 = teams + ['Man United']
# print(teams2)
#
# teams3 = teams * 3
# print(teams3)
#
# teams4 = teams.copy()
# print(teams)
# print(teams4)
#
# names = ["Payman", "Mahgol", "Mehdi", ["Pouya", "Saeed", ["Nelli", "Sahel", "Kimia"]]]
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
# print(names[4][0])
# print(names[4][2][0])

# names = ["Payman", "Mahgol", "Mehdi"]
# names = names + ["Sahel"]
# print(names)
# names.append("Sahel")
# print(names)
# names.insert(2, "Neli")
# print(names)
# print(names.index("Mehdi"))
# names.pop()
# print(names)
# names.pop(0)
# print(names)
# names.sort(reverse=True)
# print(names)
# names.reverse()
# print(names)
# names.remove("Mehdi")
# print(names)
# names.clear()
# print(names)
# del names
# print(names)

# i = 0
# while i < 5:
#     print("Python")
#     i += 1

# i = 0
# while i <= 5:
#     print(i)
#     i += 1

# i = 0
# while i <= 5:
#     i += 1
#     print(i)

# i = 0
# while i < 1000:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# i = 0
# while i < 1000:
#     if i % 2 == 0 and i % 3 == 0:
#         print(i)
#     i += 1

# question = 'yes'
# while question == 'yes':
#     print('ok')
#     question = input("yes / no : ")


# names = ["Payman", "Mahgol", "Sahel", "Neli", "Mehdi"]
# # print(names[0])
# # print(names[1])
# # print(names[2])
# # print(names[3])
# # print(names[4])
# i = 0
# while i < len(names):
#     print(names[i])
#     i += 1


# names = ["Payman", "Mahgol", "Sahel", "Neli", "Mehdi"]
# names2 = ["Payman", "Mahgol", "Pouya", "Saeed", "Sahel"]
# names3 = []
#
# i = 0
# while i < len(names):
#     j = 0
#     while j < len(names2):
#         if names[i] == names2[j]:
#             names3.append(names[i])
#         j += 1
#     i += 1
# print(names3)

# question = input("Would You Like To Check Your Number? :")
# while question.lower() == 'yes' or question.lower() == 'y':
#     number = int(input("Enter Number :"))
#     if number % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
#     question = input("Would You Like To Check Your Number? :")
# else:
#     print("OK,Bye")

# users = [["jack", 0], ["Peter", 1], ["Sarah", 1], ["Jessica", 0], ["Lincoln", 1]]
# passed = 0
# failed = 0
#
# passed_users = []
# failed_user = []
# i = 0
# while i < len(users):
#     if users[i][1] == 1:
#         passed += 1
#         passed_users.append(users[i][0])
#     else:
#         failed += 1
#         failed_user.append(users[i][0])
#     i += 1
# print(f"Passed : {passed} {passed_users}")
# print(f"Failed : {failed} {failed_user}")

# db = []
# question = input("Do You Want To Add User ? :")
# while question.lower() == 'yes' or question.lower() == 'y':
#     username = input("Enter Username : ")
#     major = input("Enter Major : ")
#     grade = input("Enter Grade : ")
#     info = [username, major, grade]
#     db.append(info)
#     question = input("Do You Want To Add User ? :")
# else:
#     print("Ok Sir, See You Later. ")
#     print(db)

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
