from _components.semiconductors.IC.power.Regulator import Regulator

class LM317(Regulator):
    name = "LM317"
    type = "linear"
    packages = ["TO-3", "TO-220", "TO-263", "SOT-223", "TO-252"]
    maxInputVoltage = [40, "V"]
    refVoltage = [1.25, "V"]
    maxOutputVoltage = [maxInputVoltage[0] - refVoltage[0], "V"]
    maxOutputCurrent = [1.5, "A"]
    minLoadCurrent = [0.004, "A"]
    currentLimit = True
    RMSnoise = [0.003, "%Vo"]
    rippleRejection = [65, "dB"]
    maxJunctionTemp = [125, "°C"]

    @staticmethod
    def Vout(R1, R2):
        vout = refVoltage*(1+(R2/R1))+(0.00005*R2)
        return [vout, "V"]

    @staticmethod
    def Ilimit(Rs):
        current = 1.2/Rs
        return [current, "A"]

    @staticmethod
    def heatsink_power(Vin, Vout, Iload):
        power = ((Vin-Vout)*Iload)+(Vin*0.00005)
        return [power, "W"]

class LM117():
    None

class LM338():
    @staticmethod
    def Vout(R1, R2):
        return refVoltage*(1+(R2/R1))+(0.00005*R2)

class LM350():
    @staticmethod
    def Vout(R1, R2):
        return refVoltage*(1+(R2/R1))+(0.00005*R2)

class TL783():
    @staticmethod
    def Vout(R1, R2):
        return refVoltage*(1+(R2/R1))+(0.00005*R2)