a) Name of your Linux distribution:
Linux kernel 5.10
b) Hardware architecture your server uses: 
64-bit x86
c) Amazon Machine Image (AMI) ID your server uses:
ami-0d3907809e0f70e5d
d) EC2 instance type used: 
t2 micro
e) Number of vCPUs your instance has: 
1
f) Amount of RAM/memory your instance has: 
1 gb
g) Storage size your instance has: 
8gb
h) Your VPC network id: 
vpc-0a1bbc9543a3d7ce2 (Mikes VPC)
i) Your Public/Elastic IP address: 
35.164.161.197
j) Private IP of your server: 
10.0.64.243 
k) Network address of your subnet: 
10.0.64.0
l) Broadcast address of your subnet: 
10.0.64.255
m) Default Gateway Address configured: 
10.0.64.1
n) Client output of `http` command: 

HTTP/1.1 200 OK
Cache-Control: no-cache, must-revalidate
Connection: Upgrade, Keep-Alive
Content-Length: 1290
Content-Type: text/html; charset=UTF-8
Date: Fri, 28 Jan 2022 14:34:24 GMT
Expires: Sat, 26 Jul 1997 05:00:00 GMT
Keep-Alive: timeout=5, max=100
Server: Apache/2.4.52 () PHP/5.4.16
Upgrade: h2,h2c
X-Powered-By: PHP/5.4.16
<!DOCTYPE html>
<html>
  <head>
    <title>Welcome to AWS Technical Essentials v4.1</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/style.css" rel="stylesheet">
  </head>

  <body>
    <div class="container">

      <div class="row">
          <div class="col-md-12">

      <nav class="navbar navbar-default" role="navigation">

<div class="navbar-header">
  <a class="navbar-brand" href="/"><img height="25" src="img/AWS_logo_RGB.png" /></a>
</div>

<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
  <ul class="nav navbar-nav">
    <li>
      <a href="load.php">Load Test</a>
    </li>
    <li>
      <a href="rds.php">RDS</a>
    </li>
  </ul>
</div>

</nav>
      <div class="jumbotron">
      <p>
      <table class='table table-bordered'><tr><th>Meta-Data</th><th>Value</th></tr><tr><td>InstanceId</td><td><i>i-0c3fc7f75a5396566</i></td><tr><tr><td>Availability Zone</td><td><i>us-west-2a</i></td><tr></table>
      <hr />

      <br /><p>Current CPU Load: <b>0%</b></p>            </p>
      <p>
      </p>
    </div>
    </div>
    </div>
    </div>

    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/scripts.js"></script>

  </body>
</html>

o) Logs displayed by `uvicorn` for the client request:
