import tkinter as tk
import json


# ---------------------------------------------------------- THERMOMETER ----------------------------------------------------------#

class Thermometer:
    def __init__(self, standort: str, einheit: str):
        self.standort = standort
        self.einheit = einheit
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
            # else:
            #   print("Falsche Einheit: muss 'C' oder 'F' sein.")
            #   raise ValueError("Falsche Einheit: muss 'C' oder 'F' sein.")
        except:
            print("Korigiere dein Termometer mit beachtung dieses Fehlers!")

    def convertToKelvin(self, temp: float) -> float:
        return temp + 273.15

    def getTempC(self) -> float:
        return self.temperatur - 273.15

    def getTempF(self) -> float:
        return self.temperatur * 9 / 5 - 459.67


def createTherm():
    therm = {
        'ort': entryS1.get(),
        'einheit': entryS2.get(),
        'temp': entryS3.get()
    }
    json.dump(therm, open('thermometer.json', 'w'))


def giveWerte():
    with open('thermometer.json', 'r') as file:
        obj = json.load(file)
        print(obj)


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


def on_entry_click(e, t):
    if e.get() == t:
        e.delete(0, "end")  # delete all the text in the entry
        e.config(fg='black')


def on_focusout(e, t):
    if e.get() == '':
        e.insert(0, t)
        e.config(fg='grey')


entryS1 = tk.Entry(root, justify="center", width=45)
entryS2 = tk.Entry(root, justify="center", width=45)
entryS3 = tk.Entry(root, justify="center", width=45)

entryS1.insert(0, S1text)
entryS1.config(fg='gray')
entryS2.insert(0, S2text)
entryS2.config(fg='gray')
entryS3.insert(0, S3text)
entryS3.config(fg='gray')

entryS1.bind('<FocusIn>', lambda event: on_entry_click(entryS1, S1text))
entryS1.bind('<FocusOut>', lambda event: on_focusout(entryS1, S1text))
entryS2.bind('<FocusIn>', lambda event: on_entry_click(entryS2, S2text))
entryS2.bind('<FocusOut>', lambda event: on_focusout(entryS2, S2text))
entryS3.bind('<FocusIn>', lambda event: on_entry_click(entryS3, S3text))
entryS3.bind('<FocusOut>', lambda event: on_focusout(entryS3, S3text))

entryS1.pack()
entryS2.pack()
entryS3.pack()
labelw.pack()

button2 = tk.Button(root, text="Ausfuehren", command=button_action2)
button2.pack()

button1 = tk.Button(root, text="Ausfuehren", command=button_action1)
button1.pack()

root.bind('<Return>', lambda event: button1.invoke())
root.bind('<Return>', lambda event: button2.invoke())

root.mainloop()
