from _components.semiconductors.IC.analog.OpAmp import OpAmp

class LM741A(OpAmp):
    name = "LM741"
    packages = ["TO-99", "CDIP", "PDIP"]
    type = "general-purpose"
    supplyVoltage = [22, "V"]
    differentialInputVoltage = [30, "V"]
    maxOffsetVoltage = [0.003, "V"]
    maxOffsetCurrent = [0.00003, "A"]
    inputResistance = [6000000, "Ω"]
    transientResponse = [0.0000008, "s"]
    bandwidth = [1500000, "Hz"]
    slewRate = [0.7, "V/us"]