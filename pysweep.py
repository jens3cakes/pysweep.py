import subprocess



#Global variable

greeting = ["hello"]



#Create a list of IP addresses

def create_ip_list():
    pass

#Loop over the list of IP addresses
def process_list():
    pass

#Print out each one
def print_ip_addesess():
    pass

def add_on():
    greeting.append("bye")  
    print(greeting)

def list_files():
    output = subprocess.run(["fping", "10.0.2.6"], capture_output=True)
    print(output.stdout, output)


if __name__ == "__main__":
    pass 
    add_on()
    print(greeting)
    list_files()

  