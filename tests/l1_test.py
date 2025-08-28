from tasks.l1 import hello


def test_console_hello_output(capfd):
    hello()
    out, err = capfd.readouterr()
    assert err == ""
    assert out == "Haloo!\n"

