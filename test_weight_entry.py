import pytest


@pytest.mark.parametrize("input, expected", [
    ("22 lb", 10),
    ("50 kg", 50),
<<<<<<< HEAD
=======
    ("23.6 kg", 24),
    ("22 lbs", 10),
    # ("22lb",10),
    ("22 Lb", 10),
    ("22 LB", 10),
    ("-22 lb", -10),
    # ("ten kg", 10),
>>>>>>> b7d996b69d226c9a1f8eb8e49a8cbcdaa2654ca2
    ])
def test_parse_weight_input(input, expected):
    from weight_entry import parse_weight_input
    answer = parse_weight_input(input)
    assert answer == expected
<<<<<<< HEAD
=======


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0.1, 0.2, 0.3),
    ])
    
def test_add(a, b, expected):
    from weight_entry import add
    answer = add(a, b)
    assert answer == pytest.approx(expected)
>>>>>>> b7d996b69d226c9a1f8eb8e49a8cbcdaa2654ca2
