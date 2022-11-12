Dns resolver to ACL of Vander network (Cisco , huawei , mikrotik)
# nslookup-to-ACL
<B>How to use</B>

<h3>1- update config file (config.ini) with information </h3>
<br>
ipaddress = [ip address of Host]
<br>
username = [username of host]
<br>
password = [password of host]
<br>
osHost  = [vander type (cisco_xr,cisco_xe,cisco_nexus,huawei,mikrotik)]
<br>
acl_name =[ACL of name will generate ]
<br>
acl_type =[ACL action (deny | permit)]
<br>
output_folder_name = [folder name wll be storage of output files]
<br>

<h3>2- execute a software with use Argument Parser </h3>
<Br>
<b>--config<B> choose file of config (like config.ini)
<br>
<b>--apply_on_host<B> for apply ACL to host dirreclty 
<Br>
example : 
<Br>
 <code>#./nsacl --config [config file name] --apply_on_host<code>
