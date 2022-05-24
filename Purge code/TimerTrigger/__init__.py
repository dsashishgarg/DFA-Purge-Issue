import logging
import azure.functions as func
import azure.durable_functions as df
from azure.durable_functions.models.DurableOrchestrationStatus import OrchestrationRuntimeStatus
from datetime import datetime, timedelta
import os


async def main(mytimer: func.Timer Request, starter: str):
    client = df.DurableOrchestrationClient(starter)
    created_time_from = datetime.min
    created_time_to = datetime.today()
    runtime_status = [OrchestrationRuntimeStatus.completed]
    response = await client.purge_instance_history_by(created_time_from, created_time_to, runtime_status)
    logging.info(response)
