import os
import runpod
from huggingface_hub import upload_folder
import requests
import shutil

def handler(payload):
    try:
        print(payload)
        job_input = payload['input']
        post_body = {
            "upload_dir": job_input["upload_dir"],
            "repo_id": job_input["repo_id"],
            "repo_path": job_input["repo_path"],
            "write_token": job_input["write_token"],
        }
        upload_folder(job_input["upload_dir"], job_input["repo_id"], job_input["repo_path"], job_input["write_token"])
        shutil.rmtree(job_input["upload_dir"])
        response = requests.post(os.getenv("UPLOADER_URL", ""), data=post_body)
        return { "response": response.text }
    except Exception as e:
        return {
            "error": repr(e)
        }

        

runpod.serverless.start({ "handler": handler}) # Required.
