# IndoorNavigation

A side project I was curious about and how it can be implemented. It's going to be a learning curve, so I'll be implementing new things as I learn them, until it becomes a complete indoor navigation system!

<br/>

# 28 December 2024
- measure the distance from the device to the connected Wi-Fi access point using RSSI (Received Signal Strength Indicator).
- update the distance in real-time (every 500ms).

## How it works
1. The distance is calculated using the **log-distance path loss model**:
<br/><br/>![image](https://github.com/user-attachments/assets/ea6fa568-a072-441d-8c17-bab733af216b)<br/>
- **RSSI**: Signal strength in dBm (retrieved programmatically).
- **RSSI_ref**: Signal strength at 1 meter from the access point (measured empirically).
- **n**: Path-loss exponent (varies depending on the environment, typically 2-4).

2. The app fetches the RSSI value of the connected Wi-Fi access point and updates the calculated distance every 500 milliseconds.

## Prerequisites
- Android Studio (latest version recommended).
- An Android device with Wi-Fi capabilities.
- A Wi-Fi access point for testing.

## Setup and Installation

1. Clone the repository
2. Open the project in Android Studio.
3. Add the following permissions to AndroidManifest.xml:
    - `<uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />`
    - `<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />`
5. Sync the project with Gradle to ensure all dependencies are installed:
    - `implementation 'androidx.appcompat:appcompat:1.6.1'`
    - `implementation 'androidx.core:core-ktx:1.12.0'`
7. Build and run the app on a physical device (not an emulator).

<br/><br/><br/><br/>

# 25 April 2025
So... navigating needs a map... pretty obvious, right? The next step was to create a floor layout. I did some quick research and learnt that architects use CAD software, which exports drawings in .dxf format. I went with QCAD, as it's free. After creating the drawing, I wrote a Python script that reads the .dxf file.<br/>

As this is a learning experience, this first program will just read the file's contents (lines and text). It doesn't necessarily interpret the drawing in the context of the entire building and it having different rooms.

## How it works
A .dxf file is a text based format that represents CAD drawings in a human readable way. The format has sections, of which the relevant one to the project are:
- HEADER (general info like units)
- ENTITIES (for drawing objects like lines, circles, texts)
- BLOCKS (reusable shapes)
- TABLES (style info)
<br/><br/>

Each entity (like a line or text) is made up of group codes
`0
LINE
8
LayerName
10
x1
20
y1
11
x2
21
y2`
This is a line from (x1, y1) to (x2, y2)

<br/><br/><br/><br/>
