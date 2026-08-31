import requests
import msal

app = msal.PublicClientApplication(
    "d3590ed6-52b3-4102-aeff-aad2292ab01c",
    authority="https://login.microsoftonline.com/common"
)

flow = app.initiate_device_flow(scopes=["https://api.fabric.microsoft.com/.default"])
print(flow["message"])

result = app.acquire_token_by_device_flow(flow)
headers = {"Authorization": f"Bearer {result['access_token']}"}

response = requests.get("https://api.fabric.microsoft.com/v1/deploymentPipelines", headers=headers).json()
for pipeline in response.get("value", []):
    print(f"\nPipeline: {pipeline['displayName']} (ID: {pipeline['id']})")
    stages_resp = requests.get(f"https://api.fabric.microsoft.com/v1/deploymentPipelines/{pipeline['id']}/stages", headers=headers).json()
    for stage in stages_resp.get("value", []):
        print(f"  - Stage: {stage['displayName']} | ID: {stage['id']}")
