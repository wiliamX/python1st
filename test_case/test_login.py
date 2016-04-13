#coding=utf-8

from selenium import webdriver
import unittest
from public import login
import xml.dom.minidom

#打开xml 文档
dom = xml.dom.minidom.parse('D:\\test_project\\test_date\\login.xml')
#得到文档元素对象
root = dom.documentElement

class TestLogin(unittest.TestCase):
	def setUp(self):
		profiledir = webdriver.FirefoxProfile("C:\\Users\wanling19\\AppData\Roaming\\Mozilla\\Firefox\Profiles\\n3hhm1vt.default")
		self.driver = webdriver.Firefox(profiledir)
		self.driver.implicitly_wait(30)
		login = root.getElementsByTagName('url')
		self.base_url = login[0].firstChild.data
		self.verificationErrors = []

	def test_null(self):
		u'''账户名和密码都为空'''
		driver = self.driver
		driver.get(self.base_url)
		tagname = root.getElementsByTagName("null")
		username = tagname[0].getAttribute("username")
		password = tagname[0].getAttribute("password")
		prompt_info = tagname[0].firstChild.data
		login.login(self,username,password)
		text = driver.find_element_by_xpath("//p[@id='loginname_error']").text
		self.assertEqual(text,prompt_info)

	def test_right(self):
		u'''登录成功'''
		driver = self.driver
		driver.get(self.base_url)
		tagname = root.getElementsByTagName("right")
		username = tagname[0].getAttribute("username")
		password = tagname[0].getAttribute("password")
		prompt_info = tagname[0].firstChild.data
		login.login(self,username,password)
		text = driver.find_element_by_xpath("//div[@class='info clearfix']/a/em").text
		self.assertEqual(text,prompt_info)
		login.logout(self)

	def test_user_null(self):
		u'''账户名为空'''
		driver = self.driver
		driver.get(self.base_url)
		tagname = root.getElementsByTagName("user_null")
		username = tagname[0].getAttribute("username")
		password = tagname[0].getAttribute("password")
		prompt_info = tagname[0].firstChild.data
		login.login(self,username,password)
		text = driver.find_element_by_xpath("//p[@id='loginname_error']").text
		self.assertEqual(text,prompt_info)

	def test_pwd_null(self):
		u'''密码为空'''
		driver = self.driver
		driver.get(self.base_url)
		tagname = root.getElementsByTagName("pwd_null")
		username = tagname[0].getAttribute("username")
		password = tagname[0].getAttribute("password")
		prompt_info = tagname[0].firstChild.data
		login.login(self,username,password)
		text = driver.find_element_by_xpath("//p[@id='loginpwd_error']").text
		self.assertEqual(text,prompt_info)

	def test_error(self):
		u'''账户名和密码不匹配'''
		driver = self.driver
		driver.get(self.base_url)
		tagname = root.getElementsByTagName("error")
		username = tagname[0].getAttribute("username")
		password = tagname[0].getAttribute("password")
		prompt_info = tagname[0].firstChild.data
		login.login(self,username,password)
		text = driver.find_element_by_xpath("//p[@id='loginname_error' and @style='display: block;']").text
		self.assertEqual(text,prompt_info)

	def tearDown(self):
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)