# import logging
# import azure.functions as func
# import requests


# def main(myblob: func.InputStream):
#     logging.info(f"Python blob trigger function processed blob \n"
#                  f"Name: {myblob.name}\n"
#                  f"Blob Size: {myblob.length} bytes")
#     # Trigger Databricks job
#     job_id = "499376165915367"
#     url = "https://adb-2343612122428095.15.azuredatabricks.net/api/2.0/jobs/run-now"

#     headers = {"Authorization": "Bearer dapi4ddd55be3e0aa4c74b1cefa580cf96ba"}
    
#     body = {"job_id": job_id}
#     response = requests.post(url, headers=headers, json=body)
#     if response.status_code != 200:
#         logging.error(f"Failed to trigger Databricks job with status code {response.status_code}")
#     else:
#         logging.info(f"Successfully triggered Databricks job")
import logging
import azure.functions as func
import requests

counter = 0
def main(myblob: func.InputStream, httpOutput: func.Out[func.HttpResponse]):
    global counter
    if counter == 0:
        logging.info(f"Python blob trigger function processed blob \n"
                    f"Name: {myblob.name}\n"
                    f"Blob Size: {myblob.length} bytes")
        
        # Trigger Databricks job
        job_id = "493796669050197" #from databrick => job id
        url = "https://adb-1747347507676475.15.azuredatabricks.net/api/2.0/jobs/run-now" #databrick url

        headers = {"Authorization": "Bearer dapi6b582337541c57e5a4c150f4c50a13a6-2"} #from user setting- generate new torkern

        body = {"job_id": job_id}
        response = requests.post(url, headers=headers, json=body)
        if response.status_code != 200:
            logging.error(f"Failed to trigger Databricks job with status code {response.status_code}")
            httpOutput.set(func.HttpResponse(f"Failed to trigger Databricks job with status code {response.status_code}"))
            logging.info(f"counter fail  {counter}") 
        else:
            counter += 1
            logging.info(f"Successfully triggered Databricks job")
            httpOutput.set(func.HttpResponse("Successfully triggered Databricks job"))
            logging.info(f"counter suc  {counter}")
    else:
        counter = 0
        logging.info(f"counter else  {counter}")


