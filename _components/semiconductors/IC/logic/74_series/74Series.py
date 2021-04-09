from _components.semiconductors._commonInfo import commonInfo

class Digital74Series(commonInfo):
    # electrical ratings
    maxDataInputVoltage = None          # V
    lowLevelVoltage = None              # V
    highLevelVoltage = None             # V
    highLevelOutputCurrent = None       # mA
    lowLevelOutputCurrent = None        # mA
    timeLowToHigh = None                # ns
    timeHighToLow = None                # ns
    maxFrequency = 1 / timeLowToHigh    # Hz
    # 74 series specific characteristics
    numberOfGates = None                # int
    typeOfGate = None                   # AND, NAND, NOR, XOR, etc
    highZ = None                        # bool
    noOfInputs = None                   # int
    noOfOutputs = None                  # int
    synchronous = None                  # bool (1 = synchronous/sequential, 0 = asynchronous)