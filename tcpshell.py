import socket
import gc
from ucryptolib import aes
from random import randint
import time
key=""
splt = "blackshell"


def aes_decrypt(ciph, msg):
    return ciph.decrypt(msg)

def aes_encrypt(ciph, msg):
    padded = msg + " " * (16 - len(msg) % 16)
    encrypted = ciph.encrypt(padded)
    return encrypted

def aes_genkey():

    key = ''
    for _ in range(32):
        value = randint(0, 9)
        key +=str(value)
        print(key)

		#key = b'[Secret Wokwi key with 256 bits]'
		#iv = key#uos.urandom(16)

    return key

def gencipher(key):
    key = key.replace('\n', '')
    iv = bytes.fromhex(key)
    cipher = aes(key, 2, iv)
    return (key,iv,cipher)



def tcpshell(iface,pas):

    addr = socket.getaddrinfo('0.0.0.0', 33633)[0][-1]
    html=""
    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    print('listening on', addr)


    while True:
        try:
            cl, addr = s.accept()
            print('client connected from', addr)
            cl_file = cl.makefile('rwb', 0)
        except:
            pass

        while True:

            try:
                line = cl_file.recv(500)
                if not line or line == b'\r\n':
                    break

                key2,iv2,ciphe = gencipher(pas)
            except:
                pass
                break
            try:
                print(line)
                dec = aes_decrypt(ciphe,line)
                print(dec)
            except:
                pass
                break

            try:
                cmd = str(dec,"utf8").split(splt)[1]
                loc = {}
                key3,iv3,ciph3 = gencipher(pas)
                rshell= exec(cmd,globals(),loc)
                print(rshell)
                if len(loc)==0:
                    loc["result"]="None"

                cl.send(aes_encrypt(ciph3, str(loc)))
            except:
                pass
                break

        try:
            cl.close()
        except:
            pass


def add_device(devicename,ip,key):

    file = open ("data/devices", "w")
    file.append(devicename+" "+ip+" "+key+"\n")
    file.close()

def list():

    file = open("data/devices", "r")

    file.read()

    file.close()
    return file 

def blackcmd(ip,cmd,pas):

    addr = socket.getaddrinfo(ip, 33633)[0][-1]
    s = socket.socket()
    s.connect(addr)

    enc = ""
    key,iv,ciph = gencipher(pas)

    enc = aes_encrypt(ciph,"-"+splt+""+cmd)

    print (enc)

    s.send(enc)

    #time.sleep(1)
    while True:
        dat = s.recv(800)
        if dat:
            key4,iv4,ciph4 = gencipher(pas)
            dec = aes_decrypt(ciph4, dat)
            print(dec)
            s.close()
            break

        else:
            break

    s.close()




                                 
