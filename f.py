from PIL import Image, ImageTk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import smtplib
from email.message import EmailMessage
import datetime
import webbrowser
from email.mime.text import MIMEText

url = f"https://www.makemytrip.com/flight/search?tripType=O&itinerary=MAA-BOM-25/01/2023&paxType=A-1_C-0_I-0&cabinClass=E&sTime=1670296032934&forwardFlowRequired=true&action=FLTSRCH&deptDate=$date_7&retnDate=&intl=false&cmp=SEM%7CD%7CDF%7CG%7CRoute%7CDF_Route_Bengaluru_Mumbai_Exact%7CDelhi_Mumbai_Exact%7CRSA%7C532427477422&s_kwcid=AL!1631!3!532427477422!e!!g!!delhi%20to%20mumbai%20flight%20status&ef_id=Cj0KCQiA1ZGcBhCoARIsAGQ0kkocyeNUuNJLVzvi9lFgFPm-Ya_QV4k6RsjuvN8LUKsC3xGxT7U8ooIaAn7kEALw_wcB:G:s&gclid=Cj0KCQiA1ZGcBhCoARIsAGQ0kkocyeNUuNJLVzvi9lFgFPm-Ya_QV4k6RsjuvN8LUKsC3xGxT7U8ooIaAn7kEALw_wcB&isSemFlow=true"

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
driver.implicitly_wait(10)
count = 1
body = """
"""
for i in range(0,10):
    if count<=5:
        try:
            try:
                fl_co = driver.find_element(By.XPATH, f'//*[starts-with(@id,"flight_list_item_{i}_")]//p[@class="boldFont blackText airlineName"]')
                fl_no = driver.find_element(By.XPATH, f'//*[starts-with(@id,"flight_list_item_{i}_")]//p[@class="fliCode"]')
                dep_air = driver.find_element(By.XPATH,f'//*[starts-with(@id,"flight_list_item_{i}_")]//div[@class="flexOne timeInfoLeft"]/p[@class="blackText"]')
                dep_time = driver.find_element(By.XPATH,  f'//*[starts-with(@id,"flight_list_item_{i}_")]//div[@class="flexOne timeInfoLeft"]/p[@class="appendBottom2 flightTimeInfo"]/span')
                arr_air = driver.find_element(By.XPATH, f'//*[starts-with(@id,"flight_list_item_{i}_")]//div[@class="flexOne timeInfoRight"]/p[@class="blackText"]')
                arr_time = driver.find_element(By.XPATH, f'//*[starts-with(@id,"flight_list_item_{i}_")]//div[@class="flexOne timeInfoRight"]/p[@class="appendBottom2 flightTimeInfo"]/span')
                duration = driver.find_element(By.XPATH, f'//*[starts-with(@id,"flight_list_item_{i}_")]//div[@class="stop-info flexOne"]/p')
                stops = driver.find_element(By.XPATH,f'//*[starts-with(@id,"flight_list_item_{i}_")]//p[@class="flightsLayoverInfo"]')
                price = driver.find_element(By.XPATH, f'//*[starts-with(@id,"flight_list_item_{i}_")]//p[@class="blackText fontSize18 blackFont white-space-no-wrap"]')
                if fl_co.text=="":
                    continue
                else:
                    body = body + f"""

Flight No.{count} 

Flight Name: {fl_co.text}
Flight Number: {fl_no.text}
Departure Airport: {dep_air.text}
Departure Time: {dep_time.text}
Arrival Airport: {arr_air.text}
Arrival Time: {arr_time.text}
Duration of Flight: {duration.text}
Number of Stops: {stops.text}

------------------------------------------"""
                    count = count + 1
            except:
                continue
        except: print("There is no internet")

msg=EmailMessage()
msg.set_content(body)
msg['From']='flightcrux16@gmail.com'
msg['To']='fardeenclan@gmail.com'
msg['Subject']="FlightCrux Flight Information"
smtpObj = smtplib.SMTP_SSL('smtp.gmail.com',465)
smtpObj.login ('flightcrux16@gmail.com', 'bpigukrmtcybhjhh')
smtpObj.send_message(msg)
smtpObj.quit()
print("Message Sent")





