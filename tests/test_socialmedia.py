import pytest
from pages.verticalpage import verticalpage
from pages.technologypage import technologypage
from pages.socialmedia import socialmediapage

@pytest.mark.smoke
@pytest.mark.order(5)
def test_socialmed_click(page):
   socialmed = socialmediapage(page)
   socialmed.trad_socialmedia_click()
