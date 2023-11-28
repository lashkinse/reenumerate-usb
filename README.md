# Troubleshooting Keyboard Disconnection Issue on Mac After Login

If you are experiencing issues with your keyboard disconnecting on your Mac after login, you can use the following
script to reset the selected USB device. To successfully execute this script, make sure that Karabiner is already
installed on your system, as it is required for the proper functioning of this script.

This script restarts the selected USB device specified in the settings, thereby resolving the problem of keyboard
disconnection after login.

## Installation:

Install Karabiner if not already installed.

Install USB Prober in the folder

```apps/Utils/```

Place the files reenumerate-usb.plist and reenumerate-usb.py in the folder

```~/Library/LaunchAgents```

## Configuration and Run:

Modify the ID of your hardware in the file reenumerate-usb.py:

```USB_VEN_ID = '0x09da'```

```USB_DEV_ID = '0x2268'```

Change "user" to your username in the file reenumerate-usb.plist:

```/Users/user/Library/LaunchAgents/reenumerate-usb.py```

Verify the correctness of the settings by running the script with the command:

```python3 reenumerate-usb.py```