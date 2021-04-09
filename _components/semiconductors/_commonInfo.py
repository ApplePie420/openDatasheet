class commonInfo():
    # package
    name = "unknown"                    # Name of the component, without version letters (i.e. only LM314, NE555, 78L05)
    packages = []                       # Array of all packages as specified by datasheet (TO-92, SOIC-14, DPAK, ...)
    type = None                         # "Generic OpAmp", "Switch Mode", "Darlington" etc.
    # electrical ratings
    supplyVoltage = None                # V (symm)
    # thermal ratings
    maxJunctionTemp = None              # °C
    powerDissapation = None             # W
    # technical
    manufacturers = None                # array of all manufacturers
    datasheet = None                    # URL to the pdf datasheet (best if it's link to official site)
    manufacturerNo = None               # number of part as specified by manufacturer (is there's more, put them in array of tuples)