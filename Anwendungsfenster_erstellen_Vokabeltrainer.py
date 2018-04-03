# Erstellen eines Anwendungsfensters: Vokabeltrainer

from tkinter import *   # Alle Namen des Moduls tkinter werden importiert


fenster = Tk()          # Ein Objekt der Klasse Tk wird instanziiert

titel = Label(master = fenster,
              text = "Vokabeltrainer",
              font = ("Comic Sans MS", 14),
              fg = "blue",
              bg = "yellow") #1 Ein Objekt (Schriftfeld) der Klasse Label wird erzeugt, 

titel.pack()    # die Methode "pack()" beauftragt den Layoutmanager "Packer" das neue Objekt "titel" in das Anwendungsfenster "fenster" einzubauen


fenster.mainloop()      # Das Anwendungsfenster wird aktiviert

#1 und die Schriftart, Größe und Farbe wird formatiert
