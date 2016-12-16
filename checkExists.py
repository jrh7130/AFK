from subprocess import check_output, check_call
from time import sleep
import sys

adb_path = r"C:\Android\platform-tools\adb"

def check_devices(timeout=10):
	"""
		Waits for a valid device to connect to adb

		Args:
			timeout - waits 60s checking for devices before exiting program if none found

		Returns:
			None
	"""
	if timeout == 0:
		print("\nNo devices found. Terminating program.")
		exit()
	chk = check_output(adb_path + " devices", shell=True).decode(sys.stdout.encoding)
	dev = chk.split('\n')
	if len(dev) <= 3:
		print("Waiting for device connection...")
		sleep(6)
		check_devices(timeout-1)
	else:
		print(dev[1].strip() + ' connected, running analysis...\n')

	return 0

def check_contacts():
    """
		Checks to see if call data is present on the phone

		Args:
			None

		Returns:
			1 - Directory not found
			0 - Directory found
	"""
    chk = check_output(adb_path + " shell ls data/data/com.android.providers.contacts/databases/contacts2.db", shell=True).decode(sys.stdout.encoding)
    dev = chk.split('\n')
    for i in dev:
        if "No such file" in i:
            return 1

    return 0

def check_sms():
    """
		Checks to see if SMS data is present on the phone

		Args:
			None

		Returns:
			1 - Directory not found
			0 - Directory found
	"""
    chk = check_output(adb_path + " shell ls data/data/com.android.providers.telephony/databases/mmssms.db", shell=True).decode(sys.stdout.encoding)
    dev = chk.split('\n')
    for i in dev:
        if "No such file" in i:
            return 1

    return 0

def check_browser():
    """
		Checks to see if Android browser data is present on the phone

		Args:
			None

		Returns:
			1 - Directory not found
			0 - Directory found
	"""
    chk = check_output(adb_path + " shell ls data/data/com.android.browser/databases/browser2.db", shell=True).decode(sys.stdout.encoding)
    dev = chk.split('\n')
    for i in dev:
        if "No such file" in i:
            return 1

    return 0

def check_chrome():
    """
		Checks to see if Chrome data is present on the phone

		Args:
			None

		Returns:
			1 - Directory not found
			0 - Directory found
	"""
    chk = check_output(adb_path + " shell ls data/data/com.android.chrome/app_chrome/Default", shell=True).decode(sys.stdout.encoding)
    dev = chk.split('\n')
    for i in dev:
        if "No such file" in i:
            return 1

    return 0

def check_gmail():
    """
		Waits for a valid device to connect to adb

		Args:
			timeout - waits 60s checking for devices before exiting program if none found

		Returns:
			0 - Directory not found
			1 - Directory found
	"""
    chk = check_output(adb_path + " shell ls data/data/com.google.android.gm/databases/mailstore*", shell=True).decode(sys.stdout.encoding)
    dev = chk.split('\n')
    for i in dev:
        if "No such file" in i:
            return 1

    return 0

def check_downloads():
	"""
		Waits for a valid device to connect to adb

		Args:
			timeout - waits 60s checking for devices before exiting program if none found

		Returns:
			0 - Directory not found
			1 - Directory is /0/Download
			2 - Directory is /legacy/Download
	"""
	chk = check_output(adb_path + " shell ls /storage/emulated/legacy/Download", shell=True).decode(sys.stdout.encoding)
	dev = chk.split('\n')
	chk2 = check_output(adb_path + " shell ls /storage/emulated/0/Download", shell=True).decode(sys.stdout.encoding)
	dev2 = chk2.split('\n')
	x = 0
	for i in dev:
	    if "No such file" in i:
	        x = 1
	for i in dev2:
		if "No such file" in i:
			x = 2

	return x

def check_sdcard():
	chk = check_output(adb_path + " shell ls /storage/sdcard0", shell=True).decode(sys.stdout.encoding)
	dev = chk.split('\n')
	for i in dev:
		if "No such file" in i:
			return 1

	return 0
