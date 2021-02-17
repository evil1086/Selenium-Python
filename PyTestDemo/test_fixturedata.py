

import pytest

from PyTestDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataload")
class TestExample2(BaseClass):

    # when we are returning something from the method then it is mandatory to pass fixure name as parameter under method
    def test_editProfile(self, dataload):
        log = self.getlogger()
        log.info(dataload[0])
        log.info(dataload[1])
        # print(dataload)

