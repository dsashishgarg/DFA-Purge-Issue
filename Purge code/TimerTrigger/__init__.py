import logging
import azure.functions as func
import azure.durable_functions as df
from azure.durable_functions.models.DurableOrchestrationStatus import OrchestrationRuntimeStatus
from datetime import datetime, timedelta

async def main(mytimer: func.TimerRequest, starter: str):
    logging.warning("Time Trigger App received a request")
    client = df.DurableOrchestrationClient(starter)
    created_time_from = datetime.min
    created_time_to = datetime.today()
    runtime_statuses = [OrchestrationRuntimeStatus.Completed]
    logging.warning("created_time_from: " + str(created_time_from))
    logging.warning("created_time_to: " + str(datetime.today()))
    logging.warning("runtime_statuses: " + str(runtime_statuses))

    purgeHistoryResult = await client.purge_instance_history_by(created_time_from, created_time_to, runtime_statuses)
    logging.warning(purgeHistoryResult)