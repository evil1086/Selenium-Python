import pytest

'''
 Fixures are Fixtures are functions, which will run before each test function to which it is applied. Fixtures are 
 used to feed some data to the tests such as database connections, URLs to test and some sort of input data. Therefore, 
 instead of running the same code for every test, we can attach fixture function to the
 tests and it will run and return the data to the test before executing each test.
 
 A function is marked as a fixture by −
 @pytest.fixture'''

# This fixtures are applicable only for class level scope


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixures(self):
        print("i will be executing in fixtures")

    def test_fixures1(self):
        print("i will be executing1 in fixtures")

    def test_fixures2(self):
        print("i will be executing2 in fixtures")

    def test_fixures3(self):
        print("i will be executing3 in fixtures")


# This will executes after end of the fixtures scope
def test_fixture():
    print("I am out of fixure scope")



