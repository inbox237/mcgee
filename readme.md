
# Mcgee Exercise

## Description



STEPS FOR CLIENT CLONE:
EC2 - press Launch Instance - then select ubuntu 20.04 - t2.micro
Add Tags Name mcgee_client + open port 5000 in security groups
create PEM called vpc and download, move this to ~/.ssh/
cd ~/.ssh/
sudo chmod 600 vpc.pem
Find public ip address on AWS
ssh -i ~/.ssh/vpc.pem ubuntu@13.210.122.128 - change this ip address to yours
sudo apt update
git clone https://github.com/inbox237/mcgee

Go to installation folder
git clone "ADDRESS of my git"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=main.py
export FLASK_ENV=development
flask db start


DB_URI= "postgresql+psycopg2://postgres:coder@13.210.56.56/mcgee_agentoffice"
DB_BINDS = {"mcgee_mayblack":"postgresql+psycopg2://postgres:coder@13.210.56.56/mcgee_mayblack"}


