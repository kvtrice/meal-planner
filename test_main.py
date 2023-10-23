import main
from io import StringIO

# Test Get Calorie Target, and that the upper (3000) and lower (1400) limits are correctly allowed:
def test_get_calorie_target(monkeypatch):
    input_data = StringIO('1400\n2100\n3000\n')
    monkeypatch.setattr('sys.stdin', input_data)

    expected_values = [1400, 2100, 3000]

    for expected_value in expected_values:
        actual_value = main.get_calorie_target()
        assert actual_value == expected_value