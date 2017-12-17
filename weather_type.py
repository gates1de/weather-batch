from enum import Enum

class WeatherType(Enum):
    CLEAR  = "Clear"
    CLOUDS = "Clouds"
    RAIN   = "Rain"
    SNOW   = "Snow"

    def japanese_name(self):
        if self == WeatherType.CLEAR:
            return "晴れ"
        elif self == WeatherType.CLOUDS:
            return "くもり"
        elif self == WeatherType.RAIN:
            return "雨"
        elif self == WeatherType.SNOW:
            return "雪"
        else:
            return ""
