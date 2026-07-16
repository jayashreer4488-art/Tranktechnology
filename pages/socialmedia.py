class socialmediapage:
   def __init__(self,page):
     self.page=page
     self.verticals=page.locator('(//a[text()="Verticals"])[1]')
     self.page.wait_for_timeout(5000)


     self.facebook=page.locator('//img[@alt="Facebook"]')
     self.linkedin=page.locator('//img[@alt="LinkedIn"]')
     self.inst=page.locator('(//img[@alt="Instagram"])[1]')
     self.pinint=page.locator('(//img[@alt="Instagram"])[2]')
     self.twitter=page.locator('//img[@alt="Twitter"]')
     self.youtube=page.locator('//img[@alt="Youtube"]')
     self.quora=page.locator('//img[@alt="Quora"]')
     self.socialmedia_list=[self.facebook,self.linkedin,self.inst,self.pinint,self.twitter,self.youtube,self.quora]

   def trad_socialmedia_click(self):
       for i in self.socialmedia_list:
        i.scroll_into_view_if_needed()
        with self.page.expect_popup() as popup_info:
         i.click()
        new_tab = popup_info.value
        new_tab.wait_for_timeout(5000) 
        new_tab.close()
     