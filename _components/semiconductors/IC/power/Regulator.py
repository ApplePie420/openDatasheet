from _components.semiconductors._commonInfo import commonInfo

class Regulator(commonInfo):
    # electrical ratings
    maxOutputVoltage = None         # V
    maxOutputCurrent = None         # A
    refVoltage = None               # V
    minLoadCurrent = None           # A
    currentLimit = None             # A
    RMSnoise = None                 # %V_o
    rippleRejection = None          # dB

    @staticmethod
    def efficiency(Pout, Pin):
        return Pout/Pin
