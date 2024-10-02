To connect to database with CLI, first install mysql cli client.

After that use a command like this (for MacOS):

`mysql -h public-mysql.c1omqs84aom8.eu-west-3.rds.amazonaws.com -u admin -p`

instead of `public-mysql.c1omqs84aom8.eu-west-3.rds.amazonaws.com` use your DB host (copied from the RDS page in AWS).


To install Python packages locally:

`pip install -r requirements.txt -t .`

To create `.zip` archive for Lambda function:

`zip -r my_lambda_function.zip .`
