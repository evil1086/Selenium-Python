import pytest
# conftest file is a generalize file for the fixures

# scope defines the scope of the fixures class scope only applicable for the class level
# it executes before the class and yield after completion of class execution


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    # from yield keyword to the end of the method this block will execute at the end of fixtures
    yield
    print("I will be executing at the last ")


@pytest.fixture()
def dataload():
    print("this is an example of fixure with passing data")
    return ["Vinod", "Pawar", "HereIAm "]


# This is an example of parameterize fixtures
# here we can wrap the data into single tuple and pass as an single index
@pytest.fixture(params=[("Chrome", 1020), ("Firefox",12345), ("Safari", 456646)])
def cross_browser(request):
    # it will invokes the each parameter while returning
    return request.param
