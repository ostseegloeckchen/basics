# Modellieren eine Warteschlange

class Queue(object):
    def __init__(self):
        self.__content = []

    def empty(self):                # testen, ob die Schlange leer ist
        return self.__content == []

    def enqueue(self, item):        # Ein Objekt hinten an die Schlange hängen
        self.__content += [item]

    def dequeue(self):              # Ein Objekt vorne von der Schlange entfernen
        if not self.empty():
            item = self.__content[0]
            del self.__content[0]
            return item

    def front(self):                # Das vorderste Element der Schlange lesen
        if not self.empty():
            return self.__content[0]
