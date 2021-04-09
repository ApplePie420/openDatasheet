from _components.semiconductors.IC.analog.Comparator import Comparator

class LM111(Comparator):
    # TODO: sort this shit
    name = "LM111"
    packages = ["TO-99", "CDIP", "PDIP", "CLGA"]
    type = "general-purpose"
    supplyVoltage = [15, "V"]
    differentialInputVoltage = [30, "V"]
    datasheet = "https://www.ti.com/lit/ds/symlink/lm311-n.pdf?"
    manufacturers = "Texas Instruments"
    # comparator specific
    inputOffsetCurrent = [20, "nA"]
    inputOffsetVoltage = [0.7, "mV"]
    voltageGain = [200, "V/mV"]
    saturationVoltage = [0.75, "V"]
    responseTime = [200, "ns"]

class LM311(Comparator):
    # TODO: sort this shit
    name = "LM311"
    packages = ["TO-99", "CDIP", "PDIP", "CLGA"]
    type = "general-purpose"
    supplyVoltage = [15, "V"]
    differentialInputVoltage = [30, "V"]
    datasheet = "https://www.ti.com/lit/ds/symlink/lm311-n.pdf"
    manufacturers = "Texas Instruments"
    # comparator specific
    inputOffsetCurrent = [50, "nA"]
    inputOffsetVoltage = [7.5, "mV"]
    voltageGain = [200, "V/mV"]
    saturationVoltage = [0.4, "V"]
    responseTime = [200, "ns"]