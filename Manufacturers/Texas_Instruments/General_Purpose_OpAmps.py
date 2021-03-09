from _components.OpAmp import OpAmp

class LM741A(OpAmp):
    name = "LM741"
    packages = ["TO-99", "CDIP", "PDIP"]
    type = "general-purpose"
    supplyVoltage = 22
    differentialInputVoltage = 30
    maxOffsetVoltage = 0.003
    maxOffsetCurrent = 0.00003
    inputResistance = 6000000
    transientResponse = 0.0000008
    bandwidth = 1500000
    slewRate = 0.7