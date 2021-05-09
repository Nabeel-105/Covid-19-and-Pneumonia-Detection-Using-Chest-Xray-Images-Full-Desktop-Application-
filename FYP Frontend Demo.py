# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 20:00:37 2020

@author: Moiz
"""
from tkinter.filedialog import *

from tkinter import *
from tkinter import ttk
from tkinter.ttk import*

import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
import witkets as wtk
from tkinter import filedialog
from tkinter import messagebox
import os
import tempfile
from PIL import Image,ImageTk
import cv2
import csv
import re
import time
import datetime
from pathlib import Path
#import PyPDF2
from fpdf import FPDF
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
from reportlab.lib import colors
from covidpneumonia_testingmodel import covidtest

fln=None

root=Tk()
root.title("Covid-19 & Pneumonia Detector")
root.geometry("833x620")
root.maxsize(833,620)
root.minsize(833,620)
root.wm_iconbitmap("icn.ico")
root.config(bg="#FFFFF0")
#root = wtk.Style()
#root.introspect('TLabel')

root.style=Style()
style=ThemedStyle(root)
style.set_theme("radiance")
#scidgrey, aquativo,clearlooks,equilux,plastik,radiance,smog, xpnative (good one)

#TO apply themes
#root.style.theme_use("clam")
#('clam','alt','default','classic')

fname=StringVar()
age=StringVar()
bgname=StringVar()
#bgsign=StringVar()
gender_choice=StringVar()
cnic=StringVar()


#menu bar code

def menuexit():
    root.destroy()
def menuhelp():
    messagebox.showinfo("Help","PLease load your X-Ray image, then click test to complete your detection of Covid-19 or Pneumonia.")  
  
menubar=Menu(root)
firstmenu=Menu(menubar,tearoff=0)
#creating menu
firstmenu.add_separator()
firstmenu.add_command(label="Exit" , command=menuexit)

#add menu to menu bar
menubar.add_cascade(label="File" , menu=firstmenu)

menubar.add_cascade(label="Help" ,command=menuhelp)

root.config(menu=menubar)


def showimage():
    global fln
    a_fname=fname.get()
    a_gender_choice=gender_choice.get()
    a_age=age.get()
    a_bgname=bgname.get()
    #a_bgsign=bgsign.get()
    a_cnic=cnic.get()
    
    
    
        
    if(a_fname=="" or a_age=="" or a_age=="0" or a_cnic==""):
            messagebox.showerror("Error","Please insert correct details")
            fname.set("")
            age.set("")
            cnic.set("")
        
    elif(a_gender_choice==""):
            messagebox.showerror("Error","Please insert correct gender")
            
            
    elif(a_bgname=="Select"): #(or a_bgsign=="Select"):
            messagebox.showerror("Error","Please select blood group")
           
            
    elif (a_fname!="" or a_age!="" or a_age!=0 or  a_cnic!="" or a_gender_choice!="" or a_bgname!="Select"): #(or a_bgsign!="Select"):
        #RegEx
        pattern1 = '^[ a-zA-Z]*$'
        if re.search(pattern1, a_fname):
            pattern2='^[1-9]?[0-9]{1}$|^100$'
            if re.search(pattern2, a_age):
                pattern3='^[0-9+]{5}-[0-9+]{7}-[1-9]{1}$'
                if re.search(pattern3, a_cnic):
                    fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File" , filetypes=(("PNG file","*.png"),("JPG File","*.jpg"),("All Files","*.*")))
                    img=Image.open(fln)
                    img.thumbnail((220,220))
                    img=ImageTk.PhotoImage(img)
                    lab2.pack()
                    lab2.configure(image=img)
                    lab2.image=img
                    btn3=Button (wrapper2, text="Test",command=open_window1).grid(row=1,column=1,padx=10,pady=10)
                else:
                    messagebox.showerror("Error","Please insert CNIC")
                    cnic.set("")
             
            else:
                messagebox.showerror("Error","Please insert correct Age")
                age.set("")
        else:
            messagebox.showerror("Error","Please insert correct Name")
            fname.set("") 
            
def open_window1():
       global fln
       global classnum
       a_fname=fname.get()
       a_gender_choice=gender_choice.get()
       a_age=age.get()
       a_bgname=bgname.get()
       #a_bgsign=bgsign.get()
       a_cnic=cnic.get()
       
       if not fln:
           messagebox.showerror('Error','Upload image')
           return
       
  
       
       if(a_fname=="" or a_age=="" or a_age=="0" or a_cnic==""):
            messagebox.showerror("Error","Please insert correct details")
            fname.set("")
            age.set("")
            cnic.set("")
        
       elif(a_gender_choice==""):
            messagebox.showerror("Error","Please insert correct gender")
            
            
       elif(a_bgname=="Select"): #(or a_bgsign=="Select"):
            messagebox.showerror("Error","Please select blood group")
           
            
       elif (a_fname!="" or a_age!="" or a_age!=0 or  a_cnic!="" or a_gender_choice!="" or a_bgname!="Select"): #(or a_bgsign!="Select"):
        #RegEx
        pattern1 = '^[ a-zA-Z]*$'
        if re.search(pattern1, a_fname):
            pattern2='^[1-9]?[0-9]{1}$|^100$'
            if re.search(pattern2, a_age):
                pattern3='^[0-9+]{5}-[0-9+]{7}-[1-9]{1}$'
                if re.search(pattern3, a_cnic):
                    
                  
                      top1=Toplevel()
                      top1.title("Loading")
                      top1.geometry("350x50")
                      top1.maxsize(350,50)
                      top1.minsize(350,50)        
                      top1.overrideredirect(True) 
                      #for hiding window bar
                      
                      root_x = top1.winfo_rootx()
                      root_y = top1.winfo_rooty()
                    
                        # add offset
                      win_x = root_x + 300
                      win_y = root_y + 200
                      
                    
                      top1.geometry(f'+{win_x}+{win_y}')  # set toplevel in new position
                      #progressbar code
                      progress = Progressbar(top1, orient = HORIZONTAL, length = 300, mode = 'determinate', maximum=100, value=0) 
                      progress.pack(pady = 10)
                        #progress bar code https://www.askpython.com/python-modules/tkinter/tkinter-spinbox-and-progressbar-widgets
                      top1.update()
                      progress['value'] = 0
                      top1.update()
                      while progress['value'] < 100:
                            progress['value'] += 10
                        # Keep updating the top1 object to redraw the progress bar
                            top1.update()
                            time.sleep(0.5)
                            
                     #testing of covid pneumonia
                      classnum = covidtest(fln)
                      
                      top1.destroy()
                  
                      #New window of reportt
                        
                      top2=Toplevel()
                      top2.title("Report")
                      top2.geometry("750x500")
                      top2.maxsize(750,600)
                      top2.minsize(750,600)
                      top2.wm_iconbitmap("icn.ico")
                     
                      
                      
                      wrapper4=LabelFrame(top2,text="")
                      wrapper4.pack(padx=10,pady=10,fill="both",expand="no")
                      lblheading1=Label(wrapper4,text="Patient Report",font=('Arial',24,"bold")).grid(row=0,column=0,padx=10,pady=10)
                        #displayed data of form to new window
                      lbl6=Label(wrapper4, text="Full Name",font="bold").grid(row=1,column=0,padx=10,pady=10)
                      a=fname.get()   
                      lbla=Label(wrapper4, text=a).grid(row=1,column=2,padx=10,pady=10)
                        
                      lbl7=Label(wrapper4, text="Gender",font="bold").grid(row=2,column=0,padx=10,pady=10)
                      b=gender_choice.get()
                      lblb=Label(wrapper4, text=b).grid(row=2,column=2,padx=10,pady=10)
                        
                      lbl8=Label(wrapper4,text="Age",font="bold").grid(row=3,column=0,padx=10,pady=10)
                      c=age.get()
                      lblc=Label(wrapper4, text=c).grid(row=3,column=2,padx=10,pady=10)
                        
                      lbl9=Label(wrapper4, text="Blood Group",font="bold").grid(row=4,column=0,padx=10,pady=10)
                        
                        
                      d=bgname.get()
                      lbld=Label(wrapper4, text=d).grid(row=4,column=2,padx=10,pady=10)
                        #e=bgsign.get()
                        
                        #lble=Label(wrapper4,text=e).grid(row=4,column=3,padx=10,pady=10)
                      
                      lbl5=Label(wrapper4, text="Report Date,Time",font="bold")
                      lbl5.grid(row=5,column=0,padx=10,pady=5)
                    
                        
                        
                      dt_time = time.localtime() # gets time
                      timeprint=time.strftime("%m/%d/%Y, %I:%M:%S", dt_time)
                        
                      lbl10=Label(wrapper4,text=time.strftime("%m/%d/%Y, %I:%M:%S", dt_time)) # %I is for time format for 12 hrs, %H is for 24 hrs
                      lbl10.grid(row=5, column=2,padx=10,pady=10)
                        
                      lbl12=Label(wrapper4, text="CNIC",font="bold")
                      lbl12.grid(row=6,column=0,padx=10,pady=5)
                        
                      
                            
                      f=cnic.get()
                      lbl13=Label(wrapper4, text=f).grid(row=6,column=2,padx=10,pady=10)
                      
                      lblheading2=Label(wrapper4,text="Result",font=('Arial',24,"bold")).grid(row=7,column=0,padx=10,pady=10)
                       
                      
                      lbl14=Label(wrapper4, text="Covid-19",font="bold")
                      lbl14.grid(row=8,column=0,padx=10,pady=5)
                      
                      lbl15=Label(wrapper4, text="Pneumonia",font="bold")
                      lbl15.grid(row=9,column=0,padx=10,pady=5)
                      
                      if classnum==0:
                          lbl16=Label(wrapper4, text="Positive").grid(row=8,column=2,padx=10,pady=10)
                          lbl17=Label(wrapper4, text="Negative").grid(row=9,column=2,padx=10,pady=10)
                          Pneumonia="Negative"
                          Covid="Positive"
                          
                      elif classnum==1:
                           lbl16=Label(wrapper4, text="Negative").grid(row=8,column=2,padx=10,pady=10)
                           lbl17=Label(wrapper4, text="Negative").grid(row=9,column=2,padx=10,pady=10)
                           Pneumonia="Negative"
                           Covid="Negative"
                          
                           
                      elif classnum==2:
                           lbl17=Label(wrapper4, text="Positive").grid(row=9,column=2,padx=10,pady=10)
                           lbl16=Label(wrapper4, text="Negative").grid(row=8,column=2,padx=10,pady=10)
                           Pneumonia="Positive"
                           Covid="Negative"
    
                      if classnum!=0 and classnum!=1 and classnum!=2:
                           lbl16=Label(wrapper4, text="").grid(row=8,column=2,padx=10,pady=10)
                           lbl17=Label(wrapper4, text="").grid(row=9,column=2,padx=10,pady=10)
                      
                      
                      def close():
                        global fln
                        top2.destroy()
                        fname.set("")
                        age.set("")
                        cnic.set("")
                        lab2.pack_forget()
                        fln=None
                    
                        
                      def print_report():
                        
                        from reportlab.lib.enums import TA_JUSTIFY
                        from reportlab.lib.pagesizes import letter
                        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
                        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
                        from reportlab.lib.units import inch
                        from reportlab.lib import colors
                        
                                
                        
                    
                        title="Patient Details"
                        
                        elems = []
                       
                       
                        data =(['Full Name', a],
                        ['Gender', b],
                        ['Age', c],
                        ['Blood Group', d],
                        ['Report Date,Time',timeprint],
                        ['CNIC',f]
                        )
                        
                        def colr(x, y, z):
                            return (x/255, y/255, z/255)    
                        def add_image(img):
                            im = Image(img)
                            im.hAlign = 'LEFT'
                            elems.append(im)
                           
                     
                        choose_filename= filedialog.asksaveasfile(mode='a', defaultextension=".pdf")
                        fileName=choose_filename.name
                     
                        add_image("2.jpeg")
                       
                        headstyle = ParagraphStyle(
                            name='MyHeader',
                            fontName='Helvetica-Bold',
                            fontSize=16,
                            leading =10
                        )
                        doctorstyle = ParagraphStyle(
                            name='MyDoctorHeader',
                            fontName='Helvetica',
                            fontSize=13,
                            leading =10
                        )
                        styles = getSampleStyleSheet()
                        text ='''Comments: 
                        <br/><br/> 
                        
                        The test has been performed by USFDA approved and CE marked triple gene detection kit for novel corona virus on nasopharyngeal/oropharyngeal swabs.
                        <br/> <br/> 
                        
                        The negative result must be interpreted along with clinical observations, patient ’s
                        history and epidemiological information. A single result might not exclude possibility of corona virus infection;
                        repeat test might be requiredbetween 24-48 hours if symptoms persist. The patient should consider himself/herself as 
                        suspected case for corona virus and should remain under self quarantine and maintain social distancing."
                        <br/><br/>
                        
                        In case of positive result, it is strongly advised that the patient should stay at home under self quarantine and
                        maintain social distancing. Additional tests required for timely decision of treatment are Blood CP with absolute
                        lymphocyte count, Serum Ferritin, LDH, D. Dimer, CPK, Troponins, CRP and X. Ray chest PA view.

                        <br/><br/>
                        
                        A positive result after some time interval/ landing in other country against a negative initial result by IDC can be
                        due to post sample exposure to Covid-19 and IDC does not bear responsibility of this.

                        <br/><br/>

                        COVID -19 PCR Testing has globally accepted technology and technique related limitations of false negative
                        and positive results. We try to keep that to lowest permissible levels by using best three targets FDA approved
                        & CE marked kits. Moreover time of sample taken and viral load are unavoidable variables.
                        Ref.(https://www.medrxiv.org/content/10.1101/2020.04.26.20080911v2)
                        
                        '''
                        para = Paragraph(text, style=styles["Normal"])
                        
                                                
                        pdf = SimpleDocTemplate(fileName,pagesize=letter,title="Report",rightMargin=20,leftMargin=20,topMargin=30,bottomMargin=18,showBoundary=1)
                        table1 = Table(data,hAlign='RIGHT')
                       
                        table1.setStyle(TableStyle([
                            ('BACKGROUND', (0, 0), (4, 0), '#CFEAD4'),
                            ('BACKGROUND', (0, 2), (4, 2), '#CFEAD4'),
                            ('BACKGROUND', (0, 4), (4, 4), '#CFEAD4'),
                            ('BOX',(0,0),(-1,-1), 0.5, '#CFEAD4'),
                            ('GRID',(0,0),(-1,-1), 0.5, colr(12, 43, 8)),
                            ]))
                        data =(['Test', 'Result'],
                               ['Covid-19',Covid],
                               ['Pneumonia',Pneumonia])
                               
                          
                        table2 = Table(data,hAlign='LEFT',colWidths=[2.9*inch] * 5)
                       
                        table2.setStyle(TableStyle([
                            ('VALIGN',(0,0),(-1,-1), 'TOP'),
                            ('TEXTCOLOR',(0,0),(-1,0),colors.white),
                            ('BACKGROUND', (0, 0), (-1, 0), colr(40, 196, 15)),
                            ('GRID',(0,1),(-1,-1), 0.5, '#CFEAD4'),
                            ]))
                        
                      
                        elems.append(table1)
                        elems.append(Spacer(1, 20))
                        elems.append(table2)
                        elems.append(Spacer(1, 50))
                        elems.append(para)
                             
                        pdf.build(elems)
                        messagebox.showinfo("Help","Saved Successfully.")
                       
                      
                      btn5=Button (wrapper4, text="Save",command=print_report).grid(row=10,column=1,padx=10,pady=10)
                      btn6=Button (wrapper4, text="Close",command=close).grid(row=10,column=2,padx=10,pady=10)
                      top2.protocol('WM_DELETE_WINDOW', close)
                      
                
                else:
                    fname.set("")
                    age.set("")
            else:
                 messagebox.showerror("Error","Please insert correct Age")
                 
                 age.set("")
        else:
               messagebox.showerror("Error","Please insert correct Name")
               fname.set("")
    
    


 
def clearform():
    fname.set("")
    age.set("")
    bgname.set("Select")
    #bgsign.set("Select")
    gender_choice.set("")
    cnic.set("")

def check_if_file_exist():
    if Path('Patient.csv').is_file():
        return True
    else:
        with open('Patient.csv', 'a')as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Fullname','Gender', 'Age', 'Blood Name', 'CNIC'])
            csvfile.close()
        return True
    
    
def saveform():
       a_fname=fname.get()
       a_gender_choice=gender_choice.get()
       a_age=age.get()
       a_bgname=bgname.get()
       #a_bgsign=bgsign.get()
       a_cnic=cnic.get()
       
       
  
       
       if(a_fname=="" or a_age=="" or a_age=="0" or a_cnic=="" ):
           messagebox.showerror("Error","Please insert correct details")
           fname.set("")
           age.set("")
           cnic.set("")
       elif(a_gender_choice==""):
           messagebox.showerror("Error","Please insert correct gender")
           
           
       elif(a_bgname=="Select"): #(or a_bgsign=="Select"):
           messagebox.showerror("Error","Please select blood group")
          
           
       elif (a_fname!="" or a_age!="" or a_cnic!="" or a_age!="0" or a_gender_choice!="" or a_bgname!="Select"):#or a_bgsign!="Select"):
           pattern1 = '^[ a-zA-Z]*$'
           if re.search(pattern1, a_fname):
             pattern2='^[0-9]*$'
             if re.search(pattern2, a_age):
                 pattern3='^[0-9+]{5}-[0-9+]{7}-[1-9]{1}$'
                 if re.search(pattern3, a_cnic):
                     result=messagebox.askquestion("Submit","Are you sure you want to enter data?")
                     if(result=='yes'):
                         check_if_file_exist()
                         with open('Patient.csv','a')as csvfile:
                           writer=csv.writer(csvfile)
                           writer.writerow([a_fname,a_gender_choice,a_age,a_bgname,a_cnic])#,a_bgsign])
                           csvfile.close()
                           messagebox.showinfo("Help","Saved Successfully.")
                     else:
                         messagebox.showinfo("Error","Record not saved.")
                       
                 else:
                    messagebox.showerror("Error","Please insert CNIC")
                    cnic.set("")
             
             else:
                messagebox.showerror("Error","Please insert correct Age")
                age.set("")
           else:
            messagebox.showerror("Error","Please insert correct Name")
            fname.set("")
       else:
           print("")
                 
                
    
#wrapper1    
wrapper=LabelFrame(root,text="")
wrapper.pack(padx=10,pady=10,fill="both",expand="no")
#wrapper2
wrapper_fat = LabelFrame(root,text="")
wrapper_fat.pack(padx=10,pady=10,fill="both",expand="no")

wrapper2=LabelFrame(wrapper_fat,text="Test Covid & Pneumonia")
wrapper2.grid(row=0,column=0,padx=5,sticky=W)
#wrapper3 with scrollbar
wrapper3=LabelFrame(wrapper_fat,text="Chest X-Ray Image")
wrapper3.grid(row=0,column=1,padx=5,sticky=E)
wrapper_fat.rowconfigure(0,weight=1)



lblheading=Label(wrapper,text="Patient Details",font=('Arial',24,"bold")).grid(row=0,column=0,padx=10,pady=10)

lbl1=Label(wrapper, text="Full Name",font=('Arial',12))
lbl1.grid(row=1,column=0,padx=90,pady=10, sticky=tk.W)
ent1=Entry(wrapper,textvariable=fname).grid(row=1,column=1,padx=50,pady=10)

lbl2=Label(wrapper, text="Gender",font=('Arial',12)).grid(row=2,column=0,padx=90,pady=5, sticky=tk.W)
radiobtn1=Radiobutton(wrapper,text="Male",variable=gender_choice,value="Male").grid(row=2,column=1,padx=10,pady=5)
radiobtn2=Radiobutton(wrapper,text="Female",variable=gender_choice,value="Female").grid(row=2,column=2,padx=10,pady=5)
radiobtn3=Radiobutton(wrapper,text="Others",variable=gender_choice,value="Other").grid(row=2,column=3,padx=40,pady=5)



lbl3=Label(wrapper, text="Age",font=('Arial',12)).grid(row=3,column=0,padx=90,pady=5, sticky=tk.W)
ent3=Entry(wrapper,textvariable=age).grid(row=3,column=1,padx=10,pady=5)

lbl4=Label(wrapper, text="Blood Group",font=('Arial',12)).grid(row=4,column=0,padx=90,pady=5, sticky=tk.W)
list1=['Select','A+','A-','B+','B-','O+','O-',"AB+",'AB-']

droplist=OptionMenu(wrapper,bgname,*list1)
droplist.config(width=5)
bgname.set('Select')
droplist.grid(row=4,column=1,padx=10,pady=5)

lbl11=Label(wrapper, text="CNIC",font=('Arial',12)).grid(row=5,column=0,padx=90,pady=5, sticky=tk.W)
ent11=Entry(wrapper,textvariable=cnic).grid(row=5,column=1,padx=10,pady=5)


lbl12=Label(wrapper,text="e.g 12345-1234567-1",font=('Arial',10)).grid(row=5,column=2,padx=10,pady=5)



btn1=Button(wrapper,text="Save" ,command=saveform).grid(row=6,column=1,padx=10,pady=10)
btn4=Button(wrapper,text="Clear",command=clearform).grid(row=6,column=2,padx=10,pady=10)
t1=StringVar()
lab2=Label(wrapper3)
lab2.pack()

btn2=ttk.Button(wrapper2,text="Browse Image", command=showimage,style='Fun.TButton').grid(row=1,column=0,padx=10,pady=10)


root.mainloop()

