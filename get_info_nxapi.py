import requests
import json


payload={
    "aaaUser":{
        "attributes":{
            "name":"username",
            "pwd":"password"
        }
    }
}

url1='http://10.82.138.114/api/aaaLogin.json'
response1 = requests.post(url=url1, data=json.dumps(payload)).json()
headers={'Cookie': 'APIC-Cookie=' + response1['imdata'][0]['aaaLogin']['attributes']['token']}

url2='http://10.82.138.114/api/node/mo/sys/bd/bd-[vlan-1].json'
response2 = requests.get(url=url2, headers=headers).json()
