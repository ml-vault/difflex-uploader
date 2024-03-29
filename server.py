import runpod
from huggingface_hub import upload_folder
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
        res = upload_folder(folder_path=job_input["upload_dir"],repo_id=job_input["repo_id"],path_in_repo= job_input["repo_path"],token= job_input["write_token"])
        if job_input["delete_after_upload"]:
            print("uploaded to hf")
            shutil.rmtree(job_input["upload_dir"])
            print("deleted")
        return { "response": f"upoaded {job_input['upload_dir']} to hf {job_input['repo_id']}:{job_input['repo_path']}" }
    except Exception as e:
        return {
            "error": repr(e)
        }

        

runpod.serverless.start({ "handler": handler}) # Required.
