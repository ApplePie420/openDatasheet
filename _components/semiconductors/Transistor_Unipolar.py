class Transistor_Unipolar():
    # package
    name = "unknown"
    packages = []
    type = None
    # electrical ratings
    drainSourceVoltage = None               # V
    gateSourceVoltage = None                # V
    contDrainCurrent = None                 # A
    pulseDrainCurrent = None                # A
    peakDiodeRecoveryTime = None            # μs
    drainSourceBreakdown = None             # V
    gateSourceLeakageCurrent = None         # nA
    zeroGateVoltageDrainCurrent = None      # nA
    inputCapacitance = None                 # pF
    outputCapacitance = None                # pF
    turnOnDelay = None                      # μs
    riseTime = None                         # μs
    rutnOffTime = None                      # μs
    fallTime = None                         # μs
    internalDrainInductance = None          # μH
    internalSourceInductance = None         # μH
    # drain-source diode ratings
    continousSourceDrainDiodeCurrent = None # A
    bodyDiodeVoltage = None                 # V
    diodeTonTime = None                     # μs
    # thermal ratings
    maxJunctionTemp = None                  # °C
    # technical
    manufacturers = None
    datasheet = None
    manufacturerNo = None