import pytest
from pages.verticalpage import verticalpage


@pytest.mark.smoke
@pytest.mark.order(1)
# @pytest.mark.skip
def test_trad_vert_click(page):
   vert_tech= verticalpage(page)
   vert_tech.trading_menu()
   vert_tech.retail_ecom_menu()
   vert_tech.health_care_menu()
   vert_tech.fintech_menu()
   vert_tech.custom_app_menu()
  
  

   

    
    