# KPA Bridge (experimental)

**Experimental. Windows, Mac and Linux.** The Windows files in this repository are batch files. Mac and Linux have their own installer, `KPA_Bridge_v3.0g_Mac_Linux.zip`, in the [latest release's Assets](https://github.com/kw4ex/kpa-bridge/releases/tag/v3.0g) (unzip it and double-click `Install_KPA_Bridge.command`). It was tested by KW4EX on a Mac; Linux is less tested. A Raspberry Pi version has not been tested yet.

**KPA Bridge is essentially the [KPA1500 SDR Bridge](https://github.com/kw4ex/kpa1500-sdr-bridge) and the [KPA1500 SmartSDR Bridge](https://github.com/kw4ex/kpa1500-smartsdr-bridge) combined into one program.** One install connects an Elecraft **KPA1500** amplifier to **Thetis** (also Thetis HL2 and SDR-VST3), **NereusSDR**, and a **FlexRadio running SmartSDR**, where the amplifier shows up as a **Power Genius XL** and a **Tuner Genius XL**. Only one radio is on the air at a time; the amplifier follows the one in use. An optional Telepost LP-100A meter and a FlexControl knob are supported. The two older bridges stay available and are not changed.

Design and on-air testing by KW4EX. Version 3.0g.

## What it does
- **Follows the radio.** The amplifier changes band by itself with the frequency of whichever radio last tuned or transmitted. When you start SmartSDR while Thetis is in use, the amp stays where it is.
- **Thetis and NereusSDR side:** Standby on Tune, live amplifier and LP-100A readings, Operate/Standby, ATU, antenna, fan, clear fault, power on/off, the FlexControl knob, no-antenna protection, ready-made Thetis windows (Telemetry, Controls, Knob), a browser control panel and a small **Applet** window.
- **FlexRadio side:** the KPA1500 appears in SmartSDR as a PGXL (power, SWR, drive, current and temperature meters, Operate/Standby) and a TGXL (Operate, Bypass, Tune, return-loss and forward-power meters, and the tuner's L and C bars). Works on the PC, on a phone, and over SmartLink. No serial cable needed.
- **Over-drive protection** for both kinds of radio: set one limit in watts for the drive into the amplifier and the full power of each radio (a Flex 100 W, a Hermes Lite 2 5 W). It warns, or holds the radio's RF power (and, on a Flex, its TUNE power) at the limit, and puts the amp in STANDBY if the drive stays over. Only while the amp is in OPERATE.
- **Software key** (amplifier firmware 3.07 or newer): the bridge keys the amplifier by network command while either radio transmits, including a Flex TUNE from SmartSDR on a phone.
- Starting a new bridge closes one that is already running; `Stop_Bridge.bat` closes it cleanly.
- The installer makes a **KPA Bridge** shortcut (Desktop, Start menu, and optionally Windows start-up) with its own icon. One shortcut starts and stops: if the bridge is running it asks "Stop it now? Y or N", if not it starts without questions.

## Download

**Start at the [Releases page](https://github.com/kw4ex/kpa-bridge/releases).** Open the newest entry. In the **Assets** list click **Install_KPA_Bridge.bat** (not "Source code"). Step-by-step instructions are on the release page.

**Guide:** [Install and User Guide (PDF)](docs/guides/KPA-Bridge-guide.pdf), also in the Assets list of each release and installed with the program as `KPA_Bridge_Help.html`.

## Install (Windows)
1. Install Python 3.8 or newer from python.org (tick Add Python to PATH).
2. Download `Install_KPA_Bridge.bat` from the Releases page and double-click it. It asks a few short questions (amplifier, Thetis or NereusSDR, FlexRadio, LP-100A, panel) and installs into its own `KPA_Bridge` subfolder (suggested: `C:\RadioScripts`). It can also make the shortcuts, open the firewall ports, run a self-test and add the KPA1500 windows to Thetis.
3. Start the bridge with the **KPA Bridge** shortcut or `start_kpa_bridge.bat`. For a Flex, look for the **PGXL** and **TGXL** in SmartSDR.

## Settings in the radio programs (once)
- **Thetis:** Setup > Serial/Network/Midi CAT > Network > TCI Server: `127.0.0.1:50001`, tick TCI Server Running.
- **NereusSDR:** File > Settings > CAT & Network: TCI Server on (`127.0.0.1`, `50001`), TCP CAT on (`127.0.0.1`, `13013`) with CAT 1 VFO A = Slice A.
- **FlexRadio:** nothing; the radio must be on the same network. For SmartSDR from outside your home (SmartLink) forward TCP 4994 and UDP 4993 to the radio.

## Good to know
- Run **only one bridge at a time**. This one closes a running [KPA1500 SDR Bridge](https://github.com/kw4ex/kpa1500-sdr-bridge), [KPA1500 SmartSDR Bridge](https://github.com/kw4ex/kpa1500-smartsdr-bridge) or [KPA1500 Thetis Bridge](https://github.com/kw4ex/kpa1500-thetis-bridge) when it starts, and they close it. Those programs stay available. Do not use it together with the Zeus KPA1500 add-on.
- The amplifier input still goes to one radio at a time: switch the cable or your antenna switch yourself.
- Uninstall with `Uninstall_KPA_Bridge.bat` in the install folder; it deletes only the bridge's own files and shortcuts.
- `Run_Selftest.bat` runs the built-in tests with simulated equipment (no amplifier or radio needed).

## Files
- `kpa_bridge.py` the program (Python standard library only; `pyserial` only for the LP-100A and the knob)
- `kpa_flex_emulation.py` the FlexRadio part (PGXL and TGXL)
- `kpa_bridge.ico` the program icon
- `start_kpa_bridge.bat`, `Open_Applet.bat`, `Stop_Bridge.bat`, `Run_Selftest.bat` double-click helpers
- `Install_KPA_Bridge.bat`, `Uninstall_KPA_Bridge.bat` installer and uninstaller
- `kpa_thetis_setup.py`, `Setup_Thetis_Containers.bat`, `Undo_Thetis_Containers.bat` add or remove the KPA1500 windows inside Thetis
- `KPA_Network_Check.bat`, `kpa_netcheck.ps1` read-only network check
- `KPA_Bridge_Help.html` the full help

## Status
Experimental. Tested against simulated amplifier and radio programs and on one station (Thetis, HL2 and SmartSDR, one radio at a time). Reports are welcome: open an issue.

**No warranty. Use at your own risk.** Shared as is by one radio operator. Not made, approved or supported by Elecraft, FlexRadio, Telepost, Thetis or NereusSDR.

## Licence
MIT, see `LICENSE`.
