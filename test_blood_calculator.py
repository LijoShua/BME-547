# test_blood_calculator.py

import pytest

# def test_check_HDLnorm(): # Not great because we write 3 separate functions that # do very similar things

    # from blood_calculator import check_HDL
    # answer = check_HDL(70)
    # assert answer == "Normal"
    
# def test_check_HDLbordlow():
    # from blood_calculator import check_HDL
    # answer = check_HDL(50)
    # assert answer == "Borderline Low"
    
# def test_check_HDLlow():
    # from blood_calculator import check_HDL
    # answer = check_HDL(30)
    # assert answer == "Low"
    
# def test_check_HDL(): # Not great unit-testing practice
    # from blood_calculator import check_HDL
    # answer = check_HDL(70)
    # assert answer == "Normal"
    # answer = check_HDL(50)
    # assert answer == "Borderline Low"
    # answer = check_HDL(30)
    # assert answer == "Low"
    
    
@pytest.mark.parametrize("input_HDL, expected", [
    [70, "Normal"],
    [45, "Borderline Low"],
    [20, "Low"]
    ])
    
def test_check_HDL(input_HDL, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(input_HDL)
    assert answer == expected
    