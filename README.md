<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>



<h1>Dns resolver to ACL of Vander network (Cisco , huawei , mikroti</h1>k)

<b> dirrecly convert any domain to ip access-list(ipv4) </b>
<Br>
<b>support muilt-vander cisco_xr,cisco_xe,cisco_nexus,huawei,mikrotik </b>
<Br>
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

<h3>2- execute a software with use Argument  </h3>
<Br>
<b>--config<B> :  choose file of config (like config.ini)
<br>
<b>--apply_on_host<B>  : for apply ACL to host dirreclty 
<Br>
<b>example </b>: 
<Br>
 <code>#./nsacl --config config.ini --apply_on_host<code>
