#Import Necessary modules
import sqlite3 as sql
from datetime import date
from tkinter import *
from tkinter import messagebox

# Create database connection and connect to table
try:
       con = sql.connect('Add_your_note.db')
       cur = con.cursor()
       cur.execute('''CREATE TABLE notes_table
                        (date DATETIME, notes_title text, notes text)''')
except:
       print("Connected to table of database")


# Insert a row of data
def add_notes():
       #Get input values
       today = date.today()
       #.strftime("%d-%m-%Y %H:%M:%S")
       notes_title = notes_title_entry.get()
       notes = notes_entry.get("1.0", "end-1c")
       #Raise a prompt for missing values
       if (len(notes_title)<=0) & (len(notes)<=1):
               messagebox.showerror(message = "ENTER REQUIRED DETAILS" )
       else:
       #Insert into the table
               cur.execute("INSERT INTO notes_table VALUES ('%s','%s','%s')" %(today, notes_title, notes))
               messagebox.showinfo(message="Note added")
       #Commit to preserve the changes
               con.commit()


#Display all the notes
def view_notes():
       #Obtain all the user input
       notes_title = notes_title_entry.get()
       #If no input is given, retrieve all notes
       if (len(notes_title)<=0):
               sql_statement = "SELECT * FROM notes_table"
              
       #Retrieve notes matching a title
       elif (len(date) <=0) & (len(notes_title)>0):
               sql_statement = "SELECT * FROM notes_table where notes_title ='%s'" %notes_title
       #Retrieve notes matching a date
       elif (len(date) >0) & (len(notes_title)<=0):
               sql_statement = "SELECT * FROM notes_table where date ='%s'"%date
       #Retrieve notes matching the date and title
       else:
               sql_statement = "SELECT * FROM notes_table where date ='%s' and notes_title ='%s'" %(date, notes_title)
              
       #Execute the query
       cur.execute(sql_statement)
       #Obtain all the contents of the query
       row = cur.fetchall()
       #Check if none was retrieved
       if len(row)<=0:
               messagebox.showerror(message="No note found")
       else:
               #Print the notes
               for i in row:
                       messagebox.showinfo(message="Date: "+i[0]+"\nTitle: "+i[1]+"\nNotes: "+i[2])


#Delete the notes
def delete_notes():
       #Obtain input values
       notes_title = notes_title_entry.get()
       #Ask if user wants to delete all notes
       choice = messagebox.askquestion(message="Do you want to delete all notes? \n\n Are sure?")
       #If yes is selected, delete all
       if choice == 'yes':
               sql_statement = "DELETE FROM notes_table" 
       else:
       #Delete notes matching a particular date and title
               if (len(notes_title)<=0): 
                       #Raise error for no inputs
                       messagebox.showerror(message = "ENTER REQUIRED DETAILS" )
                       return
               else:
                      sql_statement = "DELETE FROM notes_table where date ='%s' and notes_title ='%s'" %(date, notes_title)
       #Execute the query
       cur.execute(sql_statement)
       messagebox.showinfo(message="Note(s) Deleted complety")
       con.commit()


#Update the notes
def update_notes():
       #Obtain user input
       notes_title = notes_title_entry.get()
       notes = notes_entry.get("1.0", "end-1c")
       #Check if input is given by the user
       if (len(notes_title)<=0) & (len(notes)<=1):
               messagebox.showerror(message = "ENTER REQUIRED DETAILS" )
       #update the note
       else:
               sql_statement = "UPDATE notes_table SET notes = '%s' where date ='%s' and notes_title ='%s'" %(notes, today, notes_title)
              
       cur.execute(sql_statement)
       messagebox.showinfo(message="Note Updated")
       con.commit()


#Invoke call to class to view a window
window = Tk()
#Set dimensions of window and title
window.geometry("600x300")
window.title("Add Your Note")
title_label = Label(window, text="Please Add Your Note \n ").pack()

#Read inputs
#Date input
#date_label = Label(window, text="Date:").place(x=10,y=80)
#date_entry = Entry(window,  width=20)
#date_entry.place(x=50,y=80)

#Notes Title input
notes_title_label = Label(window, text="Notes title:").place(x=10,y=50)
notes_title_entry = Entry(window,  width=46)
notes_title_entry.place(x=10,y=70)

#Notes input
notes_label = Label(window, text="Notes: ").place(x=10,y=100)
notes_entry = Text(window, width=60,height=5)
notes_entry.place(x=10,y=120)
 
#Perform notes functions
button1 = Button(window,text='Add Notes', bg = 'gray',fg='black',command=add_notes).place(x=10,y=20)
button2 = Button(window,text='View Notes', bg = 'gray',fg='black',command=view_notes).place(x=110,y=20)
button3 = Button(window,text='Delete Notes', bg = 'gray',fg='black',command=delete_notes).place(x=210,y=20)
button4 = Button(window,text='Update Notes', bg = 'gray',fg='white',command=update_notes).place(x=320,y=20)
 
#close the app
window.mainloop()
con.close()