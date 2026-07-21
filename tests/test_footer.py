import pytest
from pages.verticalpage import verticalpage
from pages.technologypage import technologypage
from pages.footerpage import footerpage

@pytest.mark.smoke
# @pytest.mark.order(4)
# @pytest.mark.skip
def test_trad_footer_click(page):
   footer_tech= footerpage(page)
   footer_tech.trad_footer_click()
   
  
