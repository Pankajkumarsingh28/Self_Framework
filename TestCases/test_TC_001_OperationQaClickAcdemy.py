from Pages.Pg_qaclickAcdemy import OperationOnQAclickAcdemy
from Library import reportgen
from TestCases import conftest
import pytest

@pytest.mark.smoke
def test_verify_BrowserOpenining(self=None):
    #res=OperationOnQAclickAcdemy.OpenBrowser()
    OperationOnQAclickAcdemy.OpenBrowser()
    #return res
    OperationOnQAclickAcdemy.clickOnRadioButton()
    OperationOnQAclickAcdemy.selectDropdown()
    OperationOnQAclickAcdemy.Checkbox()




    #OperationOnQAclickAcdemy.CloseBroswser()

