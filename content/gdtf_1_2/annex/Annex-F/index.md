---
title: "Annex F, SubPhysicalUnit precisions"
description: "SubPhysicalUnit precisions"
lead: "SubPhysicalUnit precisions"
date: 2020-10-06T08:48:57+00:00
lastmod: 2020-10-06T08:48:57+00:00
draft: false
images: []
weight: 200
toc: true
---

## Annex F (normative) SubPhysicalUnit precisions

### Pulse

Some attributes are named "[EFFECT]Pulse" (for example Shutter(n)StrobePulse). They should behave like a triangular function. Here is how they are defined:
- The main PhysicalUnit is a **frequency** which allows to modify the duration of the period T.
- t = 0s corresponds to the activation of the channel function.
- The **TimeOffset** SubPhysicalUnit is the offset of the end of the pulse from 0, the activation of the channel function, as a percentage of the period T.
- The **DutyCycle** SubPhysicalUnit corresponds to the fraction of one period in which the value is not 0.

![Graph of a Pulse-like attribute and their SubPhysicalUnits](media/Pulse.png "Pulse-like attribute and their SubPhysicalUnits")

*Figure 5. Pulse-like attribute and their SubPhysicalUnits*

If there aren't any value given by the user, the TimeOffset and DutyCycle SubPhysicalUnits are defaulted to 100%:

![Graph of a default Pulse-like attribute and their SubPhysicalUnits](media/Pulse\_Default.png "default Pulse-like attribute and their SubPhysicalUnits")

*Figure 6. Default Pulse-like attribute and their SubPhysicalUnits*

### PulseClose

Some attributes are named "[EFFECT]PulseClose" (for example IrisPulseClose). They should behave like a decreasing ramp. Here is how they are defined:
- The main PhysicalUnit is a **frequency** which allows to modify the duration of the period T.
- t = 0s corresponds to the activation of the channel function.
- The **TimeOffset** SubPhysicalUnit is the offset of the end of the pulse from 0, the activation of the channel function, as a percentage of the period T.
- The **DutyCycle** SubPhysicalUnit corresponds to the fraction of one period in which the value is not 0.

![Graph of a PulseClose-like attribute and their SubPhysicalUnits](media/PulseClose.png "PulseClose-like attribute and their SubPhysicalUnits")

*Figure 7. PulseClose-like attribute and their SubPhysicalUnits*

If there aren't any value given by the user, the TimeOffset and DutyCycle SubPhysicalUnits are defaulted to 100%:

![Graph of a default PulseClose-like attribute and their SubPhysicalUnits](media/PulseClose\_Default.png "default PulseClose-like attribute and their SubPhysicalUnits")

*Figure 8. Default PulseClose-like attribute and their SubPhysicalUnits*

### PulseOpen

Some attributes are named "[EFFECT]PulseOpen" (for example Frost(n)PulseOpen). They should behave like an increasing ramp. Here is how they are defined:
- The main PhysicalUnit is a **frequency** which allows to modify the duration of the period T.
- t = 0s corresponds to the activation of the channel function.
- The **TimeOffset** SubPhysicalUnit is the offset of the end of the pulse from 0, the activation of the channel function, as a percentage of the period T.
- The **DutyCycle** SubPhysicalUnit corresponds to the fraction of one period in which the value is not 0.

![Graph of a PulseOpen-like attribute and their SubPhysicalUnits](media/PulseOpen.png "PulseOpen-like attribute and their SubPhysicalUnits")

*Figure 9. PulseOpen-like attribute and their SubPhysicalUnits*

If there aren't any value given by the user, the TimeOffset and DutyCycle SubPhysicalUnits are defaulted to 100%:

![Graph of a default PulseOpen-like attribute and their SubPhysicalUnits](media/PulseOpen\_Default.png "default PulseOpen-like attribute and their SubPhysicalUnits")

*Figure 10. Default PulseOpen-like attribute and their SubPhysicalUnits*

# Revision History

This section lists all the changes that are made to GDTF.

