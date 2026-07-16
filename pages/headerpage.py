class headerpage:
   def __init__(self,page):
     self.page=page
     self.verticals=page.locator('(//a[text()="Verticals"])[1]')
     self.page.wait_for_timeout(5000)

# About us
     self.about_us=page.locator('(//a[text()="About us"])[1]')
# Blog
     self.blog=page.locator('(//a[text()="Blog"])[1]')  
# contact us
     self.contact_us=page.locator('(//a[text()="Contact us"])[1]')     
# Portfolio
     self.portfolio=page.locator('(//a[text()="Portfolio"])[1]')

   def portfolio_click(self):
      self.portfolio.click()
      self.page.wait_for_timeout(5000)
      self.page.go_back() 

   def about_us_click(self):
       self.about_us.click()
       self.page.wait_for_timeout(5000)
       self.page.go_back() 

   def blog_click(self):
       self.blog.click()
       self.page.wait_for_timeout(5000)
       self.page.go_back() 

   def contact_us_click(self):
       self.contact_us.click()
       self.page.wait_for_timeout(5000)
       self.page.go_back() 