# GCP
## Installing Python 3.7 on GG Cloud Shell SSH of VM-Instances:
### Install requirements
sudo apt-get install -y build-essential checkinstall libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev zlib1g-dev openssl libffi-dev python3-dev python3-setuptools wget 

### Prepare to build
mkdir /tmp/Python37
cd /tmp/Python37

### Pull down Python 3.7, build, and install
wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
tar xvf Python-3.7.0.tar.xz
cd /tmp/Python37/Python-3.7.0
./configure
sudo make altinstall

## CONNECT to Google Cloud SQL from local client (MacOS):
### PHASE 1: Install Cloud SDK
1 .First of all, kindly make sure you already have the GCP account (account + project for Cloud SDK connect to)

  Make reference to link https://console.cloud.google.com/ for the create GCP account

2. Check your Python verison: 

    python -V 
    
    or 
    
    python --version

3. Download Cloud SDK which is compatible with OS you are using: MacOS 32bits | MacOS 64bits:

    Unzip the downloaded file: 
    
    tar -xvf <path_to_file_Cloud_SDK>
  
    we would have a folder name: 
    
    google-cloud-sdk 
 
4. Run the command below for installing Cloud SDK:

    ./google-cloud-sdk/install.sh
    
    After installing Cloud SDK, restart your terminal and use the following command to check the gcloud version: 
    
    gcloud -v
    
### PHASE 2: Create database on Cloud SQL
    Kindly refer the documents how to create a Database Instances on GG Cloud SQL (PostgreSQL, SQL Server, mysql)
    
### PHASE 3: Connect to Database on Cloud SQL from Local Client (MacOS):

1. Make connection to GG Cloud:
   a, Make connection with GG Cloud 
   
    gcloud init

    On your screen would have notification to "Login to continue, you must log in. Would you like to log in (Y/n)?" --> press Y . 
  
    Note: For the first time you would be redirected to a login page, for the next logins you just need to choose which account that's login before.
  
    b, Termial will display the list of project for your choice, please input the number of project and press enter
  
    If it is ok, terminal makes notification: "Your Google Cloud SDK is configured and ready to use!"

2. Installing Cloud SQL Proxy (Mac 64-bit):

    curl -o cloud_sql_proxy https://dl.google.com/cloudsql/cloud_sql_proxy.darwin.amd64

    chmod +x cloud_sql_proxy
  
3. Check the "connectionName" (name of Cloud SQL Instance)

    gcloud sql instances describe family-postgres-db
    
    Note: "family-postgres-db" is the name of instance created on Cloud SQL, we would have the information of "connectionName" in order to connect to database.
      --> in terminal, connectionName: "myproject-01-255502:asia-southeast2:family-postgres-db"
    
4. Connect with Cloud SQL database (Postgres) from Client Local Host:

    ./cloud_sql_proxy -instances=<connectionName>=tcp:3306 
  
    --> CONGRATULATION, you now already have a database at local host (Client) that connected to database (Postgres) on the Cloud SQL.
  
5. Check the connect by tools (SQLPRO Studio, Navicat, pgAdmin,...)

  
