from _components.semiconductors.IC.analog.OpAmp import OpAmp

class LM741A(OpAmp):
    name = "LM741"
    packages = ["TO-99", "CDIP", "PDIP"]
    type = "dual general-purpose opamp"
    supplyVoltage = [22, "V"]
    differentialInputVoltage = [30, "V"]
    maxOffsetVoltage = [3, "mV"]
    maxOffsetCurrent = [3, "uA"]
    inputResistance = [6, "MΩ"]
    transientResponse = [800, "ns"]
    bandwidth = [1.5, "MHz"]
    slewRate = [0.7, "V/us"]

class LM124(OpAmp):
    name = "LM124"
    packages = []
    type = "quadruple general-purpose"
    supplyVoltage = [16, "V"]
    differentialInputVoltage = [32, "V"]
    maxOffsetVoltage = [7, "mV"]
    maxOffsetCurrent = [50, "A"]
    inputResistance = None      # these two aren't specified in datasheet smh
    transientResponse = None
    bandwidth = [1.2, "MHz"]
    slewRate = [0.5, "V/us"]