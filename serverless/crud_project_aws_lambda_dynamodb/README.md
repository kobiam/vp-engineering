# CRUD project items-inventory

This project is to create a serverless itens-inventory via Lambda and store items in Dynamodb

## TechStack

1. AWS API Gateway
2. AWS Lambda function - `Python3.12`
3. AWS DynamoDB

### Instructions

1. Create DynamoDB via the AWS console or CloudFormation
2. Create Lambda function via the AWS console or CloudFormation
    - create **serverless-api** role
    - attach CloudWatchLogs and DynamoDB policies to **serverless-api** role
3. Create API Gateway - REST API
    - create resources:
      - /ping
      - /items
    - create methods:
      - /ping
        `GET`
      - /items
        `GET`
        `DELETE`
        `POST`
4. Make API call
    - create IAM user `serverless-api` and attach IAM policy ApiGatewayInvoke
    - copy the invoke url from the stages in API Gateway
    - paste the invoke url to postman and add the AWS access key and secret key

### API Calls

- GET `https://3opp95xidi.execute-api.us-east-1.amazonaws.com/serverless-api-stg/items?itemId=papaya`
- POST `https://3opp95xidi.execute-api.us-east-1.amazonaws.com/serverless-api-stg/items` with the JSON Content
- DELETE `https://3opp95xidi.execute-api.us-east-1.amazonaws.com/serverless-api-stg/items?itemId=papaya`

### POST

![POST](/serverless/crud_project_aws_lambda_dynamodb/pics/POST.png)

### GET

![POST](/serverless/crud_project_aws_lambda_dynamodb/pics/GET.png)

### DELETE

![POST](/serverless/crud_project_aws_lambda_dynamodb/pics/DELETE.png)

### AWS API GATEWAY

![POST](/serverless/crud_project_aws_lambda_dynamodb/pics/API-GATEWAY.png)

### AWS DynamoDB

![POST](/serverless/crud_project_aws_lambda_dynamodb/pics/DynamoDB.png)
