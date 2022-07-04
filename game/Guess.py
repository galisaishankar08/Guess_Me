import random


class Guess:
    def __init__(self, guess):
        self.guess = guess

    def expert(self):
        number = random.randint(1, 100)
        number_of_guesses = 0
        while number_of_guesses < 3:
            number_of_guesses += 1
            if guess < number:
                print('low')
            if guess > number:
                print('high')
            if guess == number:
                break

        if guess == number:
            return True
        else:
            return number


guess = int(input())
obj = Guess(guess)
x = obj.expert()
print(x)
