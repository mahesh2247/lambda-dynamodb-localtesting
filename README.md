
The aim of this repository is to provide a local environment to test the integration of your serverless web application before deploying it on the cloudformation stack.
The template file constains API gateway , lambda and dynamoDB resources. The DynamoDB image is built from aws/dynamodb-local for local testing

Kidnly make sure you have an AWS account and have configured the `AWS_KEY_ID` and `AWS_SECRET_KEY` on your CLI

1. Clone the repo

2. `docker run -p 8000:8000 amazon/dynamodb-local`
To run the DynamoDB local in a docker container at port 8000.

3. Try listing dynamodb tables using `aws dynamodb list-tables --endpoint-url http://localhost:8000`
You should see below output 
```{
"TableNames": []
}
```

4. Create a DynamoDB Table locally from the `create-person-table.json` file inside src using `aws dynamodb create-table --cli-input-json file://json/create-person-table.json --endpoint-url http://localhost:8000`

3. `sam build`

4. `sam local start-api` 
To run test your application locally on `http://127.0.0.1:3000`

5. After you have orchestrated the application as desired and tested it locally you can deploy it on cloudformation stack using
`sam deploy --guided`

