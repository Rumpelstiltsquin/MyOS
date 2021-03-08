#!/usr/bin/python3
#encoding: utf-8


import sys, re, subprocess

if len(sys.argv) !=2:
    print("\n[!] Use: python3" + sys.argv[0] + " <IP_Address>\n")
    sys.exit(1)

def get_ttl(ip_address):
    proc = subprocess.Popen(["ping -c 1 %s" % ip_address, ""], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    out = out.split()
    out = out[12].decode('utf-8')
    ttl_value = re.findall(r"\d{1,3}",out)[0]
    return ttl_value

def get_os(ttl):
    ttl=int(ttl)

    if ttl >= 0 and ttl<=64:
        return "Linux"
    elif ttl >= 65 and ttl <= 128:
        return "Windows"
    else:
        return "No Founs :("

if __name__== '__main__':
    try:
        ip_address=sys.argv[1]

        ttl = get_ttl(ip_address)
        os_name = get_os(ttl)

        print ("%s (ttl -> %s): %s" % (ip_address, ttl, os_name))
    except:
        print ("[!] Enter a valid IP ")