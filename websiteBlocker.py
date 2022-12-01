#importing required library
from tkinter import *
#creating a window
window = Tk()
window.geometry('700x500')
window.minsize(700,500)
window.maxsize(700,500)
window.title("Website Blocker")

heading=Label(window, text ='Website Blocker' , font ='arial')
heading.pack()

# path to the host file in windows
host_path ='C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

label1=Label(window, text ='Enter Website :' , font ='arial 13 bold')
label1.place(x=5 ,y=60)

enter_Website = Text(window,font = 'arial',height='2', width = '40')
enter_Website.place(x= 140,y = 60)

#function to block websites
def Blocker():
    # list of websites that you want to block
    website_lists = enter_Website.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for web in Website:
            # checking whether the hostname is already mapped
            if web in file_content:
                display=Label(window, text = 'Already Blocked' , font = 'arial')
                display.place(x=200,y=200)
                pass
            else:
                # mapping hostnames to your localhost IP address
                host_file.write(ip_address + " " + web + '\n')
                Label(window, text = "Blocked", font = 'arial').place(x=230,y =200)

# function to unblock websites
def Unblock():
    # list of websites that you want to unblock
    website_lists = enter_Website.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.readlines()
    for web in Website:
            if web in website_lists:
                with open (host_path , 'r+') as f:
                    for line in file_content:
                        # unmapping the hostname if it is mapped
                        if line.strip(',') != website_lists:
                            f.write(line)
                            Label(window, text = "UnBlocked", font = 'arial').place(x=350,y =200)
                            pass
                        else:
                            # if hostname is not mapped
                            display=Label(window, text = 'Already UnBlocked' , font = 'arial')
                            display.place(x=350,y=200)

# creating buttons
block_button = Button(window, text = 'Block',font = 'arial',pady = 5,command = Blocker ,width = 6, bg = 'red', activebackground = 'grey')
block_button.place(x = 230, y = 150)

unblock_button = Button(window, text = 'UnBlock',font = 'arial',pady = 5,command = Unblock ,width = 6, bg = 'green', activebackground = 'grey')
unblock_button.place(x = 350, y = 150)
window.mainloop()
