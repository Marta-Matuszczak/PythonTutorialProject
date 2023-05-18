
secret_word = "giraffe"
guess = ""
guess_count = 0
limit = 3
out_of_guesses = False

while guess != secret_word:
    if guess_count < limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
        break

if not out_of_guesses:
    print("You win!")
else:
    print("You lose!")
