#coding=utf-8

#登录
def login(self,username,password):
	driver = self.driver
	#driver.find_element_by_xpath("//a[@href='https://passport.nong12.com/uc/login.aspx?ReturnUrl=http://www.nong12.com/']").click()
	driver.implicitly_wait(30)
	driver.find_element_by_xpath("//input[@id='j_username']").clear()
	driver.find_element_by_xpath("//input[@id='j_username']").send_keys(username)
	driver.find_element_by_xpath("//input[@id='j_password']").clear()
	driver.find_element_by_xpath("//input[@id='j_password']").send_keys(password)
	driver.find_element_by_xpath("//a[@id='login_btn']").click()
	self.driver.implicitly_wait(30)

#退出
def logout(self):
	driver = self.driver
	driver.find_element_by_xpath("//a[@class='hover-color-green logout']").click()