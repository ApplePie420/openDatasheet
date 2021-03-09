class Transistor_Bipolar():
    # package
    name = "unknown"
    packages = []
    type = None
    # electrical ratings
    collectorBaseVoltage = None                     # V
    collectorEmitterVoltage = None                  # V
    emitterBaseVoltage = None                       # V
    collectorCurrent = None                         # A
    currentGain = None                              # multiple
    collectorEmitterSaturationVoltage = None        # V
    baseEmitterSaturationVoltage = None             # V
    baseEmitterOnVoltage = None                     # V
    bandwidth = None                                # Hz
    outputCapacitance = None                        # pF
    inputCapacitance = None                         # pF
    # thermal ratings
    maxJunctionTemp = None                          # °C
    # technical
    manufacturers = None
    datasheet = None
    manufacturerNo = None