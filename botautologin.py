Set browser = CreateObject("InternetExplorer.application")
browser.Statusbar = false
browser.Toolbar = false
browser.Menubar = false
browser.Visible = true

browser.Navigate("https://www.instagram.com/accounts/login/")

wscript.Sleep(5000)

wscript.Sleep(100)

#Fill username value
username_field = browser.find_element_by_name('username')
username_field.send_keys(name)
print(name)

#Fill password value
password_field  = browser.find_element_by_name('password')
password_field.send_keys('aa12345bb12345cc'+name) #You can determine another password here.

Set buttons = browser.Document.GetElementsByTagName("button")

buttons.Item(0).Click