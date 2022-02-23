import requests

patientIDs = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/jyl23")
print(patientIDs.text)

bloodTypeDonor = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M1")
print(bloodTypeDonor.text)

bloodTypeRecip = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F4")
print(bloodTypeRecip.text)

answer = {"Name": "jyl23", "Match": "No"}
matched = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=answer)
print(matched.text)


