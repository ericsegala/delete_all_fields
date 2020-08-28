import http.client
import mimetypes
conn = http.client.HTTPSConnection("api.withleaf.io")
payload = ''
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJlcmljQHdpdGhsZWFmLmlvIiwiYXV0aCI6IlJPTEVfVVNFUiIsImV4cCI6MTYwMTIxMzk2MH0.rLS9zKlRXNQWiCWft6URib6Q6-L5TViIPL5pesIh5u7eReqdaiyi7GQPyEuoufsrtCvGk8qlOAr0143i7Fe_Ng'
}
conn.request("GET", "/services/fields/api/fields", payload, headers)
res = conn.getresponse()
data = res.read()
# print(data.decode("utf-8"))
import json
data = data.decode('utf-8')
data = json.loads(data)
d = json.dumps(data, indent=2, sort_keys=True)

import http.client
import mimetypes
for i in data:
    conn = http.client.HTTPSConnection("api.withleaf.io")
    payload = ''
    headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJlcmljQHdpdGhsZWFmLmlvIiwiYXV0aCI6IlJPTEVfVVNFUiIsImV4cCI6MTYwMTIxMzk2MH0.rLS9zKlRXNQWiCWft6URib6Q6-L5TViIPL5pesIh5u7eReqdaiyi7GQPyEuoufsrtCvGk8qlOAr0143i7Fe_Ng',
    'Content-Type': 'application/json'
    }
    conn.request("DELETE", f"/services/fields/api/users/{i['leafUserId']}/fields/{i['id']}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))