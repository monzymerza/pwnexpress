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

def make_log_type():
    log_type = 'bluelog'
    return log_type

def make_mac_addr():
    '''http://kennethreitz.org/generate-a-random-mac-address-in-python/'''
    """Returns a completely random Mac Address"""
    mac = [0x00, 0x16, 0x3e, random.randint(0x00, 0x7f), 
       random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
    mac_addr = ':'.join(map(lambda x: "%02x" % x, mac))    
    return mac_addr

def make_device_type():
    device_type_list = ['(VOID)','Smart Phone', 'Handheld Computer', 'Tablet PC', 'Laptop']
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

while True:
    output = make_timestamp() + " " + make_server_name() + \
          " " + make_log_type() + ": " + make_mac_addr() + \
          "," + make_device_type() + "," + make_device_model() + \
          "," + make_device_name()
    print output
    time.sleep(1/EPS)
