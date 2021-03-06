﻿# ScanToolkit
*Is a toolkit capable to realize ports scan, host discover ,nslookup service, IPv4 Geolocation, Shodan Api and more.*

```[javascript]
[First Configuration] 
	Requeriments: pip install -r requeriments.txt
	Usage: setup.py
Usage: toolkit.py -M <Menu option> <Option>

Menu
1. Local Host Discover.
2. Ports Scanner.
3. NSlookup Windows type=(A, ANY, CNAME, MX, NS, PTR, SOA, SRV).
4. IPv4 Geolocation.
5. Shodan Api.
6. DNS Records.

Options:
  -h, --help                               Show this help message and exit
  -M MENUOPTION, --menu = MENUOPTION       Insert the number of option
  -P PARAMETER, --Parameters = PARAMETER   Insert parameters separated by comma
  -H HOST, --Host = HOST                   Insert a host to scan
  -p PORT, --Port = PORT                   Insert parameters separated by comma
  -R RANGE, --Range = RANGE                Insert parameters separated by comma
  -Q Query, --Query = Query 			   Shodan Query
  -F FLAG,  --Flag = Flag                  Insert a flag to TCP or UDP port scan
  
Examples:
  Host Discover:                 toolkit.py -M 1 -R <port_range>
  Port Scanner:  All ports       toolkit.py -M 2 -H <ip_address>
                 Specific ports  toolkit.py -M 2 -H <ip_address> -P <port>,<port> (TCP flag)
                 Specific flag   toolkit.py -M 2 -H <ip_address> -P <port>,<port> -F <tcp/udp flag>
  Nslookup:                      toolkit.py -M 3 -H <ip_address> -P A,ANY,CNAME,MX,NS,PTR,SOA,SRV
  IpGeolocation: MyIp Address    toolkit.py -M 4
                 Specific Ip     toolkit.py -M 4 -H <ip_address>
  Shodan Api:    Search          toolkit.py -M 5 -Q "Query"
		 Host Scanner    toolkit.py -M 5 -H <ip_address>
  DNS Records:                   toolkit.py -M 6 -H <DNS>
```
