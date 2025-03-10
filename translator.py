import json

from dictionary import Dictionary


class Translator:

    def __init__(self, dict = Dictionary()):
        self._dict = dict
        pass

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit

        print(f"\t{1}. Aggiungi nuova parola")
        print(f"\t{2}. Cerca una traduzione")
        print(f"\t{3}. Cerca con wildcard")
        print(f"\t{4}. Exit")



    def loadDictionary(self, dict):
        self._dict.loadDictionary()

        # dict is a string with the filename of the dictionary



    def handleAdd(self, txtEntry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        entry = txtEntry.split(" ")
        print(entry)

        self._dict.addWord(entry)
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        return self._dict.translate(query)


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        return self._dict.translateWordWildCard(query)

    def printAll(self):
        self._dict.printAll()