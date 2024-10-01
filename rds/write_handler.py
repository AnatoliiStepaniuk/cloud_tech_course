import pymysql
import os
import json


# RDS configuration
rds_host = os.environ['RDS_HOST']
rds_user = os.environ['RDS_USER']
rds_password = os.environ['RDS_PASSWORD']
rds_db = os.environ['RDS_DB']


# Connect to MySQL database
def connect_to_db():
   try:
       conn = pymysql.connect(
           host=rds_host,
           user=rds_user,
           password=rds_password,
           db=rds_db,
           connect_timeout=10
       )
       return conn
   except pymysql.MySQLError as e:
       print(f"Error connecting to MySQL: {e}")
       return None


# Function to insert data into the database
def insert_into_db(conn, student_data):
   try:
       with conn.cursor() as cursor:
           sql = """
           INSERT INTO students (first_name, last_name, age, grade, enrollment_date)
           VALUES (%s, %s, %s, %s, %s);
           """
           cursor.execute(sql, (
               student_data['first_name'],
               student_data['last_name'],
               student_data['age'],
               student_data['grade'],
               student_data['enrollment_date']
           ))
           conn.commit()
           return True
   except pymysql.MySQLError as e:
       print(f"Error inserting data: {e}")
       return False


# Lambda Handler function
def handler(event, context):
   conn = connect_to_db()


   if conn is None:
       return {
           'statusCode': 500,
           'body': json.dumps({'message': 'Error connecting to the database.'}, ensure_ascii=False)
       }


   # Extract student data from the request body
   try:
       student_data = json.loads(event['body'])
   except (KeyError, json.JSONDecodeError) as e:
       return {
           'statusCode': 400,
           'body': json.dumps({'message': f'Error reading student data: {e}'}, ensure_ascii=False)
       }


   success = insert_into_db(conn, student_data)


   # Close the connection
   conn.close()


   if success:
       return {
           'statusCode': 200,
           'body': json.dumps({'message': 'Student data successfully added.'}, ensure_ascii=False)
       }
   else:
       return {
           'statusCode': 500,
           'body': json.dumps({'message': 'Error inserting data into the database.'}, ensure_ascii=False)
       }


# For local testing
if __name__ == '__main__':


   # Example student data
   event = {
       'body': json.dumps({
           'first_name': 'Микита',
           'last_name': 'Самойлюк',
           'age': 19,
           'grade': 4,
           'enrollment_date': '2024-09-30'  # Format 'YYYY-MM-DD'
       })
   }
   context = None


   result = handler(event, context)
   print(result)