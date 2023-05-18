
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiouy":
            if letter.isupper():
                translation += "G"
            else:
                translation += "g"
        else:
            translation += letter
    return translation


text = input("Enter a phrase to translate: ")
print(translate(text))
