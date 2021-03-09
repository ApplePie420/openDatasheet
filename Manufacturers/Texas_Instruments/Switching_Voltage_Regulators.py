from _components.Regulator import Regulator
class LM2575(Regulator):
    @staticmethod
    def Vout(R1, R2):
        return 1.23*(1+(R2/R1))

    @staticmethod
    def Inductor_ET(Vin, Vout):
        return (Vin-Vout)*(Vout/Vin)*(1000/52)

    @staticmethod
    def Cout(Vin, Vout, L):
        return 7.785*(Vin/(Vout*L))

    @staticmethod
    def Cin(Vin, Vout, Iload):
        return 1.2*(Vout/(Vout+Vin))*Iload

    @staticmethod
    def heat_power_dissapation(Vin, Vout, ILoad):
        return Vin*10+(Vout/Vin)*ILoad*1.2

    @staticmethod
    def peak_Inductor_Current(Iload, Vin, Vout, L):
        return (Iload*(Vin+abs(Vout))/Vin)+((Vin*abs(Vout))/(Vin+abs(Vout)))*(1/(2*L*52))

    @staticmethod
    def dutyCycle(Vout, Vin):
        return abs(Vout)/(abs(Vout)+Vin)