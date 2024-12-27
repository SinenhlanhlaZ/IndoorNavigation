# IndoorNavigation

A side project I was curious about and how it can be implemented. It's going to be a learning curve, so I'll be implementing new things as I learn them, until it becomes a complete indoor navigation system!

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
   implementation ("androidx.appcompat:appcompat:1.6.1")
   implementation ("androidx.core:core-ktx:1.12.0")
6. Build and run the app on a physical device (not an emulator).

#28 December 2024
## Feature
- measure the distance from the device to the connected Wi-Fi access point using RSSI (Received Signal Strength Indicator).
- update the distance in real-time (every 500ms).

## How it works
1. The distance is calculated using the **log-distance path loss model**:
<br/><br/>![image](https://github.com/user-attachments/assets/ea6fa568-a072-441d-8c17-bab733af216b)<br/>
- **RSSI**: Signal strength in dBm (retrieved programmatically).
- **RSSI_ref**: Signal strength at 1 meter from the access point (measured empirically).
- **n**: Path-loss exponent (varies depending on the environment, typically 2-4).

2. The app fetches the RSSI value of the connected Wi-Fi access point and updates the calculated distance every 500 milliseconds.

