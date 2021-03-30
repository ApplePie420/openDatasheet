from _components.semiconductors.IC.power.Regulator import Regulator

class LM2575(Regulator):
    name = "LM2575"
    type = "switching"
    ######## ! FILLER DATA, DO NOT TRUST
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
        Vout = 1.23*(1+(R2/R1))
        return [Vout, "V"]

    @staticmethod
    def Inductor_ET(Vin, Vout):
        ET = (Vin-Vout)*(Vout/Vin)*(1000/52)
        return [ET, "V*uS"]

    @staticmethod
    def Cout(Vin, Vout, L):
        C = 7.785*(Vin/(Vout*L))
        return [C, "F"]

    @staticmethod
    def Cin(Vin, Vout, Iload):
        C = 1.2*(Vout/(Vout+Vin))*Iload
        return [C, "F"]

    @staticmethod
    def heat_power_dissapation(Vin, Vout, ILoad):
        heat = Vin*10+(Vout/Vin)*ILoad*1.2
        return [heat, "°C"]

    @staticmethod
    def peak_Inductor_Current(Iload, Vin, Vout, L):
        current = (Iload*(Vin+abs(Vout))/Vin)+((Vin*abs(Vout))/(Vin+abs(Vout)))*(1/(2*L*52))
        return [current, "A"]

    @staticmethod
    def dutyCycle(Vout, Vin):
        cycle = abs(Vout)/(abs(Vout)+Vin)
        return [cycle, "kHz"]