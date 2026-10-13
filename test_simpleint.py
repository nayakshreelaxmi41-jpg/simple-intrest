from simpleint import simInt

def test_simpleint_pos():
    assert simInt(2000, 8, 12) == 19200

def test_pos_zer():
    assert simInt(10000, 7, 0) == 0