import random

# Write your code here
print("H A N G M A N")

tuple_word = ('python', 'java', 'kotlin', 'javascript')

word = random.choice(tuple_word)

hidden_word = ["-" for x in range(len(word))]
tries = 8

set_hidden_word = set(word)
tries_letter = set()

hidden_word_str = ""

letter_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')


ans = input('Type "play" to play the game, "exit" to quit: ')

if ans == "play":

    while tries != 0 and hidden_word_str != word:
        # espacement
        print("")
        # boucle d'affichage du mot caché
        for i in range(len(hidden_word)):
            print(hidden_word[i], end='')

        letter = input("\nInput a letter: ")

        if letter in letter_tuple:
            # si la la lettre est dans le set du mot caché puis on l'enleve si oui
            if letter in set_hidden_word:

                set_hidden_word.remove(letter)

                # remplace le - par la lettre selon le placement dans word
                for i in range(len(word)):
                    if word[i] == letter:
                        hidden_word[i] = letter

            elif letter in tries_letter:
                print("You already typed this letter")

            else:
                print("No such letter in the word")
                tries -= 1
        elif len(letter) >= 2:
            print("You should print a single letter")
        else:
            print("It is not an ASCII lowercase letter")

        tries_letter.add(letter)
        hidden_word_str = ""
        for ele in hidden_word:
            hidden_word_str += ele

    else:
        if word == hidden_word_str:
            print("""You guessed the word!
            You survived!""")
        else:
            print("You are hanged!")


else:
    exit()

