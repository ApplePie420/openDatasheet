# Components guidelines
## Naming conventions
There are folders for each manufacturer. If it exists, don't overwrite, recreate or anything. Use the same naming conventions.

Folder and file names are in `Pascal_Snake_Case`. Each file in manufacturer's folder should represent a viable category, that can be found on their website. For example, _General Purpose OpAmp_, _DDR DRAM_ or _Linear Voltage Regulators_ are all valid names. **DO NOT** include part's numbers in files. 
## Characteristics
All variables should be defined in it's **SI unit base value** (that means volts, meters, amperes, farads, ohms) __if not stated otherwise__. 

Each variable is a 2-value sized array (if not required otherwise), where `[0]` is value and `[1]` is [unit.](../documentation/units_list.md)  Sometimes, it's unnecessary to use big units (such as farads for input capacitance, almost never bigger than nanofarads). In that case, units can be smaller, but be sure to specify it (e.g. return `[100, "nF"]`). Same goes for methods (they return array of value and unit).

Each file should start with appropriate imports of `component` class:
```python
from _components.OpAmp import OpAmp
```

Next, define class with component's name (__LM75A, BC547C, AtTiny13__). Pass the component parameter to it, and extend. That means fill up **as much data as possible**. Open the component class in another window, and follow everything line by line. There should be cases where you can't fill in data (missing/not present), in that case, do not even define it. It will return `None` by default. 

All methods should be `@staticmethod`. If name doesn't start with unit, you should follow `snake_case` convention. 

Methods should be part-specific. If there are methods already defined in general component, **DO NOT** redefine it. You can call previously defined methods, just let user know about it (put a comment, try/catch, if/print). 

## Example of properly documented part
```python
class LM317(Regulator):
    name = "LM317"
    type = "linear"
    packages = ["TO-3", "TO-220", "TO-263", "SOT-223", "TO-252"]
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
        return 1.25*(1+(R2/R1))+(0.00005*R2)

    @staticmethod
    def Ilimit(Rs):
        return 1.2/Rs
```

## List of all units and their acronyms
Please refer to [this document.](../documentation/units_list.md)