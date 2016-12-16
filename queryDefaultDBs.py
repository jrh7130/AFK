from checkExists import *
from subprocess import check_output, check_call
from time import strftime, localtime
import sys

adb_path = r"C:\Android\platform-tools\adb"

def query_contacts():

	if check_contacts() == 1:
		return 1

	# Query contact count
	query = r"\"select count(*) from contacts\""
	cmd = adb_path + " shell \"sqlite3 data/data/com.android.providers.contacts/databases/contacts2.db " + query + "\""
	con_count = check_output(cmd, shell=True).decode(sys.stdout.encoding)

	query = r"\"select name_raw_contact_id from contacts\""
	cmd = adb_path + " shell \"sqlite3 data/data/com.android.providers.contacts/databases/contacts2.db " + query + "\""
	con = check_output(cmd, shell=True).decode(sys.stdout.encoding)
	con_raw_id = con.split('\n')

	# Query numbers based on raw contact ID
	con_num = []
	for i in range(0, len(con_raw_id)-1):
		query = r"\"select normalized_number from phone_lookup where raw_contact_id = "
		query = query + con_raw_id[i].strip() + r"\""
		cmd = adb_path + " shell \"sqlite3 data/data/com.android.providers.contacts/databases/contacts2.db " + query + "\""
		con = check_output(cmd, shell=True).decode(sys.stdout.encoding)
		con = con.split('\n')
		con_num.append(con[0])

	# Query names based on raw contact ID
	con_name = []
	for i in range(0, len(con_raw_id)-1):
		query = r"\"select display_name from raw_contacts where _id = "
		query = query + con_raw_id[i].strip() + r"\""
		cmd = adb_path + " shell \"sqlite3 data/data/com.android.providers.contacts/databases/contacts2.db " + query + "\""
		con = check_output(cmd, shell=True).decode('ascii',errors='ignore')
		con_name.append(con)

	con = {'count' : con_count,
		   'num' : con_num,
		   'name' : con_name}

	return con

def query_calls():
	"""
		Queries the contacts2.db file for stored calls and prints to a report file

		Args:
			None

		Returns:
			calls - a dictionary containing lists of sql output
	"""
	if check_contacts() == 1:
		return 1

	# Query call count
	query = r"\"select count(*) from calls\""
	cmd = adb_path + " shell \"sqlite3 data/data/com.android.providers.contacts/databases/contacts2.db " + query + "\""
	call_count = check_output(cmd, shell=True).decode(sys.stdout.encoding)

	# Query contact name
	query = r"\"select name from calls\""
	cmd = adb_path + " shell \"sqlite3 data/data/com.android.providers.contacts/databases/contacts2.db " + query + "\""
	calls = check_output(cmd, shell=True).decode('ascii',errors='ignore')
	call_name = calls.split('\n')

	# Query contact number
	query = r"\"select formatted_number from calls\""
	cmd = adb_path + " shell \"sqlite3 data/data/com.android.providers.contacts/databases/contacts2.db " + query + "\""
	calls = check_output(cmd, shell=True).decode(sys.stdout.encoding)
	call_num = calls.split('\n')

	# Query call time
	query = r"\"select date from calls\""
	cmd = adb_path + " shell \"sqlite3 data/data/com.android.providers.contacts/databases/contacts2.db " + query + "\""
	calls = check_output(cmd, shell=True).decode(sys.stdout.encoding)
	call_time = calls.split('\n')
	# Reformat time to Date Time
	for i in range(0, len(call_time)-1):
		t_conv = call_time[i][:10]
		call_time[i] = strftime('%m-%d-%Y %H:%M:%S', localtime(int(t_conv)))

	# Query call duration
	query = r"\"select duration from calls\""
	cmd = adb_path + " shell \"sqlite3 data/data/com.android.providers.contacts/databases/contacts2.db " + query + "\""
	calls = check_output(cmd, shell=True).decode(sys.stdout.encoding)
	call_dur = calls.split('\n')

	# Query caller location
	query = r"\"select geocoded_location from calls\""
	cmd = adb_path + " shell \"sqlite3 data/data/com.android.providers.contacts/databases/contacts2.db " + query + "\""
	calls = check_output(cmd, shell=True).decode('ascii',errors='ignore')
	call_geo = calls.split('\n')

	# Query caller country
	query = r"\"select countryiso from calls\""
	cmd = adb_path + " shell \"sqlite3 data/data/com.android.providers.contacts/databases/contacts2.db " + query + "\""
	calls = check_output(cmd, shell=True).decode('ascii',errors='ignore')
	call_ctry = calls.split('\n')

	# Query call type
	# 1 = incoming, 2 = missed, 3 = outgoing
	query = r"\"select type from calls\""
	cmd = adb_path + " shell \"sqlite3 data/data/com.android.providers.contacts/databases/contacts2.db " + query + "\""
	calls = check_output(cmd, shell=True).decode(sys.stdout.encoding)
	call_type = calls.split('\n')

	calls = {'count' : call_count,
			 'name' : call_name,
			 'num' : call_num,
			 'time' : call_time,
			 'dur' : call_dur,
			 'geo' : call_geo,
			 'ctry' : call_ctry,
			 'type' : call_type}

	return calls

def query_sms():
	"""
		Queries the mmssms.db file for stored text messages and prints to a report file

		Args:
			None

		Returns:
			sms - a dictionary containing lists of sql output
	"""
	if check_sms() == 1:
	    return 1

	# Query sms count
	query = r"\"select count(*) from sms\""
	cmd = adb_path + " shell \"sqlite3 data/data/com.android.providers.telephony/databases/mmssms.db " + query + "\""
	sms_count = check_output(cmd, shell=True).decode(sys.stdout.encoding)

	# Query contact name
	query = r"\"select person from sms\""
	cmd = adb_path + " shell \"sqlite3 data/data/com.android.providers.telephony/databases/mmssms.db " + query + "\""
	sms = check_output(cmd, shell=True).decode('ascii',errors='ignore')
	sms_name = sms.split('\n')

	# Query contact number
	query = r"\"select address from sms\""
	cmd = adb_path + " shell \"sqlite3 data/data/com.android.providers.telephony/databases/mmssms.db " + query + "\""
	sms = check_output(cmd, shell=True).decode(sys.stdout.encoding)
	sms_num = sms.split('\n')

	# Query message subject
	query = r"\"select subject from sms\""
	cmd = adb_path + " shell \"sqlite3 data/data/com.android.providers.telephony/databases/mmssms.db " + query + "\""
	sms = check_output(cmd, shell=True).decode('ascii',errors='ignore')
	sms_subj = sms.split('\n')

	# Query message body
	query = r"\"select body from sms\""
	cmd = adb_path + " shell \"sqlite3 data/data/com.android.providers.telephony/databases/mmssms.db " + query + "\""
	sms = check_output(cmd, shell=True).decode('ascii',errors='ignore')
	sms_body = sms.split('\n')

	# Query message time
	query = r"\"select date from sms\""
	cmd = adb_path + " shell \"sqlite3 data/data/com.android.providers.telephony/databases/mmssms.db " + query + "\""
	sms = check_output(cmd, shell=True).decode(sys.stdout.encoding)
	sms_time = sms.split('\n')
	for i in range(0, len(sms_time)-1):
		t_conv = sms_time[i][:10]
		sms_time[i] = strftime('%m-%d-%Y %H:%M:%S', localtime(int(t_conv)))

	sms = {'count' : sms_count,
		   'name' : sms_name,
		   'num' : sms_num,
		   'subj' : sms_subj,
		   'body' : sms_body,
		   'time' : sms_time}

	return sms

def query_browser():
	"""
		Queries the browsser2.db file for default browser history

		Args:
			None

		Returns:
			brow - a dictionary containing lists of sql output
	"""
	if check_browser() == 1:
		return 1

	# Query number of browser entries
	query = r"\"select count(*) from history\""
	cmd = adb_path + " shell \"sqlite3 data/data/com.android.browser/databases/browser2.db " + query + "\""
	brow_count = check_output(cmd, shell=True).decode(sys.stdout.encoding)

	# Query page title
	query = r"\"select title from history\""
	cmd = adb_path + " shell \"sqlite3 data/data/com.android.browser/databases/browser2.db " + query + "\""
	brow = check_output(cmd, shell=True).decode(sys.stdout.encoding)
	brow_title = brow.split('\n')

	# Query page URl
	query = r"\"select url from history\""
	cmd = adb_path + " shell \"sqlite3 data/data/com.android.browser/databases/browser2.db " + query + "\""
	brow = check_output(cmd, shell=True).decode(sys.stdout.encoding)
	brow_url = brow.split('\n')

	# Query most recent date accessed
	query = r"\"select date from history\""
	cmd = adb_path + " shell \"sqlite3 data/data/com.android.browser/databases/browser2.db " + query + "\""
	brow = check_output(cmd, shell=True).decode(sys.stdout.encoding)
	brow_last = brow.split('\n')
	for i in range(0, len(brow_last)-1):
		t_conv = brow_last[i][:10]
		brow_last[i] = strftime('%m-%d-%Y %H:%M:%S', localtime(int(t_conv)))

	brow = {'count' : brow_count,
			'title' : brow_title,
			'url' : brow_url,
			'last' : brow_last}

	return brow
