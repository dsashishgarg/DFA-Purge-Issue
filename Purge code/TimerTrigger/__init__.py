import logging
import azure.functions as func
import azure.durable_functions as df
from azure.durable_functions.models.DurableOrchestrationStatus import OrchestrationRuntimeStatus
from datetime import datetime, timedelta

async def main(mytimer: func.TimerRequest, starter: str):
    client = df.DurableOrchestrationClient(starter)
    created_time_from = datetime.min
    created_time_to = datetime.today()
    runtime_statuses = [OrchestrationRuntimeStatus.Completed]
    purgeHistoryResult = client.purge_instance_history_by(created_time_from, created_time_to, runtime_statuses)
    logging.info(purgeHistoryResult)