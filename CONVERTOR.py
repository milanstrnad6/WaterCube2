#MODULE:CONVERTOR

def getDurationFrom(ml):
	switch = {
		5: 0.5,
		10: 1.0,
		15: 1.5,
		20: 2.0,
		25: 2.5,
		30: 3.0,
		35: 3.5,
		40: 4.0,
		45: 4.5,
		50: 5.0,
		55: 5.5,
		60: 6.0,
		65: 6.5,
		70: 7.0,
		75: 7.5,
		80: 8.0,
		85: 8.5,
		90: 9.0,
		95: 9.5,
		100: 10.0
	}
	return switch.get(ml, "Invalid ml")