import time
import socket
import textwrap
import argparse

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
help="\n how to use : \n ./dnsacl --os cisco_xr  --acl_name BLOCK acl_type deny \n ./dnsacl --OS huawei  --acl_name GAME acl_type pemrit \n "
parser = argparse.ArgumentParser(
      prog='Domain to ACL by',
      formatter_class=argparse.RawDescriptionHelpFormatter,
      epilog=textwrap.dedent(color_text("Software for domain dns reslove a list to ACL of multi-vendor Router and Switch \n exce software with select OS and ACL name "+help + devloper_info, rgb.BLUE)))

parser.add_argument('--os', dest='os', type=str, help='Select Vander OS [cisco_xr,cisco_xe,cisco_nexus,huawei,micrtik]')
parser.add_argument('--acl_name', dest='acl_name', type=str, help='enter Access-list name')
parser.add_argument('--acl_type', dest='acl_type', type=str, help='enter Access-list type permit | DENY')
args = parser.parse_args()

os_List = ['cisco_xr','cisco_xe','cisco_nexus','huawei','micrtik']
os ="";
acl_name="";
acl_type="";
if args.os in os_List:
 os=args.os
else:
 print (color_text("ERROR #1 : Please select only OS supported [cisco_xr , cisco_xe , cisco_nexus , huawei , micrtik ] \n example :- ./dnsacl --OS ios_xr  --ACL BLOCK ", rgb.RED))
 exit()
 
if args.acl_name != None:
 acl_name=args.acl_name
else:
 print (color_text("ERROR #2: Please select ACL name , for exmaple --acl_name TEST acl_type permit \n example :- ./dnsacl --OS ios_xr  --acl_name BLOCK acl_type deny", rgb.RED))
 exit()

 
if args.acl_type != None:
 acl_type=args.acl_type
else:
 print (color_text("ERROR #3: Please select ACL type Permit | Deny , for exmaple --acl_name TEST acl_type permit \n example :- ./dnsacl --OS ios_xr  --acl_name BLOCK acl_type deny", rgb.RED))
 exit()


print(color_text("Select OS: " + os , rgb.GREEN))
print(color_text("ACL Name: " + acl_name , rgb.GREEN))
print(color_text("ACL Type: " + acl_type , rgb.GREEN))


ip_list = [];
#file1 = open(text, 'r')
file1 = open("domain.txt", 'r')
Lines = file1.readlines()
count = 0
for domain in Lines:
 count += 1
 #print("Line{}: {}".format(count, domain.strip()))
 domain =domain.strip(); 
 ais = socket.getaddrinfo(domain,0,0,0,0)

 for result in ais:
   if validIP(result[-1][0]):
    ip_list.append(result[-1][0])
    #print("permit ipv4 host {} any".format( result[-1][0]))
 ip_list = list(set(ip_list))
  

f = open('output.txt', 'w')
count =1
if os==os_List[0]: #cisco_xr 
 f.writelines("ipv4 access-list "+ acl_name +"\n" )
 print(color_text("ipv4 access-list "+ acl_name ,rgb.YELLOW))
 for host in ip_list: 
    f.writelines("%s\n" % "{} {} ipv4 host {} any".format(count,acl_type,host))
    print(color_text("{} {} ipv4 host {} any".format(count,acl_type,host),rgb.YELLOW))
    count+=1
 if acl_type=="deny":
    f.writelines("{} permit ipv4 any any".format(count ))
    print(color_text("{} permit ipv4 any any".format(count ),rgb.YELLOW))

if os==os_List[1]: #cisco_xe
 print(color_text("ip access-list "+ acl_name ,rgb.YELLOW))
 f.writelines("ip access-list "+ acl_name )
 for host in ip_list:
    f.writelines("\n {} {} ip host {} any".format(count,acl_type,host))
    print(color_text("{} {} ip host {} any".format(count,acl_type,host),rgb.YELLOW))
    count+=1
 if acl_type=="deny":
    f.writelines("\n {} permit ip any any".format(count ))
    print(color_text("{} permit ip any any".format(count ),rgb.YELLOW))

    
if os==os_List[2]: #cisco_nexus 
 f.writelines("ip access-list "+ acl_name )
 print(color_text("ip access-list "+ acl_name ,rgb.YELLOW))
 for host in ip_list:
    f.writelines("\n {} {} ip host {} any".format(count,acl_type,host))
    print(color_text("{} {} ip host {} any".format(count,acl_type,host),rgb.YELLOW))
    count+=1
 if acl_type=="deny":
    f.writelines("\n {} permit ip any any".format(count))
    print(color_text("{} permit ip any any".format(count ),rgb.YELLOW))

if os==os_List[3]: #huawei 
 f.writelines("acl number "+ acl_name)
 print(color_text("acl number "+ acl_name ,rgb.YELLOW))
 for host in ip_list:
    f.writelines("\n rule {} {} ip soruce {} ".format(count,acl_type,host))
    print(color_text("rule {} {} ip soruce {} ".format(count,acl_type,host),rgb.YELLOW))
    count+=1
    
if os==os_List[4]: #micrtik 
 for host in ip_list:
    f.writelines("\n ip firewall address-list add address={} list={}".format(host,acl_name))
    print(" ip firewall address-list add address={} list={}".format(host,acl_name))

f.close();

