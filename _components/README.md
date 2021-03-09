# Components guidelines
## Naming conventions
Each part type should be in it's own file, named `Part.py`, singular with leading capital letter. Each class starts with also capital letter, and all elements in class are in camelCase. 
## Characteristics
Place similiar characteristics in it's own commented category, i.e.
```python
# electrical characteristics
voltage = None
curent = None
# mechanical characteristics
length = None
width = None
# thermal characteristics 
maxTemp = None
```
All values default to `None`. In this case, if no value is defined, it simply returns this value. 

Try to filter necessary, useful and commonly sought for information. You can include everything, but it's not advised to. 

If there already is a row with information you want, leave it - don't delete and move somewhere else. Also double check what you just read, and check units in comment after the row. Try not to be redundant.

All methods should be `@staticmethod`. Try to condense it to simple return, however if equation is too long, or needs additional steps, or simply would be too unreadable, feel free to write as many steps as you want. What matters is the arguments (should be named as in datasheet) and output. 

Include only **GENERAL** equations, that apply to **ALL** parts in this category. Examples would be power efficiency (in basically everything), resistor divider, different types/combinations of RLC filters, etc.

## Example of properly documented part
```python
class Regulator():
    # package
    name = "unknown"
    packages = []
    type = None
    # electrical ratings
    maxInputVoltage = None          # V
    maxOutputVoltage = None         # V
    maxOutputCurrent = None         # A
    refVoltage = None               # V
    minLoadCurrent = None           # A
    currentLimit = None             # bool
    RMSnoise = None                 # %V_o
    rippleRejection = None          # dB
    # thermal ratings
    maxJunctionTemp = None          # °C
    # technical
    manufacturers = None
    datasheet = None
    manufacturerNo = None

    @staticmethod
    def efficiency(Pout, Pin):
        return Pout/Pin
```

## List of all units and their acronyms
Please refer to [this document.](documentation/units_list.md)