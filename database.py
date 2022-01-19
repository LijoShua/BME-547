print("This is the database module and python calls it {}".format(__name__))

#import blood_calculator

#from blood_calculator import check_HDL, check_LDL

import blood_calculator as bc
import analysis

from blood_calculator import * #Imports all the functions; however, since this does not specify the module or the function being imported, it will be hard to trace a used function back to its respective module 

HDL_value = 55
#classification = blood_calculator.check_HDL(HDL_value)
#classification = check_HDL(HDL_value)
classification = bc.check_HDL(HDL_value)

print("55 is {}".format(classification))
x = bc.check_LDL(200)
