from random import randint

name = raw_input("Hey there, what's your name? ")
random_number = randint(1, 100)
print "We're thinking of a number between 1 and 100. Try and guess it."
tries = 0
still_guessing = True

while still_guessing:
    guess = raw_input("Your guess? ")
    tries += 1
    for i in guess:
        if ord(i) < 48 or ord(i) > 57:
            guess = raw_input("Guess a NUMBER, silly! ")
    guess = int(guess)
    if guess < random_number:
        print "Your number is too low. Guess again!"
    elif guess > random_number:
        print "Your guess is too high. Guess again!"
    else:
        print "You guessed it with %d tries" % tries
        still_guessing = False
