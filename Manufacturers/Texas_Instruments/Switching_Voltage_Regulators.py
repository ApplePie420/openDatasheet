from _components.semiconductors.IC.power.Regulator import Regulator
import math

class LM2575(Regulator):
    name = "LM2575"
    type = "switching"
    ######## ! FILLER DATA, DO NOT TRUST
    packages = ["TO-3", "TO-220", "TO-263", "SOT-223", "TO-252"]
    maxInputVoltage = [40, "V"]
    refVoltage = [1.25, "V"]
    maxOutputVoltage = [maxInputVoltage[0] - refVoltage[0], "V"]
    maxOutputCurrent = [1, "A"]
    minLoadCurrent = [0.02, "A"]
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

    #TODO: make this actually work lmao
    ''''
    Basically what needs to be done, there is this Figure 28 in datasheet, that marks areas in which different
    inductor values should be chosen, based on U and I (on X and Y axis). However, those areas are triangular, 
    not square, and my dumb ass cannot find a way, how to check if those 2 values lies within the triangle.
    No, if-elif chain wont work, because that marks rectangle. And I am sort of unable to comprehend anything
    more complex than multiplication, so no vectoring, goniometry or other wizardry is going to happen.
    There was an idea to rotate the figure 45 degrees to make the lines straight, and then check on that one
    horizontal axis in which area the value lies, but after 5 hours, we were unable to solve this. Help.
    ''''
    @staticmethod
    def selectInductor(Vin, loadCurrent):
        # Vin*cos(fi)-Iout*sin(fi)
        pass

    @staticmethod
    def selectSchottkyDiode(Vr):
        if(Vr > 20):
            schottkyDiode = ["1N5817", "MBR120P", "SR102"]
            return schottkyDiode
        elif(Vr > 30):
            schottkyDiode = ["1N5818", "MBR130P", "11DQ03", "SR103"]
            return schottkyDiode
        elif(Vr > 40):
            schottkyDiode = ["1N5819", "MBR140P", "11DQ04", "SR104"]
            return schottkyDiode
        elif(Vr > 50):
            schottkyDiode = ["MBR150", "11DQ05", "SR105"]
            return schottkyDiode
        elif(Vr > 60):
            schottkyDiode = ["MBR160", "11DQ06", "SR106"]
            return schottkyDiode

    @staticmethod
    def exampleFixedRegulator(Vin, Vout, maxCurrent):
        # Output capacigor is always recommended to be between 47 and 100uF, and max voltage 63V (to be safe)
        outputCap = [100, "µF", 63, "V"]
        # schottky diode, this is basically copy of Table 1
        Vr = Vin * 1.25
        schottkyDiode = selectSchottkyDiode(Vr)
        # output cap, again, recommended 47uF but for some reason at 25V only.. 
        inputCap = [47, "µF", 63, "V"]

    @staticmethod
    def exampleAdjustableRegulator(Vin, Vout, maxCurrent, R1):
        # switching frequency, fixed at 52kHz by manufacturer, in kHz
        f = 52
        # calculate the value of R2 resistor divider
        # R1 should be between 1k and 5k as specified in datasheet
        R2 = R1 * ((Vout / refVoltage) - 1)
        # calculate tghe volt.microsecond constant, that will be matched with look-up table
        Et = Inductor_ET(Vin, Vout)
        inductorL = None
        # output capacitor
        outputCap = Cout(Vin, Vout, inductorL)
        # schottky diode, this is basically copy of Table 1
        Vr = Vin * 1.25
        schottkyDiode = selectSchottkyDiode(Vr)
        # output cap, again, recommended 100uF
        inputCap = [100, "µF", 63, "V"]