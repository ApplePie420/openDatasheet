from _components.semiconductors._commonInfo import commonInfo

class Diode(commonInfo):
    # electrical ratings
    maxReverseVoltage = None        # V
    maxRMSVoltage = None            # V
    maxCurrent = None               # A
    maxReverseCurrent = None        # A
    leakageCurrent = None           # A
    forwardVoltage = None           # V
    capacitance = None              # pF

class Zener_Diode(commonInfo):
    # electrical ratings
    zenerVoltage = None             # V
    zenerImpedance = None           # Ω
    zenerCurrent = None             # A
    leakageCurrent = None           # μA
    maxCurrent = None               # A
    forwardVoltage = None        # V

class Schottky_Diode(commonInfo):
    # electrical ratings
    maxReverseVoltage = None        # V
    maxCurrent = None               # A
    maxInrushCurrent = None         # A
    maxReverseCurrent = None        # A
    leakageCurrent = None           # A
    forwardVoltage = None           # V
    capacitance = None              # pF
    recoveryTime = None             # nS

class Bridge_Rectifier(commonInfo):
    # electrical ratings
    rectificationType = None        # half, full
    phaseNo = None                  # 1, 3
    maxReverseVoltage = None        # V
    maxCurrent = None               # A
    maxInrushCurrent = None         # A
    forwardVoltage = None           # V

class LED(commonInfo):
    # electrical ratings
    forwardCurrent = None           # mA
    reverseVoltage = None           # V
    luminousIntensity = None        # lm
    viewingAngle = None             # ° degrees
    dominantWavelength = None       # nm