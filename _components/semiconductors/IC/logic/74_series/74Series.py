class Digital74Series():
    # package
    name = "unknown"
    packages = []
    type = None
    # electrical ratings
    maxDataInputVoltage = None          # V
    maxSupplyVoltage = None             # V
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
    # thermal ratings
    maxJunctionTemp = None              # °C
    # technical
    manufacturers = None
    datasheet = None
    manufacturerNo = None