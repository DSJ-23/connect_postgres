# Example connect to  postgres through lambda

Create serverless project
```
sls create -t aws-python
```

Deploy all functions in current project
```
sls deploy
```

Deploy single function
```
sls deploy function -f functionName
```

Install AWS CLI
```
brew install awscli
```

Configure AWS CLI
```
aws configure
```

List out all functions
```
aws lambda list-functions
```

List out 2 most recent lambda functions
```
aws lambda list-functions --query "reverse(sort_by(Functions, &LastModified))[:2]"
```

Install dependencies for db connection
```
python3 -m pip install psycopg2
python3 -m pip install sqlalchemy
```

Layers installing pip package in same directory example 
```
pip3 install -t $PWD pymysql or pip3 install pymysql .
```

pip3 install requests -t .
pip3 install pandas -t .

pip3 install -t $PWD requests