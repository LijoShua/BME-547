import requests

server = "http://127.0.0.1:5000"
"""
new_patient = {"name": "Chris", "id": 203, "blood_type": "O+"}
r = requests.post(server + "/add_patient", json=new_patient)
print(r.status_code)
print(r.text)
"""

q = requests.get(server + "/get_results/101")
print(q.status_code)
print(q.text)
