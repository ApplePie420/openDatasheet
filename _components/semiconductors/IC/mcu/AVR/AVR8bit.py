class AVR_8bit():
    # package
    name = "unknown"
    packages = []
    type = None
    # electrical ratings
    maxSupplyVoltage = None             # V
    maxCurrentPerPin = None             # mA
    outputLowVoltage = None             # V
    outputHighVoltage = None            # V
    inputLeakageCurrent = None          # uA
    IOPullUpResistance = None           # Ω
    maxClockFrequency = None            # MHz at recommended Vcc
    # MCU/AVR specific characteristics
    architecture = None                 # RISC/CISC
    numberOfRegisters = None            # int
    RAMsize = None                      # KiB 
    FLASHsize = None                    # KiB
    EEPROMsize = None                   # KiB
    timerCounterNumber = None           # int
    PWMchannels = None                  # int
    RTC = None                          # bool
    ADCresolution = None                # bit
    ADC = None                          # int
    UART = None                         # int
    I2C = None                          # int
    SPI = None                          # int
    oneWire = None                      # int
    CAN = None                          # int
    I2S = None                          # int
    USBhost = None                      # int
    USBdevice = None                    # int
    Ethernet = None                     # int
    OTFdebugger = None                  # bool (OTF = On The Fly, like JTAG or debugWire)
    sleepMode = None                    # list (all modes as string list)
    interrupts = None                   # int
    watchdog = None                     # bool
    onChipPLA = None                    # int (0 if none, >0 represents number of programmable cells)
    arduinoBootloaderCompatible = None  # bool
    # thermal ratings
    maxJunctionTemp = None              # °C
    # technical
    manufacturers = None
    datasheet = None
    manufacturerNo = None