import requests

out_data = {
   "name": "Joshua Li",
   "net_id": "jyl23",
   "e-mail": "joshua.li@duke.edu"
}
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_data)
print(r.text)

r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
print(r.text)
