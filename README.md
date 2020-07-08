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
### A. PHASE 1: Install Cloud SDK
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
    
### B
