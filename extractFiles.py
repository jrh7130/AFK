from subprocess import check_call, check_output
from checkExists import *
from time import strftime
import sys

adb_path = r"C:\Android\platform-tools\adb"

working_dir = check_output("cd", shell=True).decode(sys.stdout.encoding).strip()
timestamp = strftime("\%m%d%Y")
rep_dir = working_dir + "\Reports" + timestamp + "\Storage"
try:
    check_call('mkdir ' + rep_dir + "\Local", shell=True)
except:
    pass
try:
    check_call('mkdir ' + rep_dir + "\SDCard", shell=True)
except:
    pass

def extract_downloads():
    dir_type = check_downloads()
    if dir_type == 1:
        down = "/storage/emulated/0/Download/"
        check_call(adb_path + " pull " + down + ' ' + rep_dir + '\Local', shell=True)
        down = "/storage/emulated/0/Pictures/"
        check_call(adb_path + " pull " + down + ' ' + rep_dir + '\Local', shell=True)
        down = "/storage/emulated/0/DCIM/"
        check_call(adb_path + " pull " + down + ' ' + rep_dir + '\Local', shell=True)
    elif dir_type == 2:
        down = "/storage/emulated/legacy/Download/"
        check_call(adb_path + " pull " + down + ' ' + rep_dir + '\Local', shell=True)
        down = "/storage/emulated/legacy/Pictures/"
        check_call(adb_path + " pull " + down + ' ' + rep_dir + '\Local', shell=True)
        down = "/storage/emulated/legacy/DCIM/"
        check_call(adb_path + " pull " + down + ' ' + rep_dir + '\Local', shell=True)

def extract_sdcard_downloads():
    if check_sdcard() == 1:
        return 1
    else:
        down = "/storage/sdcard0/Download/"
        check_call(adb_path + " pull " + down + ' ' + rep_dir + '\SDCard', shell=True)
        down = "/storage/sdcard0/DCIM/"
        check_call(adb_path + " pull " + down + ' ' + rep_dir + '\SDCard', shell=True)
        down = "/storage/sdcard0/Pictures/"
        check_call(adb_path + " pull " + down + ' ' + rep_dir + '\SDCard', shell=True)
