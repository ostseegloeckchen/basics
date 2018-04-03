# Skript für ein Spiel

from tkinter import *
from threading import *
from time import *
from random import *

class Weltraum:
    def __init__(self):
        self.fenster =Tk()      # Erzeugt ein neues Ausgabefenster mit dem Namen "fenster"
        self.canvas = Canvas(self.fenster, width = 350,
                             height = 250, bg = "black")    #1 Erzeugt eine Leinwand mit schwarzem Hintergrund
        self.canvas.pack()

        self.addSteine()        #2 
        self.addAsteroid()

        self.schiff = Schiff("Meteore/schiff.gif",
                             self, 50, 150) #3

        self.fenster.bind(sequence = "<Any-KeyPress>",
                          func = self.schiff.steuere)   #4

        self.schiff.start()     #5
        self.fenster.mainloop

    def addAsteroid(self):
        self.astx, self.asty = 300, 100     #6
        self.astbild = PhotoImage(file = "Meteore/metgross.gif")
        self.asteroid = self.canvas.create_image(
            self.astx, self.asty, image = self.astbild) #7

    def addSteine(self):
        self.steinbild = PhotoImage(file = "Meteore/metklein.gif")
        self.steine = []
        for i in range(7):
            id = self.canvas.create_image(
                randint(100, 220), randint(-10, 270),
                image = self.steinbild)
            self.steine.append(id)

    def kollision(self, schiff):
        x, y = schiff.x, schiff.y
        for id in self.steine:
            if id in self.canvas.find_overlapping(x-20, y-5, x+0, y+5):
                return True
        return False

    def gelandet(self):
        return(self.astx - 10 < self.schiff.x < self.astx + 10) and \
                         (self.asty - 10 < self.schiff.y < self.asty + 10) and \
                         (-2 <= self.schiff.vx < 2) and \
                         (-2 <= self.schiff.vy < 2)

class Schiff(Thread):
    def __init__(self, bilddatei, weltraum, x, y):
        Thread.__init__(self)   # Was bedeutet diese Zeile???
        self.c = weltraum.canvas
        self.w = weltraum
        self.x, self.y = x, y
        self.vx = self.vy = 0
        self.bild = PhotoImage(file = bilddatei)
        self.id = self.c.create_image(x, y, image = self.bild)

    def run(self):
        while not self.w.kollision(self):
            sleep(0.1)
            self.x += self.vx
            self.y += self.vy
            self.c.move(self.id, self.vx, self.vy)
            if self.w.gelandet():
                self.c.create_text(100, 50,
                                   text = "Gewonnen!",
                                   font = ("Times New Roman", 20), fill = "white")
                break
            else:
                self.c.create_text(100, 50,
                                   text = "Schade, verloren!",
                                   font = ("Times New Roman", 20), fill = "white")

    def steuere(self, event):
        if event.keysym_num == 65362: self.vy -= 0.5
        elif event.keysym_num == 65364: self.vy += 0.5
        elif event.keysym_num == 65363: self.vx += 0.5
        elif event.keysym_num == 65361: self.vx -= 0.5

w = Weltraum()
