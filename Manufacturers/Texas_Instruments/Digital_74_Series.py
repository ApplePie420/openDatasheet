from _components.semiconductors.IC.logic.74_series import Digital_74_Series

'''
! Basic logic gates
7400 (NAND), 7404 (NOT), 7408 (AND), 7432 (OR), 7486 (XOR)
'''

class 7400(Digital_74_Series):
     # package
    name = "SN74LS00"
    packages = ["SOIC", "CFP", "SO", "CDIP", "SSOP", "LCCC"]
    type = "Quadruple 2-Input Positive NAND Gates"
    # electrical ratings
    supplyVoltage = [7, "V"]
    # thermal ratings
    maxJunctionTemp = [150, "°C"]
    powerDissapation = None
    # technical
    manufacturers = "Texas Instruments"
    datasheet = "https://www.ti.com/lit/ds/sdls025d/sdls025d.pdf"
    manufacturerNo = None
    # else
    maxDataInputVoltage = [5.25, "V"]
    lowLevelVoltage = [0.8, "V"]
    highLevelVoltage = [2, "V"]
    highLevelOutputCurrent = [-1, "mA"]
    lowLevelOutputCurrent = [20, "mA"]
    timeLowToHigh = [15, "ns"]
    timeHighToLow = [15, "ns"]
    maxFrequency = 1 / timeLowToHigh
    # 74 series specific characteristics
    numberOfGates = 4
    typeOfGate = "NAND"
    highZ = False
    noOfInputs = 8
    noOfOutputs = 4
    synchronous = False

class 7404(Digital_74_Series):
     # package
    name = "SN74LS04"
    packages = ["SOIC", "CFP", "SO", "CDIP", "SSOP", "LCCC"]
    type = "Hex Inverter"
    # electrical ratings
    supplyVoltage = [5.257, "V"]
    # thermal ratings
    maxJunctionTemp = [150, "°C"]
    powerDissapation = None
    # technical
    manufacturers = "Texas Instruments"
    datasheet = "https://www.ti.com/lit/ds/sdls029c/sdls029c.pdf"
    manufacturerNo = None
    # else
    maxDataInputVoltage = [5.5, "V"]
    lowLevelVoltage = [0.8, "V"]
    highLevelVoltage = [2, "V"]
    highLevelOutputCurrent = [-0.4, "mA"]
    lowLevelOutputCurrent = [16, "mA"]
    timeLowToHigh = [22, "ns"]
    timeHighToLow = [15, "ns"]
    maxFrequency = 1 / timeLowToHigh
    # 74 series specific characteristics
    numberOfGates = 6
    typeOfGate = "NOT"
    highZ = False
    noOfInputs = 6
    noOfOutputs = 6
    synchronous = False

class 7408(Digital_74_Series):
     # package
    name = "SN74LS08"
    packages = ["SOIC", "CFP", "SO", "CDIP", "SSOP", "LCCC"]
    type = "Quadruple 2-Input Positive AND Gates"
    # electrical ratings
    supplyVoltage = [7, "V"]
    # thermal ratings
    maxJunctionTemp = [150, "°C"]
    powerDissapation = None
    # technical
    manufacturers = "Texas Instruments"
    datasheet = "https://www.ti.com/lit/ds/sdls029c/sdls029c.pdf"
    manufacturerNo = None
    # else
    maxDataInputVoltage = [5.5, "V"]
    lowLevelVoltage = [0.8, "V"]
    highLevelVoltage = [2, "V"]
    highLevelOutputCurrent = [-0.8, "mA"]
    lowLevelOutputCurrent = [16, "mA"]
    timeLowToHigh = [27, "ns"]
    timeHighToLow = [19, "ns"]
    maxFrequency = 1 / timeLowToHigh
    # 74 series specific characteristics
    numberOfGates = 4
    typeOfGate = "AND"
    highZ = False
    noOfInputs = 8
    noOfOutputs = 4
    synchronous = False

class 7432(Digital_74_Series):
     # package
    name = "SN74LS32"
    packages = ["SOIC", "CFP", "SO", "CDIP", "SSOP", "LCCC"]
    type = "Quadruple 2-Input Positive OR Gates"
    # electrical ratings
    supplyVoltage = [7, "V"]
    # thermal ratings
    maxJunctionTemp = [150, "°C"]
    powerDissapation = None
    # technical
    manufacturers = "Texas Instruments"
    datasheet = "https://www.ti.com/lit/ds/symlink/sn7432.pdf"
    manufacturerNo = None
    # else
    maxDataInputVoltage = [5.5, "V"]
    lowLevelVoltage = [0.8, "V"]
    highLevelVoltage = [2, "V"]
    highLevelOutputCurrent = [-0.8, "mA"]
    lowLevelOutputCurrent = [16, "mA"]
    timeLowToHigh = [15, "ns"]
    timeHighToLow = [22, "ns"]
    maxFrequency = 1 / timeLowToHigh
    # 74 series specific characteristics
    numberOfGates = 4
    typeOfGate = "OR"
    highZ = False
    noOfInputs = 8
    noOfOutputs = 4
    synchronous = False

class 7486(Digital_74_Series):
     # package
    name = "SN74LS86"
    packages = ["SOIC", "CFP", "SO", "CDIP", "SSOP", "LCCC"]
    type = "Quadruple 2-Input Positive Exclusive-OR Gates"
    # electrical ratings
    supplyVoltage = [7, "V"]
    # thermal ratings
    maxJunctionTemp = [150, "°C"]
    powerDissapation = None
    # technical
    manufacturers = "Texas Instruments"
    datasheet = "https://www.ti.com/lit/ds/symlink/sn54s86.pdf
    manufacturerNo = None
    # else
    maxDataInputVoltage = [5.5, "V"]
    lowLevelVoltage = [0.8, "V"]
    highLevelVoltage = [2, "V"]
    highLevelOutputCurrent = [-0.8, "mA"]
    lowLevelOutputCurrent = [16, "mA"]
    timeLowToHigh = [23, "ns"]
    timeHighToLow = [17, "ns"]
    maxFrequency = 1 / timeLowToHigh
    # 74 series specific characteristics
    numberOfGates = 4
    typeOfGate = "XOR"
    highZ = False
    noOfInputs = 8
    noOfOutputs = 4
    synchronous = False

'''
! Multiplexers, Demultiplexers, decoders
7442 (BCD/10), 7444 (Gray code/10), 7446 (BCD/7seg), 74138 (3:8 dmx),
74139 (2x 2:4 dmx), 74146 (serial-parallel decoder), 74238 (3:8 dmx), 
74239 (2x 2:4 dmx), 74151 (3:8 mux), 74153 (2x 2:4 mux), 
'''