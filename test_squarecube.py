def test_num_multiplication(capsys):
    num = 4
    print(num * 2, num * 3)

    captured = capsys.readouterr()
    assert captured.out.strip() == "8 12"
