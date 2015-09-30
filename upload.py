import json
import requests

#url = "http://localhost:8080/alfresco/service/api/upload"
url = "http://alfresco.kbsoftware.co.uk:8080/alfresco/service/api/upload"
auth = ("patrick.kimber", "cognito")
files = {"filedata": open("test1.doc", "rb")}
data = {"siteid": "scratchpad", "containerid": "documentLibrary"}
r = requests.post(url, files=files, data=data, auth=auth)
print(r.status_code)
print(json.loads(r.text))
