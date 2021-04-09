from _components.semiconductors._commonInfo import commonInfo

class SRAM(commonInfo):
    # electrical ratings
    maxCurrentPerPin = None             # mA
    outputLowVoltage = None             # V
    outputHighVoltage = None            # V
    inputLeakageCurrent = None          # uA
    IOPullUpResistance = None           # Ω
    inputCapacitance = None             # pF
    outputCapacitance = None            # pF
    # SRAM specific characteristics
    readCycleTime = None                # ns
    addressAccessTime = None            # ns
    outputHoldTime = None               # ns
    chipEnableAccessTime = None         # ns
    outputEnableAccessTime = None       # ns
    writeCycleTime = None               # ns
    averageAccessTime = None            # ns
    wordSize = None                     # bit
    columnSize = None                   # x1000 (k)