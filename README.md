[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=6818706&assignment_repo_type=AssignmentRepo)
# restart-ss-2021-assignment1-template

This assignment is made up of 7 tasks.

## Task 1 - Database - 35 Marks

Use the SQLite version of the Sakila database from https://github.com/krp/sakila-sqlite 

Use SQLite Browser ( https://sqlitebrowser.org/ ) to help you create twenty (20) unique queries to display and manipulate data from each of the tables. 

Hint: SELECT * FROM city; is one unique query. 

a) Edit the file named queries.py to add twenty (20) Python functions that will be used to run the queries using Python’s sqlite3 module.  [20 marks] 

SQL Commands: 

b) Demonstrate the user of ORDER BY in at least one (1) table.  [2 marks] 

c) Demonstrate the use of WHERE in at least three (1) tables.  [1 mark] 

d) Demonstrate the use of DELETE in at least one (1) table.  [1 mark] 

e) Demonstrate the use of UPDATE in at least one (1) table.  [1 mark] 

f) Demonstrate the use of INSERT INTO in at least 5 tables.  [5 marks] 

g) Demonstrate the use of JOIN in at least two (2) tables.  [5 marks] 


## Task 2 - Web API - 35 Marks

Create a file named main.py which will be used to create an API using FastAPI ( https://fastapi.tiangolo.com/ - installed with pip install fastapi). 

a) Use FastAPI and main.py to create twenty (20) routes, one for each of your queries, reusing the code from the previous section with Python’s import statement. [10 marks] 

b) Use the HTTP GET method for queries which use SELECT statements.  [5 marks] 

c) Use the HTTP POST method for queries which use INSERT INTO statements.  [5 marks] 

d) Use the HTTP DELETE method for queries which use the DELETE statement.  [5 marks] 

e) Use the HTTP PUT method for queries which use the UPDATE statement.  [5 marks] 

Hint: @app.get(“/pathname”) is how you use the HTTP GET method. 

f) Create a /hash_password route which accepts a password via HTTP POST and returns a hexdigest using an algorithm from Python’s hashlib library.  [5 marks] 

 

Verify your API works by running the uvicorn webserver (installed with pip install uvicorn) and testing it with your browser at http://localhost:8000/docs . 

Ensure you upload your finished version of main.py to GitHub. 


## Task 3 - Security - 20 Marks

In the Security.md file in your GitHub repository add the following details. 

a) The SSH public key located in ~/.ssh/authorized_keys and the algorithm it uses.  [5 marks] 

b) The command used to change the API server port number (last 5 digits of your student ID number) which needs to be opened under security group settings.  [5 marks] 

c) Changing your SSH server port number can reduce the amount of bruteforce attempts that spam your SSH logs. Change your SSH server port number to the first 5 digits of your student ID number. Write down the name of the file and the line you would need to change in order to change the SSH. [5 marks] 

d) The hashing algorithm you chose earlier for the /hash_password route, and depending on which you chose, list its strengths and weaknesses.  [5 marks] 
    
    
    
## Task 4 - Networking - 10 Marks

In the Networking.md file in your GitHub repository add the following details. 

a) VPC Name and VPC ID: (Include your first name in the VPC name)  [1 mark] 

b) Public & Private Subnet CIDR Blocks [1 mark] 

Upload screenshots of the following as evidence that you have completed this section. 

c) Screenshot of VPC details  [2 mark] 

d) Screenshots of Subnet details  [2 marks] 

e) Screenshots of Security Group details  [2 marks] 

f) Screenshot of Internet Gateway details  [2 marks] 

Upload screenshots to the repository as proof. The screenshots should match the details in Networking.md. 


## Task 5 - Shell Scripting - 10 Marks

Add the following files to your GitHub repository. 

a) Create a simple shell script named install.sh which installs the latest version of Python and the required Python libraries (fastapi & uvicorn).  [5 marks] 

b) Create a simple shell script named runme.sh which runs the uvicorn webserver on a publically accessible IP address (0.0.0.0:54321) when the user types ./runme.sh into a shell.  [5 marks] 

Hint: Don’t forget to include the #! at the top of the file. 


## Task 6 - Linux/Cloud - 30 Marks

Set up a 2nd EC2 instance and install the Python httpie library on it. 

Using the http command it installed, query one of the routes your API provides. 

In the Cloud.md file in your GitHub repository add the following details. 

a) The name of the Linux distribution your EC2 instance uses.  [2 marks] 

b) The hardware architecture your server uses (e.g. 64-bit x86, 64-bit ARM).  [2 marks] 

c) The Amazon Machine Image (AMI) ID (e.g. ami-052432ead9b0a1234) used.  [2 marks] 

d) The EC2 instance type (e.g. t3.xlarge) you’re using.  [2 marks] 

e) The number of vCPUs your instance has.  [2 marks] 

f) The amount of RAM/memory (GB) your instance has.  [2 marks] 

g) The storage size (GB) your instance has.  [2 marks] 

h) Your VPC network id (e.g. vpc-0784bdc0c0866c695).  [2 marks] 

i) Your Public/Elastic IP address (your server’s IP address). [2 marks] 

j) The Private IP address of your server (begins with 10.0.). [2 marks] 

k) The Network Address of the subnet your server is using (Hint: Run ip addr).  [2 marks] 

l) The Broadcast Address of the subnet your server is using. [2 marks] 

m) The Default Gateway Address configured for your server. (Hint: Run ip route).  [2 marks] 

n) The client output from the http command.  [2 marks] 

o) The logs displayed by uvicorn on the server.  [2 marks] 


## Task 7 - Database Cloud Deployment - 10 Marks

Using the 162 - [DF] - Lab - [Challenge] Build and Access an RDS Server lab from Canvas, deploy a database server using RDS and connect to it from the command line. 

Find a way to migrate your SQLite database to your RDS database of choice. 

In the RDS.md file, add the following details: 

a) A paragraph on about chosen database software (e.g. PostgreSQL, MySQL, Aurora) and why you chose it over an alternative.  [2 marks] 

b) A link to the resource(s) you used when learning how to do this.  [2 marks] 

c) The command used to connect a CLI client to the database.  [2 marks] 

d) The IP address of your database and the subnet it is in.  [2 marks] 

e) Export the sakila schema & data from this database (not-SQLite) to a .sql file and add it to GitHub.  [2 marks] 


