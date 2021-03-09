from _components.Regulator import Regulator

class LM317(Regulator):
    name = "LM317"
    type = "linear"
    packages = ["TO-3", "TO-220", "TO-263", "SOT-223", "TO-252"]
    maxInputVoltage = 40                                    # V
    refVoltage = 1.25                                       # V
    maxOutputVoltage = maxInputVoltage - refVoltage         # V
    maxOutputCurrent = 1.5                                  # A
    minLoadCurrent = 0.004                                  # A
    currentLimit = True                                     # bool
    RMSnoise = 0.003                                        # % V_o
    rippleRejection = 65                                    # dB
    maxJunctionTemp = 125                                   # °C 

    @staticmethod
    def Vout(R1, R2):
        return 1.25*(1+(R2/R1))+(0.00005*R2)

    @staticmethod
    def Ilimit(Rs):
        return 1.2/Rs

    @staticmethod
    def heatsink_power(Vin, Vout, Iload):
        return ((Vin-Vout)*Iload)+(Vin*0.00005)

class LM117():
    @staticmethod
    def Vout(R1, R2):
        return 1.25*(1+(R2/R1))+(0.00005*R2)

    @staticmethod
    def heatsink_power(Vin, Vout, Iload):
        return ((Vin-Vout)*Iload)+(Vin*0.00005)

class LM338():
    @staticmethod
    def Vout(R1, R2):
        return 1.25*(1+(R2/R1))+(0.00005*R2)

class LM350():
    @staticmethod
    def Vout(R1, R2):
        return 1.25*(1+(R2/R1))+(0.00005*R2)

class TL783():
    @staticmethod
    def Vout(R1, R2):
        return 1.25*(1+(R2/R1))+(0.00005*R2)