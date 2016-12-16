from subprocess import check_call
from time import strftime

def make_report_dirs():
    global history, acct, google
    timestamp = strftime("\%m%d%Y")
    rep_dir = "Reports" + timestamp
    history = rep_dir + '\History'
    acct = rep_dir + '\Account'
    google = rep_dir + '\Google'

    try:
        check_call('mkdir ' + google, shell=True)
    except:
        pass
    try:
        check_call('mkdir ' + acct, shell=True)
    except:
        pass
    try:
        check_call('mkdir ' + history, shell=True)
    except:
        return

def write_chrome_history(chrome):
    with open(google + '\chrome_history.txt', 'w') as f:
        if chrome == 1:
            f.write('No Chrome browser history found.')
        else:
            for i in range(0,int(chrome['count'])):
                f.write('Page Title:     ' + chrome['title'][i] + '\n')
                f.write('URL:            ' + chrome['url'][i] + '\n')
                f.write('Visited:        ' + chrome['last'][i] + '\n')
                f.write('\n')
    f.close()

def write_chrome_downloads(chrome):
    with open(google + '\chrome_downloads.txt', 'w') as f:
        if chrome == 1:
            f.write('No Chrome download history found.')
        else:
            for i in range(0,int(chrome['count'])):
                f.write('URL:            ' + chrome['url'][i] + '\n')
                f.write('Download Path:  ' + chrome['path'][i] + '\n')
                f.write('Download Size:  ' + chrome['size'][i] + '\n' )
                f.write('Start Time:     ' + chrome['start'][i] + '\n')
                f.write('End Time:       ' + chrome['end'][i] + '\n')
                f.write('\n')
    f.close()

def write_calls(calls):
    with open(history + '\call_history.txt', 'w') as f:
        if calls == 1:
            f.write('No call history found.')
        else:
            for i in range(0,int(calls['count'])):
                if '1' in calls['type'][i]:
                    f.write('Type:      Incoming\n')
                if '2' in calls['type'][i]:
                    f.write('Type:      Missed\n')
                if '3' in calls['type'][i]:
                    f.write('Type:      Outgoing\n')
                if len(calls['name'][i]) <= 2:
                    f.write('Name:      N/A\n')
                else:
                    f.write('Name:      ' + calls['name'][i] + '\n')
                f.write('Number:    ' + calls['num'][i] + '\n')
                f.write('Date/Time: ' + calls['time'][i] + '\n')
                f.write('Duration:  ' + calls['dur'][i] + 's\n')
                f.write('Location:  ' + calls['geo'][i] + ', ' + calls['ctry'][i] + '\n')
                f.write('\n')
    f.close()

def write_sms(sms):
    with open(history + '\sms_history.txt', 'w') as f:
        if sms == 1:
            f.write('No SMS history found.')
        else:
            for i in range(0,int(sms['count'])):
                if len(sms['name'][i]) <= 2:
                    f.write('Name:       N/A\n')
                else:
                    f.write('Name:       ' + sms['name'][i] + '\n')
                f.write('Number:     ' + sms['num'][i] + '\n')
                if len(sms['subj'][i]) <= 2:
                    pass
                else:
                    f.write('Subject:    ' + sms['subj'][i] + '\n')
                f.write('Body:       ' + sms['body'][i] + '\n')
                f.write('Date/Time:  ' + sms['time'][i] + '\n')
                f.write('\n')
        f.close()

def write_browser(brow):
    with open(history + r'\browser_history.txt', 'w') as f:
        if brow == 1:
            f.write('No Android browser history found.')
        else:
            for i in range(0,int(brow['count'])):
                f.write('Page Title:     ' + brow['title'][i] + '\n')
                f.write('URL:            ' + brow['url'][i] + '\n')
                f.write('Visited:        ' + brow['last'][i] + '\n')
                f.write('\n')
    f.close()

def write_contacts(con):
    with open(acct + '\contact_list.txt', 'w') as f:
        if con == 1:
            f.write('No contacts found.')
        else:
            for i in range(0,int(con['count'])):
                f.write('Name:    ' + con['name'][i])
                f.write('Number:  ' + con['num'][i])
                f.write('\n\n')
    f.close()
