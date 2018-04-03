# Erstellen eines Anwendungsfensters: Begrüßung


def gruessen():
    fenster.label.config(text = "Hallo!")   #Veranlasst den Begrüßungstext des label in "Hallo!" zu ändern
    


from tkinter import *   # Alle Namen des Moduls tkinter werden importiert


fenster = Tk()          # Ein Objekt der Klasse Tk wird instanziiert

fenster.label = Label(master = fenster,
                      text = "Begrüßung") #1 Ein Objekt (Schriftfeld) der Klasse Label wird erzeugt, 
fenster.label.pack()    # die Methode "pack()" beauftragt den Layoutmanager "Packer" das neue Objekt "label" in das Anwendungsfenster "fenster" einzubauen

fenster.button = Button(master = fenster,
                        text = "Sage Hallo",
                        command = gruessen) # Ein Objekt (beschriftete Schaltfläche) der Klasse Button wird erzeugt
fenster.button.pack()

fenster.mainloop()      # Das Anwendungsfenster wird aktiviert

#1 Achtung: es gibt ein neues Label-Objekt namens label!!
