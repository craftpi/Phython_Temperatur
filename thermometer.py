class Thermometer:
    def __init__(self, standort: str, einheit: str):
        self.standort = standort
        self.einheit = einheit
        self.temperature = 0.0
    
    def setstandort(self, new_standort: str) -> None:
        self.standort = new_standort
    
    def getstandort(self) -> str:
        return self.standort

    def seteinheit(self, new_einheit: str) -> None:
        self.einheit = new_einheit

    def geteinheit(self) -> str:
        return self.einheit
    
    def tempsetzen(self, temp: float) -> None:
        try:   
            if self.einheit == "C":
                if temp < -273.15:
                    print("Die Temperatur kann nicht kleiner als -273.15 Grad Celsius sein.")
                    raise ValueError("Die Temperatur kann nicht kleiner als -273.15 Grad Celsius sein.")
                self.temperatur = self.convert_to_kelvin(temp)
            elif self.einheit == "F":
                if temp < -459.67:
                    print("Die Temperatur kann nicht kleiner als -459.67 Fahrenheit sein.")
                    raise ValueError("Die Temperatur kann nicht kleiner als -459.67 Fahrenheit sein.")
                self.temperatur = self.convert_to_kelvin((temp - 32) * 5/9)
            else:
                print("Falsche Einheit: muss 'C' oder 'F' sein.")
                raise ValueError("Falsche Einheit: muss 'C' oder 'F' sein.")
        except:
            print("Korigiere dein Termometer mit beachtung dieses Fehlers!")
    
    def convert_to_kelvin(self, temp: float) -> float:
        return temp + 273.15
    
    def gettempc(self) -> float:
        return self.temperatur - 273.15
    
    def gettempf(self) -> float:
        return self.temperatur * 9/5 - 459.67

