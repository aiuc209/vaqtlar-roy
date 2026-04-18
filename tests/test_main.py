import pytest

def convert_time(milliseconds):
    seconds = milliseconds // 1000
    minutes = seconds // 60
    hours = minutes // 60
    seconds = seconds % 60
    minutes = minutes % 60
    return f"{hours} soat {minutes} minut {seconds} sekund"

def test_convert_time():
    assert convert_time(3661000) == "1 soat 1 minut 1 sekund"
    assert convert_time(3600000) == "1 soat 0 minut 0 sekund"
    assert convert_time(60000) == "0 soat 1 minut 0 sekund"
    assert convert_time(1000) == "0 soat 0 minut 1 sekund"
    assert convert_time(0) == "0 soat 0 minut 0 sekund"

def test_convert_time_invalid_input():
    with pytest.raises(TypeError):
        convert_time("123")
    with pytest.raises(TypeError):
        convert_time(None)

def test_convert_time_negative_input():
    with pytest.raises(ValueError):
        convert_time(-123)
