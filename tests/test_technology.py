import pytest
from pages.verticalpage import verticalpage
from pages.technologypage import technologypage

@pytest.mark.smoke
# @pytest.mark.order(2)
# @pytest.mark.skip
def test_trading_click(page):
   trading = technologypage(page)
   trading.tech_menu_click()
   trading.mobapp_menu_click()
   trading.artificial_int_click()
   

    
    
