class verticalpage:
   def __init__(self,page):
     self.page=page
     self.verticals=page.locator('(//a[text()="Verticals"])[1]')
     self.page.wait_for_timeout(5000)

#Trading
     self.trading=page.locator('(//img[@alt="trading"])[1]')
     self.stock_trade=page.locator('(//a [text()="Stock Trading"])[1]')
     self.paper_trade=page.locator('//a[text()="Paper Trading"]')
     self.CFD_trade=page.locator('(//a[text()="CFD Trading"])[1]')
     self.trad_dev_mass=page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
     self.custom_trade=page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
     self.web_portal=page.locator('(//a[text()="Web Portal Trading"])[1]')
     self.trad_list=[self.stock_trade,self.paper_trade,self.CFD_trade,self.trad_dev_mass,self.custom_trade,self.web_portal]
# Retail and Ecommerce
     self.retail_ecom=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
     self.ecom_web=page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
     self.ecom_app_web=page.locator('(//a[text()="eCommerce App Development"])[1]')
     self.retail_list=[self.ecom_web,self.ecom_app_web]
  #Health care
     self.health_care=page.locator('(//img[@alt="trading"])[3]')
     self.Diet_nutri=page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
     self.Health_track_app=page.locator('(//a[text()="Health tracking App"])[1]')
     self.health_list=[self.Diet_nutri,self.Health_track_app]
   #Fintech
     self.Fintech=page.locator('(//img[@alt="trading"])[4]')
     self.pos_software=page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
     self.crypto=page.locator('(//a[text()="Crypto"])[1]')
     self.fintech_list=[self.pos_software,self.crypto]
    #custome_app    
     self.custom_app=page.locator('(//img[@alt="trading"])[5]')
     self.desktop_app=page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
     self.hrm_dev=page.locator('(//a[text()="HRM Development"])[1]')
     self.travel=page.locator('(//a[text()="Travel"])[1]')
     self.dating_app=page.locator('(//a[text()="Dating App Development"])[1]')
     self.crm_dev=page.locator('(//a[text()="CRM Development USA"])[1]')
     self.erp=page.locator('(//a[text()="ERP App Development"])[1]')
     self.e_learn=page.locator('(//a[text()="E-Learning"])[1]')
     self.real_estate=page.locator('(//a[text()="Real Estate"])[1]')
     self.custom_list=[self.desktop_app,self.hrm_dev,self.travel,self.dating_app,self.crm_dev,self.erp,self.e_learn]
    
   def vertical_mouse_hover(self):
      self.verticals.hover()
    
   def trading_mouse_hover(self):
       self.trading.hover()

   def retail_ecom_mouse_hover(self):
       self.retail_ecom.hover()
     
   def health_care_mouse_hover(self):
       self.health_care.hover()
     
   def Fintech_mouse_hover(self):
       self.Fintech.hover()
    
   def custom_app_mouse_hover(self):
       self.custom_app.hover()

   def trading_menu(self):
      for i in self.trad_list:
        self.verticals.hover()
        self.trading.hover()
        i.click()
        self.page.wait_for_timeout(2000)  
        self.page.go_back()

   def retail_ecom_menu(self):
       for i in self.retail_list:
        self.verticals.hover()
        self.retail_ecom.hover()
        i.click()
        self.page.wait_for_load_state("load")
        self.page.go_back()

   def health_care_menu(self):
       for i in self.health_list:
        self.verticals.hover()
        self.health_care.hover()
        i.click()
        self.page.wait_for_timeout(2000)
        self.page.go_back()

   def fintech_menu(self): 
       for i in self.fintech_list:
        self.verticals.hover()
        self.Fintech.hover()
        i.click()
        self.page.wait_for_timeout(2000)
        self.page.go_back()

   def custom_app_menu(self):
        for i in self.custom_list:
         self.verticals.hover()
         self.custom_app.hover()
         i.click()
         self.page.wait_for_timeout(2000)
         self.page.go_back()
      
    
    



