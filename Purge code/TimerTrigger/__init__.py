import logging
import azure.functions as func
import azure.durable_functions as df
from azure.durable_functions.models.DurableOrchestrationStatus import OrchestrationRuntimeStatus
from datetime import datetime, timedelta

async def main(mytimer: func.TimerRequest, starter: str):
    logging.warn("working")
    client = df.DurableOrchestrationClient(starter)
    created_time_from = datetime.min
    logging.warning(created_time_from)
    created_time_to = datetime.today()
    logging.warning(created_time_to)
    runtime_statuses = [OrchestrationRuntimeStatus.Completed]

    purgeHistoryResult = client.purge_instance_history_by(created_time_from, created_time_to, runtime_statuses)
    logging.warn(purgeHistoryResult.close)