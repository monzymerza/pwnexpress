#########
#
#########
import time
import random
import sys
EPS = 1

def make_timestamp():
    timestamp = time.strftime("%b %d %H:%M:%S")
    return timestamp

def make_server_name():
    names = ['polonus9', 'europa', 'emojin']
    server_name = names[random.randint(0,len(names)-1)]
    return server_name


def make_mac_addr():
    '''http://kennethreitz.org/generate-a-random-mac-address-in-python/'''
    """Returns a completely random Mac Address"""
    mac = [0x00, 0x16, 0x3e, random.randint(0x00, 0x7f), 
       random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
    mac_addr = ':'.join(map(lambda x: "%02x" % x, mac))    
    return mac_addr

def make_device_type():
    device_type_list = ['Wireless Client', 'Wireless Client','Wireless Client','Wireless Client','Wireless Client','Wireless AP']
    device_type = device_type_list[random.randint(0,len(device_type_list)-1)]
    return device_type

def make_device_model():
    device_model_list = ['iPhone 5', 'Samsung Galaxy', 'Blackberry Z', 'Motorola Droid X']
    device_model = device_model_list[random.randint(0,len(device_model_list)-1)]
    return device_model

def make_device_name():
    device_name_list = ['my', 'security', 'fav', 'phone', 'work', 'fan','test','heavy','pwn', 'star','black','white','foo','kung','food']
    device_name = str(device_name_list[random.randint(0,len(device_name_list)-1)]) + " " + str(device_name_list[random.randint(0,len(device_name_list)-1)])
    return device_name
def make_ssid():
    ssid_list = ['B8:17:C2:00:FB:EB', '(not associated)', '(not associated)','iHub', 'Auth_guest', '(not associated)','(not associated)','COVE', '(not associated)','Houses of the Holy', 'Megatron']
    ssid = str(ssid_list[random.randint(0,len(ssid_list)-1)])
    return ssid
def make_probe():
    probe_list = ['', 'RLSS', 'Extension','','','']
    probe = str(probe_list[random.randint(0,len(probe_list)-1)])
    return probe
def make_encryption():
    enc_list = ['WPA2WPA', 'WPA', 'OPN', '', '', '', 'WPA2']
    encryption = str(enc_list[random.randint(0,len(enc_list)-1)])
    return encryption

def make_wirelesslog():
    wirelesslog = make_timestamp() + " " + make_server_name() + \
        " " + 'logger' + ": " + time.strftime("%Y-%m-%d %H:%M:%S") + \
        ";" + make_device_type() + ";" + make_mac_addr() + \
        ";" + make_ssid() + ";" + make_encryption() + \
        ";" + make_probe() 
    return wirelesslog

while True:
    print make_wirelesslog()
    time.sleep (1/EPS)
