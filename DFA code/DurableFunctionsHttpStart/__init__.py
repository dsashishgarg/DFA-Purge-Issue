# This function an HTTP starter function for Durable Functions.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable activity function (default name is "Hello")
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt
 
import logging
import json

import azure.functions as func
import azure.durable_functions as df


async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    request_body = req.get_json()
    client = df.DurableOrchestrationClient(starter)
    instance_id = await client.start_new("orchestrator" , None, request_body)

    logging.info(f"Started orchestration with ID = '{instance_id}'.")

    response = {"instance_id": instance_id}

    return func.HttpResponse(body=json.dumps(response))