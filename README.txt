KPA Bridge  (EXPERIMENTAL)
==========================
One program for your Elecraft KPA1500 with Thetis, Thetis HL2, SDR-VST3,
NereusSDR and a FlexRadio running SmartSDR (the amp is shown there as a
Power Genius XL and a Tuner Genius XL). Only one radio is used at a time.

Start:   start_kpa_bridge.bat            Stop:  Stop_Bridge.bat
Help:    KPA_Bridge_Help.html  (full help; print it with Ctrl+P)
Status:  http://127.0.0.1:8080/flex      (FlexRadio login and meters)
Tests:   Run_Selftest.bat
Remove:  Uninstall_KPA_Bridge.bat

Run only ONE bridge at a time. This one closes a running older bridge
(Thetis, SDR or SmartSDR bridge) when it starts, so they do not fight over the amp.

Design and on-air testing by KW4EX. No warranty, use at your own risk.
Not made, approved or supported by Elecraft, FlexRadio, Telepost, Thetis or NereusSDR.
