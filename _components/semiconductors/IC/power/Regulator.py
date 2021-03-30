class Regulator():
    # package
    name = "unknown"
    packages = []
    type = None
    # electrical ratings
    maxInputVoltage = None          # V
    maxOutputVoltage = None         # V
    maxOutputCurrent = None         # A
    refVoltage = None               # V
    minLoadCurrent = None           # A
    currentLimit = None             # bool
    RMSnoise = None                 # %V_o
    rippleRejection = None          # dB
    # thermal ratings
    maxJunctionTemp = None          # °C
    # technical
    manufacturers = None
    datasheet = None
    manufacturerNo = None

    @staticmethod
    def efficiency(Pout, Pin):
        return Pout/Pin
