import random
print('--- Welcome To The Game ---')

top_of_range = input('Type a number: ')
print()
print('This number you entered was the limit of your guess.')
print()
guesses = 0
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next tima.')
        quit()
else:
    print('please type a number next time.')
    quit()

random_number = random.randint(0,top_of_range)

while True:
    guess_number = input('Make a guess: ')
    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print('please type a number next time.')
        continue
    if guess_number > random_number:
        print('Go lower')
        guesses +=1
    elif guess_number < random_number:
        print('Go higher')
        guesses +=1
    else:
        print('You got it! But you made "{}" mistakes.'.format(guesses))
        break
