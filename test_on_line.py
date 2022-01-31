def test_online():
    p1 = (0,0)
    p2 = (5,0)
    p3x = 4
    from on_line import online
    p3y = online(p1,p2,p3x)
    assert p3y == 0
    