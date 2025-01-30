# Deployment Instructions

## Step 1: Create an AWS Lambda Function
1. Go to the AWS Management Console.
2. Navigate to Lambda and click "Create Function."
3. Configure the function:
   - Runtime: Python 3.9
   - Memory: 128 MB
   - Timeout: 30 seconds
4. Upload the `lambda_function.py` file as the code.

## Step 2: Set Up API Gateway
1. Go to API Gateway in the AWS Management Console.
2. Create a new HTTP API.
3. Integrate the API with the Lambda function.
4. Deploy the API and note the invoke URL.

## Step 3: Test the API
Use tools like Postman or `curl` to send requests to the API endpoint and verify the responses.
