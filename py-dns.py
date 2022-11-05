import socket

#check if ip is ipv4
def validIP(address):
    parts = address.split(".")
    if len(parts) != 4:
        return False
    for item in parts:
        if not 0 <= int(item) <= 255:
            return False
    return True
  
 
# Using readlines()
ip_list = [];
file1 = open('Domin.txt', 'r')
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
  

for host in ip_list:
    #Chnage any output to as your router or swtich 
    print("permit ipv4 host {} any".format(host))