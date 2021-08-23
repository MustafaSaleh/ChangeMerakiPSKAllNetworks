#ChangeMerakiPSKAllNetworks 
#by Mustafa Hussein &  Muhannad Al-Shaer
#Thanks for using this script
#Important before start, You have to be sure about your ssid name
#We are assuming here that you have the same SSID name at all your networks

import meraki
APIKEY = DASHBOARD = NEWPSK = SSIDNAME = None

def connectDashboard():
    return meraki.DashboardAPI(APIKEY,print_console=False)
   
#get organizations
def getOrgs():
    return DASHBOARD.organizations.getOrganizations()

#get Netowkrs and update any SSID start number = SSIDnum
def updateAllSSIDs(organization_id):
        #get networks
        netws=  DASHBOARD.organizations.getOrganizationNetworks(organization_id, total_pages='all')
        ssidCounter = 0;
        for netw in netws:
            SSIDs = DASHBOARD.wireless.getNetworkWirelessSsids(netw['id'])
            for ssid in SSIDs:
                if(ssid['name'] == SSIDNAME ):
                    ssidCounter +=1
                    print("I found your SSID: " + ssid['name'])
                    #update SSID PSK
                    
                    res = DASHBOARD.wireless.updateNetworkWirelessSsid(
                        netw['id'], 
                        ssid['number'], 
                        psk= NEWPSK
                    )
                    if(res['number']):
                        print("SSID "+res['name']+ " @ Netowk:"+ netw['name'] + " has been updated.")
        if(ssidCounter==0):
            print("I didn't find "+SSIDNAME+ " at any of your networks")
        else:
            print("Number of SSID updated: ", ssidCounter)
            
#Fetch organizations
def fetchOrgs(orgs):
    i = 0
    while( i < len(orgs)):
         print(i, orgs[i]['name'])
         i +=1

#set API Key
APIKEY = input("Please insert your APIKEY: ")
print("APIKEY saved")

#connect to Dashboard
DASHBOARD = connectDashboard()
print("Dashboard Connected.")

SSIDNAME = input("Which SSID do you need to update?  ")
# set Organization
NEWPSK = input("Please insert a new PSK: ")

print("Please hold-on, I'm getting your organizations now....")
orgs = getOrgs()
fetchOrgs(orgs)
orgIndex = int(input("Select organization: "))
print("You have selectd: " ,orgs[orgIndex]['name'])

updateAllSSIDs(orgs[orgIndex]['id'])



