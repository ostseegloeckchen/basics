# Erstellen einer Klasse "Stack", welche von Außen nicht zugänglich ist

class Stack:
    def __init__(self):         #1
        self.__content = []

    def push(self, item):       #2
        self.__content = [item] + self.__content

    def top(self):              # wenn Liste nicht leer ist, wird ihr Inhalt wiedergegeben
        if not self.empty():
            return self.__content[0]

    def pop(self):              #3
        if not self.empty():
            item = self.__content[0]
            del self.__content[0]
            return item

    def empty(self):
        return self.__content == [] # True wenn Stapel leer ist, ansonsten False



# Hauptprogramm

if __name__ == "__main__":
    wort = input("Wort: ")
    stapel = Stack()
    for zeichen in wort:
        stapel.push(zeichen)
    if not stapel.empty():
        print(stapel.top(), end = "")


#1 Bei der Initialisierung wird eine leere Liste angelegt,
#1 in welche die Elemente des Stapels abgelegt werden

#2 Anhängen eines neuen Elementes vorne an die Liste
#2 Die Liste mit dem einzigen Element "item" und
#2 die bestehende Liste "self.__content werden konkateniert

#3 Eine Kopie des 1. Elementes wird zurückgegeben und
#3 das 1. Element (oberstes) vom Stapel entfernt
