from dataclasses import dataclass, field
from .solar_panel import SolarPanel

@dataclass
class SolarPanelFrame:
	solar_panel: SolarPanel = field(default_factory=SolarPanel)
	angle: float = 0