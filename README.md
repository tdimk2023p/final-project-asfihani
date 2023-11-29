
# Design of Palm Gesture Recognition Tracking Human-Computer Interaction System Based on PAJ7620 Motion Sensor

This research presents the design and implementation of a palm gesture recognition tracking human-computer intelligent interaction system
based on the [PAJ7620](https://www.tokopedia.com/lisuinstrument/paj7620-paj7620u2-gesture-recognition-sensor-module) gesture recognition sensor and Arduino
Uno microcontroller for intelligent interaction with [Spotify](https://www.spotify.com) audio
streaming service with the help of the Python and [shpotify](https://github.com/hnarayanan/shpotify) program on a computer running macOS Sonoma.

This research is mandatory for final project on course TD Interaksi Manusia dan Komputer (EF235131) Informatics Engineering, FTEIC, 10 Nopember Institute of Technology (ITS) Surabaya, under supervision Hadziq Fabroyir, S.Kom., Ph.D.

![system design](https://www.imghippo.com/images/1700824949.png)

![design-setup](https://www.imghippo.com/images/1700824825.jpg)


## Features

- right palm -> next track
- left palm -> previous track
- up -> increase the volume
- down -> reduce the volume
- forward -> stop/pause
- backward -> start/resume
- clockwise -> replay track
- anti-clockwise -> shuffle on/off




## Requirements

1. Arduino Uno
2. PAJ7620 Sensor
3. MacOS
4. Python
5. [Spotify](https://www.spotify.com/de-en/download/mac/)
6. [shpotify](https://github.com/hnarayanan/shpotify)

## Installation

1. Download and install [Spotify](https://www.spotify.com/de-en/download/mac/)

2. Setup Arduino Uno and PAJ7620 sensor as the wiring diagram below

![wiring diagram](https://www.imghippo.com/images/1700825548.png)

3. Download [Arduino IDE](https://www.arduino.cc/en/software) and flash the code from the file `code/paj7620_9gestures.ino`. You may need to install `paj7620.h` library file from the Library Manager, follow [this guide](https://www.arduino.cc/reference/en/libraries/gesture-paj7620/) for more information.

4. Install [shpotify](https://github.com/hnarayanan/shpotify)

```bash
brew install shpotify
```

5. Open file `code/spotify.py` and adjust the serial device name if necessary (pro tip: you can issue command `ls /dev/` to see your serial port device name)

6. Run the program using command: `python3 spotify.py`

7. You may asked to adjust the bash/python under `System Preferences > Security & Privacy > Privacy > Accessibility`
## FAQ

#### Question 1

Answer 1

#### Question 2

Answer 2


