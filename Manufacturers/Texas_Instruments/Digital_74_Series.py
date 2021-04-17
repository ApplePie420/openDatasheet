from _components.semiconductors.IC.logic.74_series import Digital_74_Series

'''
! Basic logic gates
7400 (NAND) [X], 7404 (NOT) [X], 7408 (AND) [X], 7432 (OR) [X], 7486 (XOR) [X]
'''

class 7400(Digital_74_Series):
     # package
    name = "SN74LS00"
    packages = ["SOIC", "CFP", "SO", "CDIP", "SSOP", "LCCC"]
    type = "Quadruple 2-Input Positive NAND Gates"
    # electrical ratings
    supplyVoltage = [5.5, "V"]
    # thermal ratings
    maxJunctionTemp = [150, "°C"]
    powerDissapation = None
    # technical
    manufacturers = "Texas Instruments"
    datasheet = "https://www.ti.com/lit/ds/sdls025d/sdls025d.pdf"
    manufacturerNo = None
    # 74 series specific characteristics
    maxDataInputVoltage = [supplyVoltage "V"]
    lowLevelVoltage = [0.8, "V"]
    highLevelVoltage = [2, "V"]
    highLevelOutputCurrent = [-1, "mA"]
    lowLevelOutputCurrent = [20, "mA"]
    timeLowToHigh = [15, "ns"]
    timeHighToLow = [15, "ns"]
    maxFrequency = 1 / timeLowToHigh
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
    # 74 series specific characteristics
    maxDataInputVoltage = [supplyVoltage, "V"]
    lowLevelVoltage = [0.8, "V"]
    highLevelVoltage = [2, "V"]
    highLevelOutputCurrent = [-0.4, "mA"]
    lowLevelOutputCurrent = [16, "mA"]
    timeLowToHigh = [22, "ns"]
    timeHighToLow = [15, "ns"]
    maxFrequency = 1 / timeLowToHigh
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
    supplyVoltage = [5.5, "V"]
    # thermal ratings
    maxJunctionTemp = [150, "°C"]
    powerDissapation = None
    # technical
    manufacturers = "Texas Instruments"
    datasheet = "https://www.ti.com/lit/ds/sdls029c/sdls029c.pdf"
    manufacturerNo = None
    # 74 series specific characteristics
    maxDataInputVoltage = [supplyVoltage, "V"]
    lowLevelVoltage = [0.8, "V"]
    highLevelVoltage = [2, "V"]
    highLevelOutputCurrent = [-0.8, "mA"]
    lowLevelOutputCurrent = [16, "mA"]
    timeLowToHigh = [27, "ns"]
    timeHighToLow = [19, "ns"]
    maxFrequency = 1 / timeLowToHigh
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
    supplyVoltage = [5.5, "V"]
    # thermal ratings
    maxJunctionTemp = [150, "°C"]
    powerDissapation = None
    # technical
    manufacturers = "Texas Instruments"
    datasheet = "https://www.ti.com/lit/ds/symlink/sn7432.pdf"
    manufacturerNo = None
    # 74 series specific characteristics
    maxDataInputVoltage = [supplyVoltage, "V"]
    lowLevelVoltage = [0.8, "V"]
    highLevelVoltage = [2, "V"]
    highLevelOutputCurrent = [-0.8, "mA"]
    lowLevelOutputCurrent = [16, "mA"]
    timeLowToHigh = [15, "ns"]
    timeHighToLow = [22, "ns"]
    maxFrequency = 1 / timeLowToHigh
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
    supplyVoltage = [5.5, "V"]
    # thermal ratings
    maxJunctionTemp = [150, "°C"]
    powerDissapation = None
    # technical
    manufacturers = "Texas Instruments"
    datasheet = "https://www.ti.com/lit/ds/symlink/sn54s86.pdf"
    manufacturerNo = None
    # 74 series specific characteristics
    maxDataInputVoltage = [supplyVoltage, "V"]
    lowLevelVoltage = [0.8, "V"]
    highLevelVoltage = [2, "V"]
    highLevelOutputCurrent = [-0.8, "mA"]
    lowLevelOutputCurrent = [16, "mA"]
    timeLowToHigh = [23, "ns"]
    timeHighToLow = [17, "ns"]
    maxFrequency = 1 / timeLowToHigh
    numberOfGates = 4
    typeOfGate = "XOR"
    highZ = False
    noOfInputs = 8
    noOfOutputs = 4
    synchronous = False

'''
! Multiplexers, Demultiplexers, decoders
7442 (BCD/10) [X], 7444 (Gray code/10), 7446 (BCD/7seg) [X], 74138 (3:8 dmx) [X],
74139 (2x 2:4 dmx) [X], 74146 (serial-parallel decoder) [X], 74238 (3:8 dmx) [X], 
74239 (2x 2:4 dmx), 74151 (3:8 mux) [X], 74153 (2x 2:4 mux) [X], 
'''

class 7442(Digital_74_Series):
     # package
    name = "SN74LS42"
    packages = ["SOIC", "CFP", "SO", "CDIP", "SSOP", "LCCC"]
    type = "4-Line BCD To 10-Line Decimal Decoder"
    # electrical ratings
    supplyVoltage = [5.5, "V"]
    # thermal ratings
    maxJunctionTemp = [150, "°C"]
    powerDissapation = None
    # technical
    manufacturers = "Texas Instruments"
    datasheet = "https://www.ti.com/lit/ds/sdls109/sdls109.pdf"
    manufacturerNo = None
    # 74 series specific characteristics
    maxDataInputVoltage = [supplyVoltage, "V"]
    lowLevelVoltage = [0.8, "V"]
    highLevelVoltage = [2, "V"]
    highLevelOutputCurrent = [-0.4, "mA"]
    lowLevelOutputCurrent = [8, "mA"]
    timeLowToHigh = None
    timeHighToLow = None
    maxFrequency = 1 / timeLowToHigh
    numberOfGates = None
    typeOfGate = "BCD/DEC"
    highZ = False
    noOfInputs = 4
    noOfOutputs = 10
    synchronous = False

class 7446(Digital_74_Series):
     # package
    name = "SN74LS46"
    packages = ["SOIC", "CFP", "SO", "CDIP", "SSOP", "LCCC"]
    type = "BCD To Seven Segment Decoder"
    # electrical ratings
    supplyVoltage = [5.5, "V"]
    # thermal ratings
    maxJunctionTemp = [150, "°C"]
    powerDissapation = None
    # technical
    manufacturers = "Texas Instruments"
    datasheet = "https://www.ti.com/lit/ds/sdls111/sdls111.pdf"
    manufacturerNo = None
    # 74 series specific characteristics
    maxDataInputVoltage = [supplyVoltage, "V"]
    lowLevelVoltage = [0.8, "V"]
    highLevelVoltage = [2, "V"]
    highLevelOutputCurrent = [-0.4, "mA"]
    lowLevelOutputCurrent = [8, "mA"]
    timeLowToHigh = [100, "ns"]
    timeHighToLow = [100, "ns"]
    maxFrequency = 1 / timeLowToHigh
    numberOfGates = None
    typeOfGate = "BCD/7SEG"
    highZ = False
    noOfInputs = 4
    noOfOutputs = 7
    synchronous = False

class 74138(Digital_74_Series):
     # package
    name = "SN74LS138"
    packages = ["SOIC", "CFP", "SO", "CDIP", "SSOP", "LCCC"]
    type = "3 Line to 8 Line Demultiplexer"
    # electrical ratings
    supplyVoltage = [5.5, "V"]
    # thermal ratings
    maxJunctionTemp = [150, "°C"]
    powerDissapation = None
    # technical
    manufacturers = "Texas Instruments"
    datasheet = "https://www.ti.com/lit/ds/sdls014/sdls014.pdf"
    manufacturerNo = None
    # 74 series specific characteristics
    maxDataInputVoltage = [supplyVoltage, "V"]
    lowLevelVoltage = [0.8, "V"]
    highLevelVoltage = [2, "V"]
    highLevelOutputCurrent = [-0.4, "mA"]
    lowLevelOutputCurrent = [8, "mA"]
    timeLowToHigh = None
    timeHighToLow = None
    maxFrequency = 1 / timeLowToHigh
    numberOfGates = None
    typeOfGate = "3:8 Demux"
    highZ = False
    noOfInputs = 3
    noOfOutputs = 8
    synchronous = False

class 74139(Digital_74_Series):
     # package
    name = "SN74LS139"
    packages = ["SOIC", "CFP", "SO", "CDIP", "SSOP", "LCCC"]
    type = "Dual 2 Line to 4 Line Demultiplexer"
    # electrical ratings
    supplyVoltage = [5.5, "V"]
    # thermal ratings
    maxJunctionTemp = [150, "°C"]
    powerDissapation = None
    # technical
    manufacturers = "Texas Instruments"
    datasheet = "https://www.ti.com/lit/ds/sdls013a/sdls013a.pdf"
    manufacturerNo = None
    # 74 series specific characteristics
    maxDataInputVoltage = [supplyVoltage, "V"]
    lowLevelVoltage = [0.8, "V"]
    highLevelVoltage = [2, "V"]
    highLevelOutputCurrent = [-0.4, "mA"]
    lowLevelOutputCurrent = [8, "mA"]
    timeLowToHigh = None
    timeHighToLow = None
    maxFrequency = 1 / timeLowToHigh
    numberOfGates = None
    typeOfGate = "2x 2:4 Demux"
    highZ = False
    noOfInputs = 2
    noOfOutputs = 4
    synchronous = False

class 74164(Digital_74_Series):
     # package
    name = "SN74LS164"
    packages = ["SOIC", "CFP", "SO", "CDIP", "SSOP", "LCCC"]
    type = "8 Bit Serial-In Parallel-Out Shift Register"
    # electrical ratings
    supplyVoltage = [6, "V"]
    # thermal ratings
    maxJunctionTemp = [150, "°C"]
    powerDissapation = None
    # technical
    manufacturers = "Texas Instruments"
    datasheet = "https://www.ti.com/lit/ds/schs240a/schs240a.pdf"
    manufacturerNo = None
    # 74 series specific characteristics
    maxDataInputVoltage = [supplyVoltage, "V"]
    lowLevelVoltage = [1.65, "V"]
    highLevelVoltage = [2.4, "V"]
    highLevelOutputCurrent = None
    lowLevelOutputCurrent = None
    timeLowToHigh = None
    timeHighToLow = None
    maxFrequency = [7, "MHz"]
    numberOfGates = None
    typeOfGate = "8-Bit Serial-In Parallel-Out"
    highZ = False
    noOfInputs = 2
    noOfOutputs = 8
    synchronous = False

class 74238(Digital_74_Series):
     # package
    name = "CD74ACT238"
    packages = ["SOIC", "CFP", "SO", "CDIP", "SSOP", "LCCC"]
    type = "3 Line to 8 Line Demultiplexer"
    # electrical ratings
    supplyVoltage = [5.5, "V"]
    # thermal ratings
    maxJunctionTemp = [150, "°C"]
    powerDissapation = None
    # technical
    manufacturers = "Texas Instruments"
    datasheet = "https://www.ti.com/lit/ds/symlink/cd74act238.pdf"
    manufacturerNo = None
    # 74 series specific characteristics
    maxDataInputVoltage = [supplyVoltage, "V"]
    lowLevelVoltage = [0.8, "V"]
    highLevelVoltage = [2, "V"]
    highLevelOutputCurrent = [-24, "mA"]
    lowLevelOutputCurrent = [24, "mA"]
    timeLowToHigh = [10, "ns"]
    timeHighToLow = [10, "ns"]
    maxFrequency = 1 / timeLowToHigh
    numberOfGates = None
    typeOfGate = "3:8 Demultiplexer"
    highZ = False
    noOfInputs = 3
    noOfOutputs = 8
    synchronous = False

class 74151(Digital_74_Series):
     # package
    name = "SN74151"
    packages = ["SOIC", "CFP", "SO", "CDIP", "SSOP", "LCCC"]
    type = "8 Line to 1 Line Multiplexer"
    # electrical ratings
    supplyVoltage = [5.5, "V"]
    # thermal ratings
    maxJunctionTemp = [150, "°C"]
    powerDissapation = None
    # technical
    manufacturers = "Texas Instruments"
    datasheet = "https://www.ti.com/lit/ds/symlink/sn74ls151.pdf"
    manufacturerNo = None
    # 74 series specific characteristics
    maxDataInputVoltage = [supplyVoltage, "V"]
    lowLevelVoltage = [0.8, "V"]
    highLevelVoltage = [2, "V"]
    highLevelOutputCurrent = [40, "mA"]
    lowLevelOutputCurrent = [-1.6, "mA"]
    timeLowToHigh = [8, "ns"]
    timeHighToLow = [8, "ns"]
    maxFrequency = 1 / timeLowToHigh
    numberOfGates = None
    typeOfGate = "3:8 Mux"
    highZ = False
    noOfInputs = 11
    noOfOutputs = 1
    synchronous = False

class 74153(Digital_74_Series):
     # package
    name = "SN74153"
    packages = ["SOIC", "CFP", "SO", "CDIP", "SSOP", "LCCC"]
    type = "Dual 4 Line to 1 Line Data Multiplexer"
    # electrical ratings
    supplyVoltage = [5.5, "V"]
    # thermal ratings
    maxJunctionTemp = [150, "°C"]
    powerDissapation = None
    # technical
    manufacturers = "Texas Instruments"
    datasheet = "https://www.ti.com/lit/ds/symlink/sn74ls151.pdf"
    manufacturerNo = None
    # 74 series specific characteristics
    maxDataInputVoltage = [supplyVoltage, "V"]
    lowLevelVoltage = [0.8, "V"]
    highLevelVoltage = [2, "V"]
    highLevelOutputCurrent = [40, "mA"]
    lowLevelOutputCurrent = [-1.6, "mA"]
    timeLowToHigh = [14, "ns"]
    timeHighToLow = [14, "ns"]
    maxFrequency = 1 / timeLowToHigh
    numberOfGates = None
    typeOfGate = "2x 2:4 Mux"
    highZ = False
    noOfInputs = 6
    noOfOutputs = 1
    synchronous = False