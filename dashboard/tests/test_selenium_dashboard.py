import pytest
import selenium
from selenium.webdriver.common.keys import Keys


@pytest.mark.selenium
def test_dashboard_admin_login():
    """
    Test dashboard admin login.
    """
    driver = selenium.webdriver.chrome()
    driver.get("http://localhost:8000/admin/")
    driver.find_element_by_xpath()