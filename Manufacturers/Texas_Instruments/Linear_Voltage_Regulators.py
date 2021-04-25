from _components.semiconductors.IC.power.Regulator import Regulator

class LM317(Regulator):
    name = "LM317"
    type = "linear"
    packages = ["TO-3", "TO-220", "TO-263", "SOT-223", "TO-252"]
    datasheet = "https://www.ti.com/lit/ds/symlink/lm317.pdf"
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

    # p11, Equation 1
    @staticmethod
    def Vout(R1, R2):
        vout = refVoltage*(1+(R2/R1))+(0.00005*R2)
        return [vout, "V"]

    # p14, Equation (4)
    @staticmethod
    def Ilimit(Rs):
        current = 1.2/Rs
        return [current, "A"]

    # p6, note (4)
    @staticmethod
    def heatsink_power(Vin, Vout, Iload):
        power = ((Vin-Vout)*Iload)+(Vin*0.00005)
        return [power, "W"]

    class Examples():
        # p13, Figure 13
        @staticmethod
        def exampleAdjustableRegulator(R2, Vout):
            # Compute the value of resistor given recommended R1 value (240R) and a constant
            # R2 = R1((V/1.25)-1)
            R2 = 240 * ((Vout/1.25)-1)
            import schemdraw
            import schemdraw.elements as elm

            elm.style(elm.STYLE_IEC)
            d = schemdraw.Drawing()
            d += elm.Jack().label("Vin")
            d += (reg := elm.VoltageRegulator().label("LM317").anchor("in"))
            d += elm.Dot()
            d += elm.Line().down()
            d += (inCap := elm.Capacitor().down().label("100n"))
            d += elm.Ground()
            d += (outLine := elm.Line().at(reg.out).right())
            d += (adjLine := elm.Line().at(reg.gnd).down().toy(inCap.start))
            d += (adjDot := elm.Dot())
            d.push()
            d += elm.Resistor().down().label(str(int(R2)) + "Ω", rotate=90)
            d += elm.Ground()
            d.pop()
            d += elm.Line().right()
            d.push()
            d += elm.Dot()
            d += (adjR := elm.Resistor().up().toy(outLine.end).label("240Ω"))
            d += elm.Dot()
            d += elm.Capacitor().down().at(adjR.start).label("10u")
            d += elm.Ground()
            d.pop()
            d += elm.Line().right()
            d += elm.Diode().up().toy(outLine.end).label("1N4002")
            d += elm.Dot()
            d.push()
            d += elm.Line().left()
            d.pop()
            d += elm.Line().right()
            d += elm.Dot()
            d.push()
            d += elm.Line().toy(inCap.start).down()
            d += elm.Capacitor().label("1u")
            d += elm.Ground()
            d.pop()
            d += elm.Plug().label(str(Vout) + "V")

            return d.draw()

        # p13, Figure 13
        @staticmethod
        def exampleCurrentLimiter(Ilimit):
            # Compute the value of resistor, given the constant and desired current limit
            R1 = 1.2 / Ilimit
            import schemdraw
            import schemdraw.elements as elm

            elm.style(elm.STYLE_IEC)
            d = schemdraw.Drawing()
            d += elm.Jack().label("Vin")
            d += (reg := elm.VoltageRegulator().label("LM317").anchor("in"))
            d += elm.Dot().at(reg.out)
            d += (pot := elm.Potentiometer().at(reg.out).label(str(R1) + "Ω"))
            d += (feedback := elm.Line().at(pot.tap).left().tox(reg.out))
            d += elm.Line().down().to(reg.out)
            d += elm.Line().at(reg.gnd).right().tox(pot.end)
            d += elm.Line().up().toy(pot.end)
            d += elm.Dot()
            d += elm.Plug().right().label(str(Ilimit) + "A")

            return d.draw()

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