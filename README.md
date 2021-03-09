# OpenDatasheet Project
This project's goal is to create a free, open source electronic parts database platform. Base idea is, that all parts are user-contributed. 

# Features
## Common values quick access
From each parts' type, a bunch of common itneresting values were picked, that are used in each component, and are quickly accessible. This includes parameters such as `package type, supply voltage, input capacitance, resistance, output current etc.`. 
## Calculations
If there are some calculations provided in datasheet, they are reflected in it's definition. That means you no longer have to manually calculate everything, just find a function for what you want to calculate, plug your variables in and let your computer do the hard work. Simple as that. Let's say you need to know what peak inductor current will be. Just call `SMPS.peak_Inductor_Current(Iload, Vin, Vout, L)`, put appropriate values in and you're done. 

# Contributing
If you want to contribute, please follow **guidelines** in each folder. You can either add new [component type](./_components/) or an existing [part](./Manufacturers).

# Plans for future
[] Integrate SAGE/SymPy/Wolfram to solve equations
[] Create automatic checker if guidelines are met
[] Create REST API
[] Add metaparts