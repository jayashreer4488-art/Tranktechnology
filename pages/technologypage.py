class technologypage:
   def __init__(self,page):
     self.page=page
     self.Tech=page.locator('(//a[text()="Technologies"])[1]')
     self.page.wait_for_timeout(5000)
# Ecommerce development
     self.ecom_dev=page.locator('//img[@alt="ecommerce"]')
     self.Magneto=page.locator('//a[text()="Magento Development"]')
     self.codeign=page.locator('(//a[text()="Codeigniter Development"])[1]')
     self.big_com=page.locator('(//a[text()="Big Commerce"])[1]')
     self.cs_cart=page.locator('(//a[text()="CS-Cart Development"])[1]')
     self.opn_cart=page.locator('(//a[text()="Opencart Development"])[1]')
     self.larvel_dev=page.locator('(//a[text()="Laravel Development"])[1]')
     self.drupal_dev=page.locator('(//a[text()="Drupal Development"])[1]')
     self.joomla_dev=page.locator('(//a[text()="Joomla Development"])[1]')
     self.exp_dev=page.locator('(//a[text()="Express JS Development"])[1]')
     self.word_press=page.locator('(//a[text()="WordPress Development"])[1]')
     self.shopify_dev=page.locator('(//a[text()="Shopify Development"])[1]')
     self.node_dev=page.locator('(//a[text()="Node JS Development"])[1]')
     self.woo_com=page.locator('(//a[text()="Woo Commerce"])[1]')
     self.pres_dev=page.locator('(//a[text()="Prestashop Development"])[1]')
     self.wix_dev=page.locator('(//a[text()="Wix Development"])[1]')
     self.react_dev=page.locator('(//a[text()="React JS Development"])[1]')
     self.list_ecom=[self.Magneto,self.codeign,self.big_com,self.cs_cart,self.opn_cart,self.larvel_dev,self.drupal_dev,self.joomla_dev,self.exp_dev,self.word_press,self.shopify_dev,self.node_dev,self.woo_com,self.pres_dev,self.wix_dev,self.react_dev]
#Mobile app development
     self.mobapp=page.locator('//strong[text()="Mobile App Development"]')
     self.a=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
     self.b=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
     self.c=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
     self.d=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
     self.e=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
     self.f=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
     self.g=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
     self.h=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
     self.list_mob=[self.a,self.b,self.c,self.d,self.e,self.f,self.g,self.h]

#Artifical intelligence
     self.AI=page.locator('//strong[text()="Artificial Intelligence"]')

     
   def tech_mouse_hover(self):
       self.Tech.hover()

   def mobapp_mouse_hover(self):
       self.mobapp.hover()
  
   def tech_menu_click(self):
      for i in self.list_ecom:
        self.Tech.hover()
        self.ecom_dev.hover()
        i.click()
        self.page.wait_for_timeout(2000)
        self.page.go_back() 

   def mobapp_menu_click(self):
      for i in self.list_mob:
        self.Tech.hover()
        self.mobapp.hover()
        i.click()
        self.page.wait_for_timeout(5000)
        self.page.go_back() 

   def artificial_int_click(self):
        self.Tech.hover()
        self.AI.click()
        self.page.wait_for_timeout(3000)
        self.page.go_back() 

   

   

 

    