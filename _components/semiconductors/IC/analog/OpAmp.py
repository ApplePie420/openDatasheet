from _components.semiconductors._commonInfo import commonInfo

class OpAmp(commonInfo):
    # OpAmp specific characteristics
    transientResponse = None            # s
    bandwidth = None                    # Hz
    slewRate = None                     # V/μS
    maxOffsetVoltage = None             # V
    maxOffsetCurrent = None             # A

    @staticmethod
    def gain(R1, R2):
        return 1 + (2/R1)
