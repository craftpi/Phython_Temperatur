
#-----------------Klassendiagramm---------------#

+---------------------+
|     Thermometer     |
+---------------------+
| -standort: string   |
| -einheit: string    |
| -temperatur: float  |
+-----------------------------------------------+
| +__init__(self, standort: str, einheit: str)	|
| +setstandort(self, new_standort: str) -> None	|
| +getstandort(self) -> str						|
| +settemperatur(self, temp: float) -> None		|
| -convert_to_kelvin(self, temp: float) -> float|
| +gettempc(self) -> float						|
| +gettempf(self) -> float						|
+-----------------------------------------------+
