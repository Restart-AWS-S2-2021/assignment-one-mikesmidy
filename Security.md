# Task 3 - Security

## a) Paste the SSH public key and list the algorithm it uses below.
ssh-rsa AEBRB1AsaT1ak1DBASACAIIBSAAMCCCPh2aOkcHCAtRKSF/NSeIzqD9L9Se2OxmaGsQ8ais$

RSA hashing algorithm
## b) Paste the command used to run your API server on a different port
### The port should be the last 5 digits of your student ID number
uvicorn main:my_querie_app --reload --port 64696

## c) Write down the name of the SSH configuration file and the line needed to change its port.
### The port should be the first 5 digits of your student ID number
sshd_config, line 18, where it says "Port 22" 

## d) The hashing algorithm you chose earlier for the /hash_password route
### Write a brief paragraphs on its strengths and weaknesses (in your own words, don't copy/paste from the Internet)
A big disadvantage is security. If the private key is given out or is stolen, it will enable the ability to decrypt past messages also.
Another disadvantage is it can be very slow when it comes to encrypting large data on the same computer.


An advantage is that I can share my public key with anyone. This way they can encrypt a message to me but I'm the only one being able to decrypt it with the private key.
Public key encryption is also quite fast and can be done directly and is helpful for verification. 