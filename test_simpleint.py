from simpleint import simple_interest

def test_simpleint_pos():
    assert simple_interest(2000, 8, 12) == 19200

def test_pos_zer():
    assert simple_interest(10000, 7, 0) == 0