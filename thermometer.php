+---------------------+
|     Thermometer     |
+---------------------+
| -location: string    |
| -unit: string        |
| -temperature: float  |
+---------------------+
| +__init__(self, location: str, unit: str)|
| +set_location(self, new_location: str) -> None|
| +get_location(self) -> str|
| +set_temp(self, temp: float) -> None|
| -convert_to_kelvin(self, temp: float) -> float|
| +get_temp_c(self) -> float|
| +get_temp_f(self) -> float|
+---------------------+