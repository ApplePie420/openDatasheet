class Diode():
    # package
    name = "unknown"
    packages = []
    type = None
    # electrical ratings
    maxReverseVoltage = None        # V
    maxRMSVoltage = None            # V
    maxCurrent = None               # A
    maxReverseCurrent = None        # A
    forwardVoltage = None           # V
    capacitance = None              # pF
    # thermal ratings
    maxJunctionTemp = None          # °C
    # technical
    manufacturers = None
    datasheet = None
    manufacturerNo = None

class Zener_Diode():
    None

class Schottky_Diode():
    None

class Bridge_Rectifier():
    None

class LED():
    # package
    name = "unknown"
    packages = []
    type = None
    # electrical ratings
    forwardCurrent = None           # mA
    reverseVoltage = None           # V
    luminousIntensity = None        # lm
    viewingAngle = None             # ° degrees
    dominantWavelength = None       # nm
    # thermal ratings
    maxJunctionTemp = None          # °C
    # technical
    manufacturers = None
    datasheet = None
    manufacturerNo = None