class OpAmp():
    # package
    name = "unknown"
    packages = []
    type = None
    # electrical ratings
    supplyVoltage = None                # V (symm)
    differentialInputVoltage = None     # V (symm)
    maxOffsetVoltage = None             # V
    maxOffsetCurrent = None             # A
    inputResistance = None              # Ω
    transientResponse = None            # s
    bandwidth = None                    # Hz
    slewRate = None                     # V/μS
    # thermal ratings
    maxJunctionTemp = None              # °C
    # technical
    manufacturers = None
    datasheet = None
    manufacturerNo = None

    @staticmethod
    def gain(R1, R2):
        return 1 + (2/R1)
