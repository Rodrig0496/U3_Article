import pytest

def test_successful_login():
    """
    Test a valid login scenario.
    """
    username = "admin"
    password = "password123"
    
    # Mock login logic
    is_logged_in = (username == "admin" and password == "password123")
    
    # We expect this test to PASS
    assert is_logged_in == True

def test_failed_login():
    """
    Test an invalid login scenario.
    """
    username = "admin"
    password = "wrongpassword"
    
    is_logged_in = (username == "admin" and password == "password123")
    
    # We expect this test to FAIL (because it returns False)
    assert is_logged_in == True
