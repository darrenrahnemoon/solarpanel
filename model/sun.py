from dataclasses import dataclass, field

@dataclass
class Sun:
	position: dict[str, float] = field(
		default_factory = lambda: {
			"x" : 0,
			"y" : 0,
			"z" : 0,
		}
	)