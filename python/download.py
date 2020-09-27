"""
	Pre-requisites:
	selenium needs to be installed (pip install selenium)
	Firefox
	Firefox should be configured to download/save PDF by default.
	geckodriver

	Things that have to be changed in this file:
	Insert your SRN in between the double quotes equated to the username variable
	Insert your password in between the double quotes equated to the password variable
	Insert path to the firefox profile you configured. (Note: A firefox profile with the pre-requisites has to be made in order for the script to run properly)

	Run as follows:
	python download.py <position_of_course_in_list> <unit_number> <slides_or_notes> <starting_lecture_number> <ending_lecture_number>	(pass 2 to download slides, 3 to download notes)
	example:
	python download.py 3 2 2 5 12
	Running the above code downloads slides of lectures 5-12(both inclusive) of the 2nd unit of the 3rd course in 'My Courses' list
"""

import time, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

def download(args):
	link = "https://pesuacademy.com/Academy/"
	username = "<Insert SRN here>"
	password = "<Insert Password here>"

	firefox_options = Options()
	firefox_options.add_argument('--headless')
	driver = webdriver.Firefox(firefox_profile='<Insert profile PATH here>',options=firefox_options)

	driver.get(link)
	un = driver.find_element_by_id('j_scriptusername')
	un.send_keys(username)
	pw = driver.find_element_by_name('j_password')
	pw.send_keys(password)
	driver.find_element_by_id('postloginform#/Academy/j_spring_security_check').click()

	for i in range(int(args[4]),int(args[5])+1):
		time.sleep(2)
		driver.find_element_by_id('menuTab_653').click()																							# Click 'My courses'
		time.sleep(2)
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div[3]/div/table/tbody/tr[' + args[1] + ']/td[2]').click()		# Click course name
		time.sleep(2)
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div[2]/div[1]/div/ul/li[' + args[2] + ']').click()						# Click on the desired unit
		time.sleep(2)
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div[' + str(i) +']').click()					# Click lecture number
		time.sleep(2)
		driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[' + args[3] + ']/a').click()										# Click 'slides' or 'notes' tab depending on user input

if __name__ == "__main__":
	download(sys.argv)