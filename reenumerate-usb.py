import os
import subprocess
import time


USB_VEN_ID = '0x09da'
USB_DEV_ID = '0x2268'


def is_runnning(app):
    count = int(subprocess.check_output(["osascript",
                                         "-e", "tell application \"System Events\"",
                                         "-e", "count (every process whose name is \"" + app + "\")",
                                         "-e", "end tell"]).strip())
    return count > 0


def reenumerate_usb(vendor_id, dev_id):
    cmd = 'open -a "/Applications/Utilities/USB Prober.app/Contents/Resources/reenumerate" --args -v '
    cmd += vendor_id + ',' + dev_id
    os.system(cmd)


if __name__ == '__main__':
    while 1:
        if is_runnning('Karabiner-Menu'):
            time.sleep(5)
            reenumerate_usb(USB_VEN_ID, USB_DEV_ID)
            exit()
        time.sleep(1)
