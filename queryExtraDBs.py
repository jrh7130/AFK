from subprocess import check_output, check_call
from time import strftime, localtime
from checkExists import *
import sys

adb_path = r"C:\Android\platform-tools\adb"

def query_chrome_history():
    if check_chrome() == 1:
        return 1

    # Query number of entries
    query = r"\"select count(*) from urls\""
    cmd = adb_path + " shell \"sqlite3 data/data/com.android.chrome/app_chrome/Default/History " + query + "\""
    chm_count = check_output(cmd, shell=True).decode(sys.stdout.encoding)

    # Query page titles
    query = r"\"select title from urls\""
    cmd = adb_path + " shell \"sqlite3 data/data/com.android.chrome/app_chrome/Default/History " + query + "\""
    chrome = check_output(cmd, shell=True).decode('ascii',errors='ignore')
    chm_title = chrome.split('\n')

	# Query page URl
    query = r"\"select url from urls\""
    cmd = adb_path + " shell \"sqlite3 data/data/com.android.chrome/app_chrome/Default/History " + query + "\""
    chrome = check_output(cmd, shell=True).decode(sys.stdout.encoding)
    chm_urls = chrome.split('\n')

    # Query page access date
    query = r"\"select last_visit_time from urls\""
    cmd = adb_path + " shell \"sqlite3 data/data/com.android.chrome/app_chrome/Default/History " + query + "\""
    chrome = check_output(cmd, shell=True).decode(sys.stdout.encoding)
    chm_time = chrome.split('\n')
    for i in range(0, len(chm_time)-1):
        t_conv = chm_time[i][:10]
        chm_time[i] = strftime('%m-%d-%Y %H:%M:%S', localtime(int(t_conv)))

    chrome = {'count' : chm_count,
              'title' : chm_title,
              'url' : chm_urls,
              'last' : chm_time}

    return chrome

def query_chrome_downloads():
    if check_chrome() == 1:
        return 1

    # Query number of entries
    query = r"\"select count(*) from downloads\""
    cmd = adb_path + " shell \"sqlite3 data/data/com.android.chrome/app_chrome/Default/History " + query + "\""
    chm_count = check_output(cmd, shell=True).decode(sys.stdout.encoding)

    # Query page title
    query = r"\"select target_path from downloads\""
    cmd = adb_path + " shell \"sqlite3 data/data/com.android.chrome/app_chrome/Default/History " + query + "\""
    chrome = check_output(cmd, shell=True).decode('ascii',errors='ignore')
    chm_trgt = chrome.split('\n')

	# Query page URl
    query = r"\"select tab_url from downloads\""
    cmd = adb_path + " shell \"sqlite3 data/data/com.android.chrome/app_chrome/Default/History " + query + "\""
    chrome = check_output(cmd, shell=True).decode(sys.stdout.encoding)
    chm_url = chrome.split('\n')

    # Query download start
    query = r"\"select start_time from downloads\""
    cmd = adb_path + " shell \"sqlite3 data/data/com.android.chrome/app_chrome/Default/History " + query + "\""
    chrome = check_output(cmd, shell=True).decode(sys.stdout.encoding)
    chm_stime = chrome.split('\n')
    for i in range(0, len(chm_stime)-1):
        t_conv = chm_stime[i][:10]
        chm_stime[i] = strftime('%m-%d-%Y %H:%M:%S', localtime(int(t_conv)))

    # Query download end
    query = r"\"select end_time from downloads\""
    cmd = adb_path + " shell \"sqlite3 data/data/com.android.chrome/app_chrome/Default/History " + query + "\""
    chrome = check_output(cmd, shell=True).decode(sys.stdout.encoding)
    chm_etime = chrome.split('\n')
    for i in range(0, len(chm_etime)-1):
        t_conv = chm_etime[i][:10]
        chm_etime[i] = strftime('%m-%d-%Y %H:%M:%S', localtime(int(t_conv)))

    # Query download size
    query = r"\"select total_bytes from downloads\""
    cmd = adb_path + " shell \"sqlite3 data/data/com.android.chrome/app_chrome/Default/History " + query + "\""
    chrome = check_output(cmd, shell=True).decode(sys.stdout.encoding)
    chm_size = chrome.split('\n')

    chrome = {'count' : chm_count,
              'path' : chm_trgt,
              'url' : chm_url,
              'start' : chm_stime,
              'end' : chm_etime,
              'size' : chm_size}

    return chrome
