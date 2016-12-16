#
# (A)ndroid (F)orensics (K)it
# Python 3.5 Android Forensics
# Author: Jacob R Hooker
#

from extractFiles import *
from checkExists import *
from queryDefaultDBs import *
from queryExtraDBs import *
from writeReports import *

#def pull_gmail():
#	query = r"\"select * from messages\""
#	cmd = adb_path + " shell \"sqlite3 data/data/com.google.android.gm/databases/mailstore.jacobrhooker@gmail.com.db " + query + "\""
#	mail = check_output(cmd, shell=True).decode('ascii',errors='ignore')
#	return mail

#def disable_pattern():
#	print("Disabling pattern lock, reboot device to take effect")
#	check_call("adb shell \"rm data/system/gesture.key\"", shell=True)

def run_default():
	check_devices()
	make_report_dirs()
	write_calls(query_calls())
	write_sms(query_sms())
	write_browser(query_browser())
	write_contacts(query_contacts())
	write_chrome_history(query_chrome_history())
	write_chrome_downloads(query_chrome_downloads())
	extract_downloads()
	extract_sdcard_downloads()
	return

if __name__ == '__main__':
	print("----------(A)ndroid (F)orensics (K)it----------")
	run_default()
	exit()
