# Dns resolver to ACL of Vander network 

## Description


 dirrecly convert any domain to ip access-list(ipv4) 
 <br>
support muilt-vander cisco_xr,cisco_xe,cisco_nexus,huawei,mikrotik
<br>


### Executing program

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

<h3>2- execute a software with use Argument  </h3>
<Br>
--config :  choose file of config (like config.ini)
<br>
--apply_on_host : for apply ACL to host dirreclty 
<Br>
<b>example </b>: 
<Br>

```
#./nsacl --config config.ini --apply_on_host
```

## Help

Any advise for common problems or issues.

## Authors

Contributors names and contact info

ex.  Anas abdullkarim

## Version History





