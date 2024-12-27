# IndoorNavigation

IndoorNavigation is a small Android project that demonstrates the ability to measure the distance between a device and a Wi-Fi access point. This is the initial step toward building an indoor navigation system, which can be used to determine the user's position within an indoor environment.

## Features

- Measures the distance from the device to the connected Wi-Fi access point using RSSI (Received Signal Strength Indicator).
- Dynamically updates the distance in real-time (every 500ms).
- Provides a foundation for implementing an indoor navigation system.

## How It Works

1. The app calculates the distance using the **log-distance path loss model**:
![image](https://github.com/user-attachments/assets/a50418a6-483b-4ee6-8eea-144d366c194a)
- **RSSI**: Signal strength in dBm (retrieved programmatically).
- **RSSI_ref**: Signal strength at 1 meter from the access point (measured empirically).
- **n**: Path-loss exponent (varies depending on the environment, typically 2-4).

2. The app fetches the RSSI value of the connected Wi-Fi access point and updates the calculated distance every 500 milliseconds.

## Prerequisites

- Android Studio (latest version recommended).
- An Android device with Wi-Fi capabilities.
- A Wi-Fi access point for testing.

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/IndoorNavigation.git
cd IndoorNavigation
