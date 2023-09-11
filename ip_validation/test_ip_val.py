from ip_validation import validate

def test_correct():
    assert validate("9.1.2.9") == "Valid"
    assert validate("99.1.1.1") == "Valid"
    assert validate("255.0.0.0") == "Valid"
    assert validate("255.255.255.255") == "Valid"
    assert validate("255.99.1.2") == "Valid"
    assert validate("99.255.9.5") == "Valid"
    assert validate("85.96.33.21") == "Valid"
    assert validate("8.33.125.10") == "Valid"
    assert validate("127.0.0.1") == "Valid"
    assert validate("239.0.0.0") == "Valid"
    assert validate("2.239.2.2") == "Valid"
    assert validate("127.127.127.127") == "Valid"
    assert validate("249.249.249.249") == "Valid"



def test_invalid():
    assert validate("255255.0.0.0") == "Invalid"
    assert validate("300.25.25.25") == "Invalid"
    assert validate("35.256.3.2") == "Invalid"
    assert validate("35.5.256.36") == "Invalid"
    assert validate("26.36.25.25.24") == "Invalid"
    assert validate("w22.33.3.3") == "Invalid"
    assert validate("cat") == "Invalid"
    assert validate("25.25.25") == "Invalid"
    
