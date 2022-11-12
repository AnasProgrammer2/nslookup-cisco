
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



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
