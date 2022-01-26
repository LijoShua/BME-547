def add_patient(patient_name, patient_id, age):
    new_patient = [patient_name, patient_id, age, []]   
    return new_patient
    
def main():
    db = []
    x = add_patient("Ann Ables", 342, 40)
    db.append(x)
    y = add_patient("Bob Boyles", 50, 50)
    db.append(y)
    z = add_patient("Chris Columbus", 111, 35)
    db.append(z)
    db.append(add_patient("David Dinkins", 22, 72))
    # print(x)
    # print(y)
    # print(z)
    # print(db)
    # print(db[1])
    # print(db[1][2])
    # patient = db[1]
    # patient_age = patient[2]
    
    # print(db[-1]) # Gives the last entry of a list
    # print(db[0:3]) # Up to but not including the third element.
    # s = "abcdef"
    # print(s[3:5])
    

    
    # for patient in db:
        # for item in patient:
            # print(item)
        
    found_patient = find_patient(db, 111)
    print(found_patient)  
    print(db)
    add_test_to_patient(db, 111, "HDL", 100)
    print(db)
    return db
    
def find_patient(db, id_no):
    for patient in db:
        if patient[1] == id_no:
            return patient
    return

def add_test_to_patient(db, id_no, test_name, test_result):
    patient = find_patient(db, id_no)
    test_tuple = (test_name, test_result)
    patient[3].append(test_tuple)

def print_directory(db):
    rooms = ["Room 13", "Room 12", "Room 99", "Room 3"]
    for i, patient in enumerate(db):
        print("Name: {} Room: {}".format(patient[0], rooms[i]))
    # for rooms, patient in zip(rooms, db):
        # print("{} - {}".format(patient[0], rooms))
        


if __name__ == "__main__":
    db=main()
    print_directory(db)
