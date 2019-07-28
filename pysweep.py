import subprocess
import re



#Global variable

greeting = ["hello"]
ip_target = "10.0.2.0/24"
fping_range = "fping -g"
ip_range = ""
pysweep_file = open("filePysweep.txt", mode ="w+t")



#Create a list of IP addresses

def create_ip_list():
    output = subprocess.run(['fping', '-g', '-a','-q', '10.0.2.0/24'], capture_output=True, check=False)
    ip_range = output.stdout.split()
    pysweep_file.write(str(ip_range).replace('b', ''))
    pysweep_file.close()
    # pysweep_file.write(str(output.stdout.split())
    # print(ip_range)
    # sorted(pysweep_file)
    # print(pysweep_file)
    print(ip_range)
    return pysweep_file
    

    
# Loop over the list of IP addresses
def process_list():
    def loop_over():
        for ip in pysweep_file:
            return ip
        print(ip)
    # output = subprocess.run(['fping', '-C', '5', loop_over()], capture_output=True)
    

   
    # output = subprocess.run(['fping', '-C', 5, ip_range], capture_output=True)
    # print(output.stdout)

# #Print out each one
# def print_ip_addesess():
#     pass

# def add_on():
#     greeting.append("bye")  
#     print(greeting)

# def list_files():
#     output = subprocess.run(["fping", "10.0.2.6"], capture_output=True)
#     print(output.stdout, output.value)


if __name__ == "__main__":
    create_ip_list()
    process_list()
    print(ip_range)
  