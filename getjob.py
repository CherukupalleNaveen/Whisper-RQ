from redis import Redis
from rq import Queue
from rq.job import Job
from pydantic import BaseModel

jobID = input("Enter the job ID: ")

redis_conn = Redis(host="localhost", port=6379)
task_queue = Queue("task_queue", connection=redis_conn)

job = Job.fetch(jobID, connection=redis_conn)
print("Job Status: " + job.get_status())
print("Job result: " + job.result)