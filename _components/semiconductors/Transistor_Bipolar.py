from _components.semiconductors._commonInfo import commonInfo

class Transistor_Bipolar():
    # electrical ratings
    collectorBaseVoltage = None                     # V
    collectorEmitterVoltage = None                  # V
    emitterBaseVoltage = None                       # V
    collectorCurrent = None                         # A
    currentGain = None                              # (multiple)
    collectorEmitterSaturationVoltage = None        # V
    baseEmitterSaturationVoltage = None             # V
    baseEmitterOnVoltage = None                     # V
    bandwidth = None                                # Hz
    outputCapacitance = None                        # pF
    inputCapacitance = None                         # pF