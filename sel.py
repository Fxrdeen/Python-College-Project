from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import smtplib
from email.mime.text import MIMEText

url = f"https://www.makemytrip.com/flight/search?tripType=O&itinerary=BLR-BOM-16/12/2022&paxType=A-1_C-0_I-0&cabinClass=E&sTime=1670296032934&forwardFlowRequired=true&action=FLTSRCH&deptDate=$date_7&retnDate=&intl=false&cmp=SEM%7CD%7CDF%7CG%7CRoute%7CDF_Route_Bengaluru_Mumbai_Exact%7CDelhi_Mumbai_Exact%7CRSA%7C532427477422&s_kwcid=AL!1631!3!532427477422!e!!g!!delhi%20to%20mumbai%20flight%20status&ef_id=Cj0KCQiA1ZGcBhCoARIsAGQ0kkocyeNUuNJLVzvi9lFgFPm-Ya_QV4k6RsjuvN8LUKsC3xGxT7U8ooIaAn7kEALw_wcB:G:s&gclid=Cj0KCQiA1ZGcBhCoARIsAGQ0kkocyeNUuNJLVzvi9lFgFPm-Ya_QV4k6RsjuvN8LUKsC3xGxT7U8ooIaAn7kEALw_wcB&isSemFlow=true"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome('/Users/fardeenmac/Downloads/chromedriver', options=options)
driver.get(url)
wait = driver.implicitly_wait(5)

vid = driver.find_element("xpath",'//p[@class="blackText"]')
print(vid.text)

vid1 = driver.find_element("xpath", '//p[@class="fliCode"]')
print(vid1.text)

vid2 = driver.find_element("xpath", '//p[@class="boldFont blackText airlineName"]')
print(vid2.text)

vid3 = driver.find_element("xpath", '//p[@class="appendBottom2 flightTimeInfo"]')
print(vid3.text)



sender = 'flightcrux16@gmail.com'
receivers = ['fardeenclan@gmail.com']
subject = "Hello"
body = f"""
Departure Airport: {vid.text}
Flight Number: {vid1.text}
Flight company: {vid2.text}
Time: {vid3.text}
"""
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = ", ".join(receivers)
smtpObj = smtplib.SMTP_SSL('smtp.gmail.com',465)
smtpObj.login ('flightcrux16@gmail.com', 'bpigukrmtcybhjhh')
smtpObj.sendmail(sender, receivers, body)
print("Mail Sent")


# driver.close()
# '/Users/fardeenmac/Downloads/chromedriver'
# https://www.makemytrip.com/flight/search?tripType=O&itinerary=BLR-BOM-10/12/2022&paxType=A-1_C-0_I-0&cabinClass=E&sTime=1670296032934&forwardFlowRequired=true&action=FLTSRCH&deptDate=$date_7&retnDate=&intl=false&cmp=SEM%7CD%7CDF%7CG%7CRoute%7CDF_Route_Bengaluru_Mumbai_Exact%7CDelhi_Mumbai_Exact%7CRSA%7C532427477422&s_kwcid=AL!1631!3!532427477422!e!!g!!delhi%20to%20mumbai%20flight%20status&ef_id=Cj0KCQiA1ZGcBhCoARIsAGQ0kkocyeNUuNJLVzvi9lFgFPm-Ya_QV4k6RsjuvN8LUKsC3xGxT7U8ooIaAn7kEALw_wcB:G:s&gclid=Cj0KCQiA1ZGcBhCoARIsAGQ0kkocyeNUuNJLVzvi9lFgFPm-Ya_QV4k6RsjuvN8LUKsC3xGxT7U8ooIaAn7kEALw_wcB&isSemFlow=true

# https://www.kayak.co.in/horizon/sem/flights/destination/COK?lang=en&z_sig=465d81f1a912c65a&z_trk=tr56fb3fce9e35a8d1&skipapp=true&depart_date=2022-12-11&origin=BOM&gclid=CjwKCAiA-dCcBhBQEiwAeWidtfQ5WHZ3TsJVQmIzO-fByPD5q5v6BZf2Q70tYFFoZtHzxBGXwEoGkRoC9kMQAvD_BwE