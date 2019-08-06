import subprocess

#Global variable

greeting = ["hello"]
ip_target = "172.20.10.13/24"
fping_range = "fping -g"
ip_range = 0
pysweep_file = open("filePysweep.txt", mode ="w+t")

#Create a list of IP addresses

def create_ip_list():
    output = subprocess.run(['fping', '-g', '-a','-q', ip_target], capture_output=True, check=False)
    ip_range = output.stdout.split()
    pysweep_file.write(str(ip_range).replace('b', ''))
    pysweep_file.close()
    print(ip_range)
    

if __name__ == "__main__":
    create_ip_list()
  