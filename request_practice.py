import requests

# http://vcm-21170.vm.duke.edu:5001

message = {"user": "ben", "message": "sup"}

r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json=message)
print(r.text)

# r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/josh")
# print(r.text)