from main import greet

def test_greet_output(capsys):
    greet("Vaishnavi")
    captured = capsys.readouterr()
    assert "Vaishnavi" in captured.out
