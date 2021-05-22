# Each pytest files should be start with test_
# Each method should be start with test_ or end  with _test
# While execution from the CMD/conda prompt we need to  py.test , which will execute whole test under that directory
# py.test -v  - it will add the more details onto the cmd
# py.test -s - It will add more details on to the console
# py.test test_demo1.py -v -s - it will execute specific file
# py.test -m smoke -v -s  : it will execute specific marker methods in the files
# to generate html reporting we need to execute file like
# syntax: py.test --html=report.html
# if you want to build report for single file then py.test demo1.py --html=report.html 

import pytest


def test_firstProgramm(setup):
    print("Hello")

# To add marker at any mark we need to add @pytest.mark.marker-name
@pytest.mark.smoke
def test_greet():
    print("hey Good morning")


@pytest.mark.xfail
def test_creditcard():
    no = "123456789"
    assert no == "123456789", "Credid card number does not  matches"


def test_cross_browser(cross_browser):
    print(cross_browser[1])





