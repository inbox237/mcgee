## Mcgee Exercise

Setup Instructions:

STEPS FOR CLIENT CLONE:
EC2 - press Launch Instance - then select ubuntu 20.04 - t2.micro
Add Tags Name mcgee_client + open port 5000 in security groups
create PEM called vpc and download, move this to ~/.ssh/
cd ~/.ssh/
sudo chmod 600 vpc.pem

Find public ip address on AWS

Then run the following commands:
```
ssh -i ~/.ssh/vpc.pem ubuntu@13.210.122.128 - change this ip address to yours
sudo apt update
git clone https://github.com/inbox237/mcgee
cd mcgee
python3 -m venv venv
source venv/bin/activate
sudo apt-get install libpq-dev
sudo apt-get install gcc libpq-dev -y
sudo apt-get install python-dev python-pip -y
sudo apt-get install python3-dev python3-pip python3-venv python3-wheel -y
sudo apt install libgirepository1.0-dev
sudo apt install libdbus-1-3 libdbus-1-dev

pip install -r requirements.txt
```
```
vim .env 
```
then copy the following into the .env file:
```
DB_URI= "postgresql+psycopg2://postgres:coder@13.210.56.56/mcgee_agentoffice"
DB_BINDS = {"mcgee_mayblack":"postgresql+psycopg2://postgres:coder@13.210.56.56/mcgee_mayblack"}
```

Then run these commands:
```
export FLASK_APP=main.py
export FLASK_ENV=development
flask db start
```

Here is the public ip address of my client but you can replace everything before :5000/agents/ with the correct IP of your client

```
http://ec2-13-210-122-128.ap-southeast-2.compute.amazonaws.com:5000/agents/
```




