import subprocess
import re
import os


#Global variable

greeting = ["hello"]
ip_target = "10.0.2.0/24"
fping_range = "fping -g"
ip_range = []
pysweep_file = open("filePysweep.txt", mode ="w+t")



#Create a list of IP addresses

def create_ip_list():
       
     output = subprocess.run(['fping', '-g','-a','-q', ip_target], text = True, capture_output=True)
     spl_output = output.stdout.split('\n')

     for ip in spl_output:
             output = subprocess.run(['fping', '-C', '5', str(ip)], capture_output=True, text = True)
             pysweep_file.write(output.stdout)   
     
     pysweep_file.close()


    
   

if __name__ == "__main__":
    create_ip_list()
    
    
  