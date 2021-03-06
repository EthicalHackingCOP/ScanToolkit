# -*- coding: UTF-8 -*-
#!/usr/bin/python

import scanning
import netscan
import nslookup
import optparse
import banners
import geoip
import shod
import dnsrecords


from socket import *
from threading import *
def toolkit(api_keys):
    Keys = api_keys
    parser = optparse.OptionParser('usage %prog '+\
		'-M <Menu option> -P <Parameters>')
    parser.add_option('-M','--Menu', dest='MenuOption', type='string', \
		help='|Insert the number of option')
    parser.add_option('-P','--Parameters', dest='parameter', type='string', \
		help='Insert parameters separated by comma')
    parser.add_option('-H','--Host', dest='host', type='string', \
		help='Insert parameters separated by comma')
    parser.add_option('-p','--Port', dest='port', type='string', \
		help='Insert parameters separated by comma')
    parser.add_option('-R','--Range', dest='range', type='string', \
		help='Insert parameters separated by comma')
    parser.add_option('-Q','--Query', dest='query', type='string', \
		help='"Shodan Query into quotes"')
    parser.add_option('-F', '--Flag', dest='flag', type='string', \
                      help='"tcp or udp scan"')
    
    (options, args) = parser.parse_args()
    try: 
        Moption = options.MenuOption
    except Exception, e:
        print "\n[!] Error: "+str(e)
        exit(0)
    if (Moption == "1"):
        try:
            parameters= str(options.range).split(",")
        except Exception, e:
            print "\n[!] Error: "+str(e)
            exit(0)
        if parameters[0] != "None":   
            try:
                #banners.randomBanner()
                netscan.netscan(int(parameters[0]),int(parameters[1]))
            except Exception, e:
                print "\n[!] Error: "+str(e)
            exit(0)
        else:
            try:
                banners.randomBanner()
                netscan.netscan(2,254)
            except Exception, e:
                print "\n[!] Error: "+str(e)
            exit(0)
    elif(Moption == "2"):
        try:
            host = str(options.host)
            ports = str(options.port)
            flag = str(options.flag)
        except Exception, e:
            print "\n[!] Error: "+str(e)
        banners.randomBanner()

        if ports != "None":
            scanning.scaner(host,ports,flag)
        else:
            scanning.scaner(host,"",flag)

        exit(0)
    elif(Moption == "3"):
        try:
            parameters= str(options.parameter)
            host = str(options.host)
        except Exception, e:
            print "\n[!] Error: "+str(e)
        try:
            banners.randomBanner()
            nslookup.nslookupscanOPT(parameters,host)
        except Exception, e:
            print "\n[!] Error: "+str(e)
        exit(0)
    elif(Moption == "4"):
        try:
            host = str(options.host)
        except Exception, e:
            print "\n[!] Error: "+str(e)
        if host != "None":
            try:
                banners.randomBanner()
                geoip.remoteIpOPT(host)
            except Exception, e:
                print "\n[!] Error: "+str(e)
        else:
            try:
                banners.randomBanner()
                geoip.myIpOPT()
            except Exception, e:
                print "\n[!] Error: "+str(e)
        exit(0)
    elif(Moption == "5"):
        query = str(options.query)
        host = str(options.host)
        if Keys['Shodan_Api_Key'] == "":
            print "Please insert the shodan_api_key on data.json file."
            exit(0)
        if host != "None" and query != "None":
            print "Error. Please insert a correct query"
        elif host != "None":
            try:
                banners.randomBanner()
                shod.searchHost(host,Keys['Shodan_Api_Key'])
            except:
                print "Error. Please insert correctly a query"
        elif query != "None":
            try:
                banners.randomBanner()
                shod.searchQuery(query,Keys['Shodan_Api_Key'])
            except:
                print "Error. Please insert correctly a query"
        else:
            print "Please insert a query"
        exit(0)
    elif(Moption == "6"):
        try:
            dns = str(options.host)
        except Exception, e:
            print "\n[!] Error: "+str(e)
        if dns != "None":
            try:
                dns = dns.split(",")
                for x in dns:
                    banners.randomBanner()
                    dnsrecords.DNSRecordOpt(x)
            except Exception, e:
                print "\n[!] Error: "+str(e)
        else:
            print "[-] You gotta to insert a dns for this scan."
        exit(0)
    elif(Moption == "Help" or Moption == "HELP" or Moption == "help"):
        sos()
        exit(0)

    banners.randomBanner()
    print "\nMenu"
    print "1. Local Host Discover."
    print "2. Ports Scanner."
    print "3. NSlookup Windows."
    print "4. IPv4 Geolocation."
    print "5. Shodan Api."
    print "6. DNS Records."

    try:
        menu = raw_input("Option: ")
    except Exception, e:
        print "\n[!] Error: "+str(e)
        exit(0)
    if(menu=="1"):
        netscan.netscan("2","254")
    elif(menu=="2"): 
        scanning.scaner("","","")
    elif(menu=="3"):
        nslookup.nslookupscan()
    elif(menu=="4"):
        geoip.GeoIp()
    elif(menu=="5"):
        shod.shodanS(Keys['Shodan_Api_Key'])
    elif(menu=="6"):
        dnsrecords.DNSRecord()
    elif(menu=="Exit" or menu=="EXIT" or menu=="exit"):
        exit(0)

def sos():
    banners.randomBanner()
    print "[*] Menu"
    print "\t1. Local Host Discover."
    print "\t2. Ports Scanner."
    print "\t3. NSlookup Windows."
    print "\t4. IPv4 Geolocation."
    print "\t5. Shodan Api."
    print "\t6. DNS Records."
    print "[*] Options:"
    print "\t-M --menu <Menu Option> \n\t-P --Parameters <Parameters> \n\t-H --Host <dns/host/IPv4> \n\t-p --Port <port> \n\t-R --Range <range> \n\t-Q --Query \"Shodan Query\""
    print "[*] Examples:"
    print "\t-- Local Host Discover\n\t\t\t\t\ttoolkit.py -M 1 -R <range hosts> "
    print "\t-- Ports Scanner\n\t\tAll ports\t\ttoolkit.py -M 2 -H <ip_address>"
    print "\t\tSpecific ports\t\ttoolkit.py -M 2 -H <ip_address> -P <port>,<port>"
    print "\t-- Nslookup \n\t\t\t\t\ttoolkit.py -M 3 -H <DNS> -P A,ANY,CNAME,MX,NS,PTR,SOA,SRV"
    print "\t-- IpGeolocation\n\t\tMyIp Address\t\ttoolkit.py -M 4 "
    print "\t\tSpecific Ip\t\ttoolkit.py -M 4 -H <ip_address>"
    print "\t\tShodan Host Scanner\ttoolkit.py -M 5 -H <ip_address>"
    print "\t-- DNS Records \n\t\t\t\t\ttoolkit.py -M 6 -H <DNS>"
    
if __name__ == '__main__':
    file = "data.json"
    setup_data = eval(open(file, 'r').read())
    start = setup_data['starting']
    if start != 0:
        try:
            toolkit(setup_data['keys'])
        except:
            exit(0)
    else:
        print "\nFirst Execute setup.py"

