import pytest
from pages.verticalpage import verticalpage
from pages.technologypage import technologypage
from pages.headerpage import headerpage

@pytest.mark.smoke
# @pytest.mark.header
@pytest.mark.order(3)
def test_trad_header_click(page):
   header_tech= headerpage(page)
   header_tech.about_us_click()
   header_tech.blog_click()
   header_tech.contact_us_click()
   header_tech.portfolio_click()
   



    
    
