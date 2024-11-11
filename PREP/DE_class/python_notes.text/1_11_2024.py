++++++++++++++++++
8:05 AM 11/1/2024
++++++++++++++++++

*******************
 GCP Data Engineer
******************* 

Cloud Run Functions:(Gen1, Gen2)

Develop, Deployment and Scheduling:


1. HTTP Trigger CRF:
    Console: Done...
    IDE(Cloud SDK from Local Machine):
    
IDE(Cloud SDK from Local Machine):
Step 1:
VSCode:(Folder Structure):
MainFolder:
    |
    |-> CloudFunctions:
            |
            |-->GCSEvents
            |
            |-->PubSub
            |
            |-->HTTPTriggers:
                 |
                 |-->basic-http-trigger
                 |     |->main.py
                 |     |->requirements.txt
                 |
                 |-->bigquery-to-gsheets
    
Step 2:
Enable Python Virtual Environment:
Change to your project directory
PS C:\GCP-Cloud-DE\SuperGCP\Workflows> cd C:\GCP-Cloud-DE\SuperGCP\Cloud-Run-Functions
or
cd your-project # change the directory

Step 3: Create virtual environment by running the following command.
py -m venv env

Step 4: Activate venv 
.\env\Scripts\activate

Step 5: Developemnt, Deployement, Testing

Step 6: Deactivate venv
deactivate

================================================================================================:

main.py:

import functions_framework

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using make_response
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return 'Hello {}!'.format(name) 
    # in http request triggers - return statement while comming out of the logic is mandatory.
    
    
    
requirements.txt:
functions-framework==3.*
functions-framework


======================================================================================================:
Cloud Run Functions Deployment Command:
gcloud functions deploy localhttp-test-func 
    --runtime python311 
    --trigger-http 
    --allow-unauthenticated 
    --entry-point hello_http_trigger  
    

    
2. GCS Events:
    Console:
    IDE(Cloud SDK from Local Machine):

3. PubSub Events:
    Console:
    IDE(Cloud SDK from Local Machine):
    
    
    
    
Analasis Ticket:
----------------
What is the use and why should we have a virtual environment for any programmable development - like python?



Functions Back End Services Running:
  Deploying function...
  |  [Build] Build in progress... Logs are available at  [https://console.cloud.google.com/cloud-build/builds;region=us-centra
  l1/ce73e0b4-0b38-4529-bf45-3bfd6fc709b9?project=840233991363] *
  .  [Service]
  .  [ArtifactRegistry] * 
  .  [Healthcheck]
  .  [Triggercheck]

    
User Customised Cloud Run Function for HTTP Request:
-----------------------------------------------------
main.py:

import functions_framework

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function"""
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return name
    
    
 
Assignment1:
------------
Write a cloud run function using http trigger which returns the square of a digit we pass a argument to the function while calling it.

?name=3

3 --> 9

10 ---> 100


Assignment2:
Write a GCP CRF which can be triggerd using http request - which in return get the top 10 rows of a bigquery table we are passing as an argument to the funciton calling.

name=orders

orders -

top 10 records

sales

top 10 records


customer

top 10 records 


Error:

ERROR: (gcloud.functions.deploy) OperationError: code=3, message=Could not create or update Cloud Run service localhttp-test-func, Container Healthcheck failed. Revision 'localhttp-test-func-00003-huq' is not ready and cannot serve traffic. The user-provided container failed to start and listen on the port defined provided by the PORT=8080 environment variable within the allocated timeout. This can happen when the container port is misconfigured or if the timeout is too short. The healtcheck timeout can be extended. Logs for this revision might contain more information.







