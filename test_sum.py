"""
Name:
Edward Clark
Purpose:
Is to test applications making sure all the code works.
Date:
7/7/2025
"""

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_fail():
    assert sum([1, 1, 1]) == 6, "Should be 6"  # This one should fail

if __name__ == "__main__":
    test_sum()
    test_sum_fail()
    print("All tests ran")
