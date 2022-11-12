# Project Title

Dns resolver to ACL of Vander network 

## Description


 dirrecly convert any domain to ip access-list(ipv4) 
support muilt-vander cisco_xr,cisco_xe,cisco_nexus,huawei,mikrotik

## Getting Started

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)







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
