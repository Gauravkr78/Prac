from New_Code.fxn import add, add1, sum_numbers

def test_add():
    assert add(2, 3) == 5

def test_add1(capsys):
    add1(3, 4)
    captured = capsys.readouterr()
    assert captured.out.strip() == "7"

def test_sum_numbers_valid():
    assert sum_numbers(10, 20) == 30

def test_sum_numbers_invalid():
    assert sum_numbers("10", 20) == 0
