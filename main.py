import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?\n")
        txtIn = input()
        t.handleAdd(txtIn)
        print("Aggiunta!")
        continue

    if int(txtIn) == 2:
        print("Ok, quale parola devo tradurre?")
        txtIn = input()
        print(f"Traduzione: {str(t.handleTranslate(txtIn))}")
        continue
    if int(txtIn) == 3:
        print("Ok, quale parola devo cercare?")
        txtIn = input()
        print(f"Traduzione: {str(t.handleWildCard(txtIn))}")

        continue
    if int(txtIn) == 4:
        break