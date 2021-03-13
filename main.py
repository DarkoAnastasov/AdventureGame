while True:
    answer = input('Are you ready to play? (yes/no)' )

    if answer.lower().strip() == 'yes':

        answer = input('You reach a crossroads, where would you like to go? left or right?').lower().strip()
        if answer == 'left':
            answer = input('You faced a monster. Would you like to attack or run?')

            if answer == 'attack':
                print('That was not the greatest idea. You lost!')
            else:
                print('Good choice! You made it away safely')

                answer = input('You see a car and a plane. Which would you like to take? (car/plane)')
                if answer == 'plane':
                    print('Unfortunately you do not know how to fly... Game Over')
                else:
                    print('Congrats YOU WON!')

        elif answer == 'right':
            print('Unfortunately you died. You were eaten by a lion')

        else:
            print('Invalid choice, you lost!')

    else:
        print("That's to bad!")
        break