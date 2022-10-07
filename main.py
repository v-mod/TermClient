import os
import psutil
import socket
#import sched
import login
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
battery = psutil.sensors_battery()
def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)
def cmd_ui():
    try:
        while True:
            op=input('> ')
            if op == 'su':
                os.system('powershell C:/Users/vivaa/Onedrive/Desktop/Other/ssh.bat')
            elif op == 'sc':
                host=input('Host: ')
                username=input(host+' login: ')
                os.system('powershell ssh '+username+'@'+host)
            elif op == 'stu':
                print('powershell ssh pi@ultimate neofetch')
            elif op == 'ou':
                os.system('powershell wsl -d ubuntu')
            elif op == 'op':
                os.system('powershell')
            elif op == 'vo':
                print('Please select an option: SSH to Ultimate [SU], SSH to custom host [SC], View status of Ultimate [STU], Open Ubuntu [OU], Open Debian [OD], Open windows powershell [OP], Open Browse [OB], View these options again [VO], Start Shizuku [SS], Launch adb [LA], Screen mirror [SM], Bluestacks [BS].')
            elif op == 'lud':
                print('It is no longer recommended to launch Ubuntu Desktop as it interferes with Chrome OS Flex and requires a fresh install of ubuntu to fix. Due to this the feature has been disabled.')
#                os.system('powershell.exe wsl -e sudo python3 /desktop/start.py')
            elif op == 'ob':
                os.system(r'C:\Windows\py.exe "C:\Users\vivaa\Projects\python-utils\browser.py"')
            elif op == 'cros':
                print('It is now recomended to just boot straight from the ChromeOS Usb')
            elif op == 'ss':
                os.system('cd C:/Users/vivaa/Google/platform-tools && adb shell sh /storage/emulated/0/Android/data/moe.shizuku.privileged.api/start.sh ')
            elif op == 'la':
                os.system('cd C:/Users/vivaa/Google/platform-tools && cmd')
            elif op == 'sm':
                os.system('C:/Users/vivaa/Google/Scrcpy/scrcpy.exe')
            elif op == 'bs':
                os.system('"C:\Program Files\BlueStacks_nxt\HD-Player.exe" --instance Nougat64')
            elif op == 'discord':
                if login.login():
                    os.system(r'C:\Users\vivaa\AppData\Local\Discord\app-1.0.9006\Discord.exe')
            elif op == 'od':
                os.system('powershell wsl -d debian')
            elif op == '':
                continue
            else:
                os.system('powershell.exe "'+op+'"')
    except:
        cmd_ui()
print('Welcome')
print('')
print('Please select an option:  SSH to Ultimate [SU], SSH to custom host [SC], View status of Ultimate [STU], Open Ubuntu [OU], Open Debian [OD], Open powershell [OP], Open Browse [OB], View these options again [VO], Start Shizuku [SS], Launch adb [LA], Screen mirror [SM], Bluestacks [BS]')
print('')
print('Computer Status: ')
if battery.power_plugged:
    print("Charging: "+str(battery.percent)+"%")
else:
    print("Not Charging: "+str(battery.percent)+"%")
    print("Discharge time: ", secs2hours(int(battery.secsleft)))
print("Computer Name: "+hostname)
print("Computer IP Address: "+IPAddr)
if IPAddr == '172.30.64.1':
    print('Wifi Status: Not Connected')
else:
    print('Wifi Status: Connected')
print('')
print('© Vivaan Modi. All Rights Reserved.')
cmd_ui()
os.system('powershell pause')
