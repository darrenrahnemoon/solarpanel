from dataclasses import dataclass, field
from .light_sensor import LightSensor

@dataclass
class SolarPanel:
	angle: float = 0
	light_sensors: dict[str, LightSensor] = field(
		default_factory = lambda: {
			"top" : LightSensor(),
			"right" : LightSensor(),
			"bottom" : LightSensor(),
			"left" : LightSensor(),
		}
	)