class footerpage:
   def __init__(self,page):
     self.page=page
     self.verticals=page.locator('(//a[text()="Verticals"])[1]')
     self.page.wait_for_timeout(5000)

     #web development
     self.cms=page.locator('//a[text()="CMS Website Development"]')
    # web_dev=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[1]').click()
    # web_dev1=page.locator('//a[text()="Website Development"]').click()
     self.cust=page.locator('//a[text()="Custom Web Portal Development"]').click()
# App development
     self.ios_app_dev=page.locator('//a[text()="iOS App Development"]')
    # android_app_dev=page.locator('(//i[@class="fa fa-chevron-down text-red-2"])[2]')
    # android_app_dev1=page.locator('(//a[text()="Android App Development"])[2]')
     self.hybrid_app_dev=page.locator('//a[text()="Hybrid Mobile App Development"]')
     self.cross_app_dev=page.locator('//a[text()="Cross-Platform App Development"]')
     self.progres_app_dev=page.locator('//a[text()="Progressive Web App Development"]')

# Graphic Design
     self.logo_des=page.locator('//a[text()="Logo Design"]')
     self.ban_des=page.locator('//a[text()="Banner Design"]')
     self.pack_des=page.locator('//a[text()="Packaging Design"]')
     self.bus_card_des=page.locator('//a[text()="Business cards Design"]')

# UI UX development
     self.mob_app_des=page.locator('//a[text()="Mobile App Design"]')
     self.resp_web_des=page.locator('//a[text()="Responsive Web Design"]')
     self.brand_id_des=page.locator('//a[text()="Brand Identity Design"]')
     self.list_footer=[self.cms,self.ios_app_dev,self.hybrid_app_dev,self.cross_app_dev,self.progres_app_dev,self.logo_des,self.ban_des,self.pack_des,self.bus_card_des,self.mob_app_des,self.resp_web_des,self.brand_id_des]

   def trad_footer_click(self):
       for i in self.list_footer:
        i.scroll_into_view_if_needed()
        i.click()
        self.page.wait_for_timeout(3000)
        self.page.go_back()