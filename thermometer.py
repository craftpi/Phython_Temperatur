import string
import tkinter as tk
from tkinter import ttk
import json

# ---------------------------------------------------------- THERMOMETER ----------------------------------------------------------#

class Thermometer:
    def __init__(self):
        self.standort = None
        self.einheit = None
        self.temperatur = 0.0

    def setStandort(self, new_standort: str) -> None:
        self.standort = new_standort

    def getStandort(self) -> str:
        return self.standort

    def setEinheit(self, new_einheit: str) -> None:
        self.einheit = new_einheit

    def getEinheit(self) -> str:
        return self.einheit

    def tempSetzen(self, temp: float) -> None:
        try:
            if self.einheit == "C":
                if temp < -273.15:
                    print("Die Temperatur kann nicht kleiner als -273.15 Grad Celsius sein.")
                    raise ValueError("Die Temperatur kann nicht kleiner als -273.15 Grad Celsius sein.")
                self.temperatur = self.convertToKelvin(temp)
            elif self.einheit == "F":
                if temp < -459.67:
                    print("Die Temperatur kann nicht kleiner als -459.67 Fahrenheit sein.")
                    raise ValueError("Die Temperatur kann nicht kleiner als -459.67 Fahrenheit sein.")
                self.temperatur = self.convertToKelvin((temp - 32) * 5 / 9)
            else:
               print("Falsche Einheit: muss 'C' oder 'F' sein.")
               raise ValueError("Falsche Einheit: muss 'C' oder 'F' sein.")
        except:
            print("Korigiere dein Termometer mit beachtung dieses Fehlers!")

    def convertToKelvin(self, temp: float) -> float:
        return temp + 273.15

    def getTempC(self) -> float:
        return self.temperatur - 273.15

    def getTempF(self) -> float:
        return self.temperatur * 9 / 5 - 459.67

def Name() -> str:
    name = entryS1.get()
    return name

def createTherm() -> str:
    print(Name())
    name =Name()
    name = Thermometer()
   # '"' + entryS1.get() + '"', '"' + str(entryS2.get()) + '"'
    name.setStandort(entryS1.get())
    name.setEinheit(entryS2.get())
    name.tempSetzen(int(entryS3.get()))
   
    a=name.getTempC()
    b=name.getEinheit()
    c=name.getStandort()
    print(a)
    print(b)
    print(c)

def read(na):
    na=Thermometer()
    na.getEinheit()
    return na

   #therm = {
   #     'ort': entryS1.get(),
    #    'einheit': entryS2.get(),
     #   'temp': entryS3.get()
    #}
    #json.dump(therm, open('thermometer.json', 'w'))


def giveWerte():
    name=entryS4.get() 
   # c=Thermometer
    #f=.c.getEinheit()
    print(name)
    #print(f)
    print(read(name))
    
    


    
    #with open('thermometer.json', 'r') as file:
     #   obj = json.load(file)
      #  print(obj)


# -------------------------------------------------------------- GUI --------------------------------------------------------------#

def button_action1():
    createTherm()


def button_action2():
    giveWerte()


root = tk.Tk()
root.title("Ort Thermometer")

label = tk.Label(root, text="Gib die Temperaturen ein")
labelw = tk.Label(root, text="")
label.pack()

S1text = "Welchen Ort moechtest du speichern"
S2text = "In welcher Einheit moechtest du du die Temperatur speichern"
S3text = "Wie hoch ist die Temperatur"
S4text = "Welches Thermometer moechtest du suchen"


def on_entry_click(e, t):
    if e.get() == t:
        e.delete(0, "end")  # delete all the text in the entry
        e.config(fg='black')


def on_focusout(e, t):
    if e.get() == '':
        e.insert(0, t)
        e.config(fg='grey')

global entryS1
entryS1 = tk.Entry(root, justify="center", width=45)
global entryS2
entryS2 = tk.Entry(root, justify="center", width=45)
global entryS3
entryS3 = tk.Entry(root, justify="center", width=45)
entryS4 = tk.Entry(root, justify="center", width=45)

entryS1.insert(0, S1text)
entryS1.config(fg='gray')
entryS2.insert(0, S2text)
entryS2.config(fg='gray')
entryS3.insert(0, S3text)
entryS3.config(fg='gray')
entryS4.insert(0, S4text)
entryS4.config(fg='gray')

entryS1.bind('<FocusIn>', lambda event: on_entry_click(entryS1, S1text))
entryS1.bind('<FocusOut>', lambda event: on_focusout(entryS1, S1text))
entryS2.bind('<FocusIn>', lambda event: on_entry_click(entryS2, S2text))
entryS2.bind('<FocusOut>', lambda event: on_focusout(entryS2, S2text))
entryS3.bind('<FocusIn>', lambda event: on_entry_click(entryS3, S3text))
entryS3.bind('<FocusOut>', lambda event: on_focusout(entryS3, S3text))
entryS4.bind('<FocusIn>', lambda event: on_entry_click(entryS4, S4text))
entryS4.bind('<FocusOut>', lambda event: on_focusout(entryS4, S4text))

entryS1.pack()
entryS2.pack()
entryS3.pack()
labelw.pack()

button2 = tk.Button(root, text="Suchen", command=button_action2)

button1 = tk.Button(root, text="Erstellen", command=button_action1)

button1.pack()
entryS4.pack()
button2.pack()

root.bind('<Return>', lambda event: button1.invoke())
root.bind('<Return>', lambda event: button2.invoke())

root.mainloop()
