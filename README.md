## Steps to run
- Clone the repository
- Navigate inside the repository
- Create an "uploads" directory
- Create Python Virtual Environment and activate it
- Install dependencies using
	```
	pip install -r requirements.txt
	```
- Run the below 2 commands in 2 different shells with virtual environment activated
	- Terminal-1:
		```
		uvicorn testapi:app --reload
		```
	- Temrinal-2:
		```
		rq worker task_queue
		```
- Now we can use the Endpoint API to upload the audio,
	```
	curl -X POST -F "file=@sample4.flac" http://localhost:8000/process
	```
- Now we can fetch the transcription using the below endpoint,
	```
	curl http://localhost:8000/job/JOBID
	```
