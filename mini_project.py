import customtkinter
import gmplot
from customtkinter import *
from tkinter import messagebox
from tkinter import *
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
import mysql.connector

week_list = []
today = datetime.date.today()
for i in range(5):
    week_ago = today + datetime.timedelta(days=i)
    week_list.append(str(week_ago))
root= customtkinter.CTk()
root.geometry(f"{1290}x{730}")
root.wm_attributes('-transparent')
def btnclick():
    messagebox.showinfo("Window","You have clicked on this Button")

dic = {'BOM':[19.093706, 72.865046], 'BLR':[13.198382,77.714200], 'MAA':[12.995176,80.173890], 'CCU':[22.643127, 88.439002], 'DEL':[28.554248, 77.104266]}

var_email1=StringVar()
var_password1=StringVar()

def Login():
    def f():
        try:
            # Gmap - Gautham
            global dic
            lat = [dic[str(o_dep.get()[0:3])][0], dic[str(o_arr.get()[0:3])][0]]
            long = [dic[str(o_dep.get()[0:3])][1], dic[str(o_arr.get()[0:3])][1]]
            gmap = gmplot.GoogleMapPlotter(dic[str(o_dep.get()[0:3])][0], dic[str(o_dep.get()[0:3])][1], 8)
            gmap.scatter( lat, long,size = 40, marker = False )
            gmap.plot(lat, long, 'cornflowerblue', edge_width = 2.5)
            gmap.draw('/Users/fardeenmac/Documents/Documents/gmap1.html')
            webbrowser.open('file://' + os.path.realpath('/Users/fardeenmac/Documents/Documents/gmap1.html'))
        except:
            messagebox.showerror("Window","Please select All options")
    def click():
        if o_arr.get()==o_dep.get():
            messagebox.showerror("Window","Arrival and Departure Airport cant be the same")
        elif o_arr.get()=='Arrival Airport' or o_dep=='Departure Airport' or (o_dep=='Departure Airport' and o_arr=='Arrival Airport'):
            messagebox.showerror("Window",'Please select all options')
        else:
            try:
                url = f"https://www.makemytrip.com/flight/search?tripType=O&itinerary={o_dep.get()[0:3]}-{o_arr.get()[0:3]}-{go_date.get()[8:10]}/{go_date.get()[5:7]}/{go_date.get()[:4]}&paxType=A-{adults.get()}_C-{child.get()}_I-{inf.get()}&cabinClass=E&sTime=1670296032934&forwardFlowRequired=true&action=FLTSRCH&deptDate=$date_7&retnDate=&intl=false&cmp=SEM%7CD%7CDF%7CG%7CRoute%7CDF_Route_Bengaluru_Mumbai_Exact%7CDelhi_Mumbai_Exact%7CRSA%7C532427477422&s_kwcid=AL!1631!3!532427477422!e!!g!!delhi%20to%20mumbai%20flight%20status&ef_id=Cj0KCQiA1ZGcBhCoARIsAGQ0kkocyeNUuNJLVzvi9lFgFPm-Ya_QV4k6RsjuvN8LUKsC3xGxT7U8ooIaAn7kEALw_wcB:G:s&gclid=Cj0KCQiA1ZGcBhCoARIsAGQ0kkocyeNUuNJLVzvi9lFgFPm-Ya_QV4k6RsjuvN8LUKsC3xGxT7U8ooIaAn7kEALw_wcB&isSemFlow=true"
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
                count = 0
                body = f"""
Dear Customer, Please find the Available flight details from {o_dep.get()[4:]} to {o_arr.get()[4:]}
which have been ordered according to price of the tickets"""
                for i in range(0,20):
                    if count<5:
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
                                count += 1
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
Number of Adults: {adults.get()}
Number of Children: {child.get()}
Number of Infants: {inf.get()}
Price: Rs. {price.text[1:]}
------------------------------------------

"""

                        except:
                            continue
                body = body + f"""

For Booking Details go to:
https://www.makemytrip.com/flight/search?tripType=O&itinerary={o_dep.get()[0:3]}-{o_arr.get()[0:3]}-{go_date.get()[8:10]}/{go_date.get()[5:7]}/{go_date.get()[:4]}&paxType=A-{adults.get()}_C-{child.get()}_I-{inf.get()}&cabinClass=E&sTime=1670296032934&forwardFlowRequired=true&action=FLTSRCH&deptDate=$date_7&retnDate=&intl=false&cmp=SEM%7CD%7CDF%7CG%7CRoute%7CDF_Route_Bengaluru_Mumbai_Exact%7CDelhi_Mumbai_Exact%7CRSA%7C532427477422&s_kwcid=AL!1631!3!532427477422!e!!g!!delhi%20to%20mumbai%20flight%20status&ef_id=Cj0KCQiA1ZGcBhCoARIsAGQ0kkocyeNUuNJLVzvi9lFgFPm-Ya_QV4k6RsjuvN8LUKsC3xGxT7U8ooIaAn7kEALw_wcB:G:s&gclid=Cj0KCQiA1ZGcBhCoARIsAGQ0kkocyeNUuNJLVzvi9lFgFPm-Ya_QV4k6RsjuvN8LUKsC3xGxT7U8ooIaAn7kEALw_wcB&isSemFlow=true"""
                msg=EmailMessage()
                msg.set_content(body)
                msg['From']= 'flightcrux16@gmail.com'
                msg['To']= var_email1.get()
                msg['Subject']="FlightCrux Flight Information"
                smtpObj = smtplib.SMTP_SSL('smtp.gmail.com',465)
                smtpObj.login ('flightcrux16@gmail.com', 'bpigukrmtcybhjhh')
                smtpObj.send_message(msg)
                smtpObj.quit()
                messagebox.showinfo("window","Mail has been Sent")      
            except:
                messagebox.showerror("Window","Please check Internet Connection and try again")

    if var_email1.get()=='' or var_password1.get()=='' or (var_email1.get()=='' and var_password1.get()==''):
        messagebox.showerror("Window", "Please Fill in all the details")
    else:
        con=mysql.connector.connect(host="localhost",  user="root", password="Havind9123s@",database="mysql")
        my_cursor=con.cursor()
        my_cursor.execute("select * from register where email=%s and pass=%s",(var_email1.get(), var_password1.get()))
        row=my_cursor.fetchone()
        if row== None:
            messagebox.showerror("Error"," Invalid Username and Password")
        else:
            global bg2
            top=customtkinter.CTkToplevel()
            top.geometry(f"{1290}x{730}")
            top.title("logged in Successfully")
            image1=Image.open('image1.webp')
            img2=image1.resize((1290,730))
            bg2 = ImageTk.PhotoImage(img2)
            lblbg2=Label(top, image=bg2)
            lblbg2.place(x=0,y=0,relwidth=1,relheight=1)
            lbltitle = Label(top, bd=20, relief=RIDGE,text="WELCOME TO FLIGHTCRUX!!",fg="yellow",bg="black",font=("times new roman",50,"bold"))
            frame_login = Frame(top, bg = "black")
            frame_login.place(x=600, y=170,width=540,height=450)
            lbltitle.pack(side=TOP,fill=X)
            o_dep=customtkinter.CTkOptionMenu(frame_login, values=['BLR-Bangalore','MAA-Chennai','DEL-Delhi','BOM-Mumbai','CCU-Kolkata'])
            o_dep.place(x=40, y=50)
            o_arr=customtkinter.CTkOptionMenu(frame_login, values=['BLR-Bangalore','MAA-Chennai','DEL-Delhi','BOM-Mumbai','CCU-Kolkata'])
            o_arr.place(x=40, y=220)
            go_date = customtkinter.CTkOptionMenu(frame_login, values=week_list)
            go_date.place(x=40, y=140)
            c_btn = customtkinter.CTkButton(frame_login,text="Send Mail",bd=3,fg_color='black', border_color='red', command=click)
            send = customtkinter.CTkButton(frame_login, text='View Route', bd = 3, fg_color='black', border_color='red', command=f)
            send.place(x=110, y=300, width=120, height=45)
            c_btn.place(x=280,y=300,width=120,height=45)
            o_arr.set("Arrival Airport")
            o_dep.set('Departure Airport')
            adults_lbl = customtkinter.CTkLabel(frame_login, text="Number of Adults")
            adults_lbl.place(x=300, y=20)
            adults = customtkinter.CTkOptionMenu(frame_login, values=['0','1','2','3','4','5','6','7'])
            adults.place(x=300, y=50)
            adults.set('1')
            child_lbl = customtkinter.CTkLabel(frame_login, text="Number of Children")
            child_lbl.place(x=300, y=100)
            child = customtkinter.CTkOptionMenu(frame_login, values=['0','1','2','3','4','5','6','7'])
            child.place(x=300, y=140)
            child.set('0')
            inf_lbl = customtkinter.CTkLabel(frame_login, text="Number of Infants")
            inf_lbl.place(x=300, y=180)
            inf = customtkinter.CTkOptionMenu(frame_login, values=['0','1','2','3','4','5','6','7'])
            inf.place(x=300, y=220)
            inf.set('0')



def Register():
    def register():
        if var_fname.get()=="" or var_email.get()=="" or var_lname.get()=="" or var_age.get()=="" or var_DOB.get()=="" or var_contact.get()=="" or var_password.get()=="" or var_cpassword.get()=="":
            messagebox.showerror("Window", "All fields are required")
        elif var_password.get()!=var_cpassword.get():
            messagebox.showerror("Window", "Password and Confirm Password should be same. Please check again")
        else:
            try:
                con=mysql.connector.connect(host="localhost", user="root", password="Havind9123s@", database="mysql")
                my_cursor=con.cursor()
                query=("select * from register where email=%s")
                value=(var_email.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row != None:
                    messagebox.showerror("Error", "User already exists, please try another email ID")
                else:
                    my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s)",(var_fname.get(),
                                                                                              var_lname.get(),
                                                                                              var_DOB.get(),
                                                                                              var_age.get(),
                                                                                              var_contact.get(),
                                                                                              var_email.get(),
                                                                                              var_password.get(),
                                                                                              var_cpassword.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Window","You have successfully registered, Please login now!")
                root1.destroy()
            except:
                messagebox.showerror("Window","Please check if everything is correct")
# Tkinter register -- Hari Surya 
    root1 = Toplevel()
    root1.title("Register")
    root1.geometry("1200x700+0+0")
    var_fname=StringVar()
    var_lname=StringVar()
    var_DOB=StringVar()
    var_age=StringVar()
    var_contact=StringVar()
    var_email=StringVar()
    var_password=StringVar()
    var_cpassword=StringVar()
    global bg3
    image1=Image.open('bg_image.jpeg')
    img2=image1.resize((1290,730))
    bg3 = ImageTk.PhotoImage(img2)
    lblbg2=Label(root1, image=bg3)
    lblbg2.place(x=0,y=0,relwidth=1,relheight=1)

    frame=Frame(root1, bg="dark blue")


    reglbl = Label(frame,text="REGISTER HERE!", font=("times new roman",20,"bold"),fg="white",bg="dark blue")
    reglbl.place(x=20,y=20)

    fname = Label(frame,text="First Name", font=("times new roman",20,"bold"),bg="dark blue")
    fname.place(x=50,y=100)

    fnameent = Entry(frame,textvar=var_fname, font=("times new roman",20,"bold"))
    fnameent.place(x=50,y=140,width=250)

    txt_lname = Label(frame,text="Last Name", font=("times new roman",20,"bold"),bg="dark blue")
    txt_lname.place(x=370,y=100)

    lnameent = Entry(frame,textvar=var_lname, font=("times new roman",20,"bold"))
    lnameent.place(x=370,y=140,width=250)

    dob = Label(frame,text="DOB(YYYY-MM-DD)", font=("times new roman",20,"bold"),bg="dark blue")
    dob.place(x=50,y=180)

    txt_DOB = Entry(frame,textvar=var_DOB, font=("times new roman",20,"bold"))
    txt_DOB.place(x=50,y=220,width=250)

    age = Label(frame,text="Age", font=("times new roman",20,"bold"),bg="dark blue")
    age.place(x=370,y=180)

    txt_age = Entry(frame,textvar=var_age, font=("times new roman",20,"bold"))
    txt_age.place(x=370,y=220,width=250)

    contact = Label(frame,text="Contact No", font=("times new roman",20,"bold"),bg="dark blue")
    contact.place(x=50,y=260)

    txt_contact = Entry(frame,textvar=var_contact, font=("times new roman",20,"bold"))
    txt_contact.place(x=50,y=300,width=250)

    email = Label(frame,text="Email Address", font=("times new roman",20,"bold"),bg="dark blue")
    email.place(x=370,y=260)

    txt_email = Entry(frame,textvar=var_email, font=("times new roman",20,"bold"))
    txt_email.place(x=370,y=300,width=250)

    password = Label(frame,text="Password", font=("times new roman",20,"bold"),bg="dark blue")
    password.place(x=50,y=340)

    txt_password = Entry(frame,show="*",textvar=var_password, font=("times new roman",20,"bold"))
    txt_password.place(x=50,y=380,width=250)

    cpassword = Label(frame,text="Confirm Password", font=("times new roman",20,"bold"),bg="dark blue")
    cpassword.place(x=370,y=340)

    txt_cpassword = Entry(frame,show="*",textvar=var_cpassword, font=("times new roman",20,"bold"))
    txt_cpassword.place(x=370,y=380,width=250)

    egbtn = customtkinter.CTkButton(frame,text="Register Now!",borderwidth=0, fg_color='black', border_color='red', command=register)
    egbtn.place(x=230, y=450, width = 250)


# Tkinter Login -- Gautham

image=Image.open('bgimgfinal.jpeg')
img=image.resize((1290,730))
bg = ImageTk.PhotoImage(img)
lblbg=Label(root, image = bg)
lblbg.place(x=0,y=0,relwidth=1,relheight=1)
root.title("Welcome to Flightcrux")
frame = Frame(root, bg = "black")
frame.place(x=500, y=170,width=340,height=450)

lbltitle1 = Label(root,text="LOGIN",fg="light blue",bg="black",font=("times new roman",50,"bold"))
lbltitle1.place(x=570,y=220,width=200,height=50)

username = Label(frame,text="Email",font=("times new roman",20,"bold"),fg="white", bg = "black")
username.place(x=70,y=155)

txtuser=customtkinter.CTkEntry(frame,textvar=var_email1)
txtuser.place(x=40,y=190,width=270)

password = Label(frame,text="Password",font=("times new roman",20,"bold"),fg="white", bg = "black")
password.place(x=70,y=225)

txtpass=customtkinter.CTkEntry(frame,show="*",textvar=var_password1)
txtpass.place(x=40,y=260,width=270)

loginbtn = customtkinter.CTkButton(frame,text="Login",bd=3,fg_color='black', border_color='red', command=Login)
loginbtn.place(x=15,y=310,width=120,height=45)

regbtn = customtkinter.CTkButton(frame,text="New User Register",borderwidth=0, fg_color='black', border_color='red', command=Register)
regbtn.place(x=15,y=370,width=200)

root.mainloop()