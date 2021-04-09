from _components.semiconductors.IC.power.Regulator import Regulator

class LM317(Regulator):
    name = "LM317"
    type = "linear"
    packages = ["TO-3", "TO-220", "TO-263", "SOT-223", "TO-252"]
    maxInputVoltage = [40, "V"]
    refVoltage = [1.25, "V"]
    maxOutputVoltage = [maxInputVoltage[0] - refVoltage[0], "V"]
    minOutputVoltage = [1.25, "V"]
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
    name = "LM117"
    type = "linear"
    packages = ["TO-3", "TO"]
    maxInputVoltage = [40, "V"]
    refVoltage = [1.25, "V"]
    maxOutputVoltage = [maxInputVoltage[0] - refVoltage[0], "V"]
    minOutputVoltage = [1.25, "V"]
    maxOutputCurrent = [1.5, "A"]
    minLoadCurrent = [4, "mA"]
    currentLimit = True
    RMSnoise = [0.003, "%Vo"]
    rippleRejection = [65, "dB"]
    maxJunctionTemp = [125, "°C"]

class LM338():
    name = "LM338"
    type = "linear"
    packages = ["TO-220", "TO-CAN"]
    maxInputVoltage = [40, "V"]
    refVoltage = [1.24, "V"]
    maxOutputVoltage = [maxInputVoltage[0] - refVoltage[0], "V"]
    minOutputVoltage = [1.2, "V"]
    maxOutputCurrent = [5, "A"]
    minLoadCurrent = [5, "mA"]
    currentLimit = [8, "A"]
    RMSnoise = [0.003, "%Vo"]
    rippleRejection = [75, "dB"]
    maxJunctionTemp = [125, "°C"]
    datasheet = "https://www.ti.com/lit/ds/symlink/lm338.pdf"
    
    @staticmethod
    def Vout(R1, R2):
        return refVoltage*(1+(R2/R1))+(0.00005*R2)

class LM350():
    name = "LM338"
    type = "linear"
    packages = ["TO-220", "TO-CAN"]
    maxInputVoltage = [33, "V"]
    refVoltage = [1.25, "V"]
    maxOutputVoltage = [maxInputVoltage[0] - refVoltage[0], "V"]
    minOutputVoltage = [1.2, "V"]
    maxOutputCurrent = [4.5, "A"]
    minLoadCurrent = [3.5, "mA"]
    currentLimit = [4.5, "A"]
    RMSnoise = [0.001, "%Vo"]
    rippleRejection = [86, "dB"]
    maxJunctionTemp = [125, "°C"]
    datasheet = "https://www.ti.com/lit/ds/snvs772b/snvs772b.pdf"

    @staticmethod
    def Vout(R1, R2):
        return refVoltage*(1+(R2/R1))+(0.00005*R2)

class TL783():
    name = "LM338"
    type = "linear"
    packages = ["TO-220", "TO-263", "PFM"]
    maxInputVoltage = [125, "V"]
    refVoltage = [1.27, "V"]
    maxOutputVoltage = [maxInputVoltage[0] - refVoltage[0], "V"]
    minOutputVoltage = [1.2, "V"]
    maxOutputCurrent = [1100, "mA"]
    minLoadCurrent = [15, "mA"]
    currentLimit = [1100, "mA"]
    RMSnoise = [0.003, "%Vo"]
    rippleRejection = [76, "dB"]
    maxJunctionTemp = [125, "°C"]
    datasheet = "https://www.ti.com/lit/ds/symlink/tl783.pdf"

    @staticmethod
    def Vout(R1, R2):
        return refVoltage*(1+(R2/R1))+(0.00005*R2)