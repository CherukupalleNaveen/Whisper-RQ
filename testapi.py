from fastapi import FastAPI, UploadFile, File
from redis import Redis
from rq import Queue
from rq.job import Job
from pydantic import BaseModel
from transcribe import transcribe
import uuid
import os

app = FastAPI()
redis_conn = Redis(host="localhost", port=6379)
task_queue = Queue("task_queue", connection=redis_conn)

# class JobData(BaseModel):
#     audio_path : str

@app.get("/")
def index():
    return {
        "success": True,
        "message": "pong"
    }

@app.post("/process")
async def post_job(file: UploadFile = File(...)):
    i = str(uuid.uuid4())
    filename = i + os.path.splitext(file.filename)[1]
    file_path = os.path.join('/media/naveen/253eda55-9f25-43e1-a970-07c1269e1cbe/Projects/temp/Ozonetel/Task1/uploads', filename)
    with open(file_path, "wb") as f:
        f.write(await file.read())
    print("Your response will be available at the ID: " + i)
    data=[]
    data.append(file_path)
    data.append(i)
    job_instance = task_queue.enqueue(transcribe,data,job_id=i)
    return {
        "success": True,
        "job_id": i,
        "filename": filename
    }
@app.get("/job/{jobID}")
async def get_job(jobID: str):
    file_path = "/media/naveen/253eda55-9f25-43e1-a970-07c1269e1cbe/Projects/temp/Ozonetel/Task1/uploads/"+ jobID + ".txt"
    transcription=""
    with open(file_path, "r") as text_file:
        transcription = text_file.read()
    return {
        "jobID": jobID,
        "Transcription": transcription
    }