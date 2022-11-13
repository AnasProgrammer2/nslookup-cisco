#!/usr/bin/python3
__author__ = "Anas Andullkarim"
__copyright__ = "Copyright 2022, NBTEL"
__license__ = "GPL"
__version__ = "1.2"
__maintainer__ = "NBTEL"
__email__ = "anas.abdullkarim@gmail.com"
__status__ = "Production"
import argparse
import socket
import textwrap
import time
import configparser
import time
import datetime
import configparser
import io
import os
import requests
import paramiko
from operator import truediv
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#text = input("enter path of file text: ") 

#check if ip is ipv4
def validIP(address):
    parts = address.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True

def color_text(text, rgb):
    r, g, b = rgb
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

class rgb():
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    # and so on ...

devloper_info ="\n --------------- \n by Anas Abdullkarim \n Nour Al-BADIYA ISP. \n anas.abdullkarim@gmail.com \n";
help=" Router Supported "+ __version__+" cisco_xr , cisco_xe ,cisco_nexus, huawei , mikrotik \n how to use : \n ./dns-acl --config config.ini  --apply_on_host  \n  "
parser = argparse.ArgumentParser(
      prog='Domain to ACL by',
      formatter_class=argparse.RawDescriptionHelpFormatter,
      epilog=textwrap.dedent(color_text("Software for domain dns reslove a list to ACL of multi-vendor Router and Switch \n just select  select OS and ACL name "+help + devloper_info, rgb.GREEN)))

#parser.add_argument('--os', dest='os', type=str, help='Select Vander OS [cisco_xr,cisco_xe,cisco_nexus,huawei,mikrotik]')
#parser.add_argument('--acl_name', dest='acl_name', type=str, help='enter Access-list name')
#parser.add_argument('--acl_type', dest='acl_type', help='enter Access-list type permit | DENY')
parser.add_argument('--config', dest='config',  type=str, help='choose file of config.ini')
parser.add_argument('--apply_on_host', dest='apply_on_host', action="store_false", help='that will appply ACL to router dirclty though SSH')


args = parser.parse_args()

e = datetime.datetime.now()    
current_time = (e.strftime("%I:%M:%S %p"))

print(color_text("Automation start at :{}".format(current_time),rgb.RED))
time.sleep(0.3)
os_List = ['cisco_xr','cisco_xe','cisco_nexus','huawei','mikrotik']

osHost ="";
acl_name="";
acl_type="";
config_file="";


apply_on_host=0;
#if args.os in os_List:
# osHost=args.os
#else:
# print (color_text("ERROR #1 : Please select only OS supported [cisco_xr , cisco_xe , cisco_nexus , huawei , mikrotik ] \n example :- ./dnsacl --OS ios_xr  --ACL BLOCK ", rgb.RED))
# exit()
 
#if args.acl_name != None:
# acl_name=args.acl_name
#else:
# print (color_text("ERROR #2: Please select ACL name , for exmaple --acl_name TEST acl_type permit \n example :- ./dnsacl --OS ios_xr  --acl_name BLOCK acl_type deny", rgb.RED))
# exit()

 
#if args.acl_type != None:
# acl_type=args.acl_type
#else:
# print (color_text("ERROR #3: Please select ACL type Permit | Deny , for exmaple --acl_name TEST acl_type permit \n example :- ./dnsacl --OS ios_xr  --acl_name BLOCK acl_type deny", rgb.RED))
# exit()

if args.apply_on_host == True  :
 apply_on_host=0
else:
 apply_on_host=1

if args.config != None:
 config_file=args.config
else:
 print (color_text("ERROR #4: please select config file ", rgb.RED))
 exit()



config = configparser.ConfigParser()
config.read(config_file)

ip_addr = config.get('authorization', 'ipaddress')
username = config.get('authorization', 'username')
password = config.get('authorization', 'password')
acl_name = config.get('authorization', 'acl_name')
acl_type = config.get('authorization', 'acl_type')
osHost = config.get('authorization', 'osHost')
output_folder_name = config.get('authorization', 'output_folder_name')
temp_file=output_folder_name+ "/" + osHost +"_"+ip_addr+".txt"

if not os.path.exists(output_folder_name):
    # if the demo_folder directory is not present 
    # then create it.
    os.makedirs(output_folder_name)


time.sleep(1)
print(color_text("Select OS: " + osHost , rgb.GREEN))
print(color_text("ACL Name: " + acl_name , rgb.GREEN))
print(color_text("ACL Type: " + acl_type , rgb.GREEN))

time.sleep(1)

ip_list = [];
#file1 = open(text, 'r')
file1 = open("domain.txt", 'r')
Lines = file1.readlines()
count = 0
for domain in Lines:
 count += 1
 #print("Line{}: {}".format(count, domain.strip()))
 domain =domain.strip();
 try:
  ais = socket.getaddrinfo(domain,0,0,0,0)
 except socket.gaierror as e:
        continue

    
 for result in ais:
   if validIP(result[-1][0]):
    ip_list.append(result[-1][0])
    #print("permit ipv4 host {} any".format( result[-1][0]))
 
 ip_list = list(set(ip_list))
  

f = open(temp_file, 'w')
count =1
if osHost==os_List[0]: #cisco_xr 
 f.writelines("ipv4 access-list "+ acl_name +"\n" )
 print(color_text("ipv4 access-list "+ acl_name ,rgb.YELLOW))
 for host in ip_list: 
    f.writelines("%s\n" % "{} {} ipv4 host {} any".format(count,acl_type,host))
    print(color_text("{} {} ipv4 host {} any".format(count,acl_type,host),rgb.YELLOW))
    count+=1
 if acl_type=="deny":
    f.writelines("{} permit ipv4 any any".format(count ))
    print(color_text("{} permit ipv4 any any".format(count ),rgb.YELLOW))

if osHost==os_List[1]: #cisco_xe
 print(color_text("ip access-list extended "+ acl_name ,rgb.YELLOW))
 f.writelines("ip access-list "+ acl_name )
 for host in ip_list:
    f.writelines("\n {} {} ip host {} any".format(count,acl_type,host))
    print(color_text("{} {} ip host {} any".format(count,acl_type,host),rgb.YELLOW))
    count+=1
 if acl_type=="deny":
    f.writelines("\n {} permit ip any any".format(count ))
    print(color_text("{} permit ip any any".format(count ),rgb.YELLOW))

    
if osHost==os_List[2]: #cisco_nexus 
 f.writelines("ip access-list "+ acl_name )
 print(color_text("ip access-list "+ acl_name ,rgb.YELLOW))
 for host in ip_list:
    f.writelines("\n {} {} ip host {} any".format(count,acl_type,host))
    print(color_text("{} {} ip host {} any".format(count,acl_type,host),rgb.YELLOW))
    count+=1
 if acl_type=="deny" or "DENY" :
    f.writelines("\n {} permit ip any any".format(count))
    print(color_text("{} permit ip any any".format(count ),rgb.YELLOW))

if osHost==os_List[3]: #huawei 
 f.writelines("acl number "+ acl_name)
 print(color_text("acl number "+ acl_name ,rgb.YELLOW))
 for host in ip_list:
    f.writelines("\n rule {} {} ip soruce {} ".format(count,acl_type,host))
    print(color_text("rule {} {} ip soruce {} ".format(count,acl_type,host),rgb.YELLOW))
    count+=1
    
if osHost==os_List[4]: #mikrotik 
 for host in ip_list:
    f.writelines("\n ip firewall address-list add address={} list={}".format(host,acl_name))
    print(" ip firewall address-list add address={} list={}".format(host,acl_name))

f.close();

print(color_text("------------------------------------ ",rgb.RED))

if apply_on_host==0: 
 getConfrim=0
 print(color_text("for apply on Device , please use --apply_on_host \n example : pydns.py --config config.ini  --apply_on_host ".format(ip_addr),rgb.RED))
else:
 getConfrim=1
    


if getConfrim ==1:
     file2 = open(temp_file, 'r')
     time.sleep(0.5)
     remote_conn_pre = paramiko.SSHClient()
     remote_conn_pre
     remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
     remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False,timeout=5)
     print("API connection established to Router " + ip_addr)
     remote_conn = remote_conn_pre.invoke_shell()
     Lines = file2.readlines()
     if osHost =='cisco_xr' or 'cisco_se' or 'cisco_nexus' :
      remote_conn.send('configure terminal \n') 
      time.sleep(3)
     
     
     if osHost =='huawei' :
      remote_conn.send('sys \n') 
      time.sleep(0.3)
     for configline in Lines: 
      print(configline)
      remote_conn.send(configline)
      remote_conn.send(' \n') 
      time.sleep(2)


     if osHost =='cisco_xr':
      remote_conn.send('commit \n') 
      time.sleep(5)
      
     output = remote_conn.recv(5000)
     print(output.decode("ascii").strip("\n"))
     time.sleep(5)
     remote_conn.close();
     print("apply ACL to rotuer has successful")
 
print(color_text("------------------------------------ ",rgb.RED))
