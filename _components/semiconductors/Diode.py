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
    leakageCurrent = None           # A
    forwardVoltage = None           # V
    capacitance = None              # pF
    # thermal ratings
    maxJunctionTemp = None          # °C
    # technical
    manufacturers = None
    datasheet = None
    manufacturerNo = None

class Zener_Diode():
    # package
    name = "unknown"
    packages = []
    type = None
    # electrical ratings
    zenerVoltage = None             # V
    zenerImpedance = None           # Ω
    zenerCurrent = None             # A
    leakageCurrent = None           # μA
    maxCurrent = None               # A
    forwardVoltage = None        # V
    # thermal ratings
    maxJunctionTemp = None          # °C
    maxDissapationPower = None      # W
    # technical
    manufacturers = None
    datasheet = None
    manufacturerNo = None

class Schottky_Diode():
    # package
    name = "unknown"
    packages = []
    type = None
    # electrical ratings
    maxReverseVoltage = None        # V
    maxCurrent = None               # A
    maxInrushCurrent = None         # A
    maxReverseCurrent = None        # A
    leakageCurrent = None           # A
    forwardVoltage = None           # V
    capacitance = None              # pF
    recoveryTime = None             # nS
    # thermal ratings
    maxJunctionTemp = None          # °C
    # technical
    manufacturers = None
    datasheet = None
    manufacturerNo = None

class Bridge_Rectifier():
    # package
    name = "unknown"
    packages = []
    type = None
    shape = None
    # electrical ratings
    rectificationType = None        # half, full
    phaseNo = None                  # 1, 3
    maxReverseVoltage = None        # V
    maxCurrent = None               # A
    maxInrushCurrent = None         # A
    forwardVoltage = None           # V
    # thermal ratings
    maxJunctionTemp = None          # °C
    # technical
    manufacturers = None
    datasheet = None
    manufacturerNo = None

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