from _components.semiconductors._commonInfo import commonInfo

class Comparator(commonInfo):
    # Comparator specific characteristics
    inputCurrent = None                 # nA
    offsetCurrent = None                # nA
    inputOffsetVoltage = None           # mV
    voltageGain = None                  # V/mV
    saturationVOltage = None            # V
    responseTime = None                 # ns