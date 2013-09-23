from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.proxy import *
import time

print "\n"

print '''	*************WELCOME*************
	*			        *
	*		      	        *
	*			        *
	*BOT TO MAKE MULTIPLE CONNECIONS*
	*  	MYFREECAMS.COM		*
	*    DEVELOPED BY ANU YADAV	* '''


print "\n"

i=0

conn = raw_input("PLAESE ENTER THE NUMBER OF CONNECTIONS TO BE MADE :")

print "\n"

tt = conn*(50)

#tt1 = (tt)/(60)

print "THE MINIMUM TIME PERIOD IT WILL TAKE TO MAKE %s NUMBER OF CONNECTIONS :" % (tt)

print "\n"

for line in open('plist.txt'):
	if i>=conn:
		break
	else:
		myProxy = line
		print "proxy used to connect is %s " % (myProxy)
		proxy = Proxy({
		    'proxyType': ProxyType.MANUAL,
		    'httpProxy': myProxy,
		    'ftpProxy': myProxy,
		    'sslProxy': myProxy,
		    })
		display = Display(visible=0, size=(800, 600))
		display.start()
		driver = webdriver.Firefox(proxy=proxy)
		driver.get('http://www.myfreecams.com/')
		time.sleep(20)
		driver.get('http://www.myfreecams.com/#Sw3etSelena')
		driver.refresh()
		time.sleep(30)
		driver.quit()
		display.stop()
		i=i+1

#while i<5:
#	driver = webdriver.Firefox()
#	driver.get('http://www.myfreecams.com/')
#	time.sleep(20)
#	driver.get('http://www.myfreecams.com/#Sw3etSelena')
#	driver.refresh()
#	time.sleep(30)
#	i=i+1
