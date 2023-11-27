from tkinter import *
base = Tk()
base.title("PRACTICAL-3")
base.geometry("500x500")

doc = ""
def avgtm():
    doc = txt1.get()

    doc_split = doc.split(" ")
    count = 0
    term = txt2.get()
    for i in doc_split:
        if (i == term):
            count += 1

    print("the ", term, " occured ", count, " this many times...")
    term_frequency = count / len(doc_split)
    term_frequency = round(term_frequency,3)
    lb3.config(text="Term Frequency : " + str(term_frequency))

def docTerm():
    # doc1 = txt3.get()
    # doc2 = txt4.get()
    # doc3 = txt5.get()
    doc1 = txt3.get().split(" ")
    doc2 = txt4.get().split(" ")
    doc3 = txt5.get().split(" ")
    count = 0
    term = txt6.get()

    if term in doc1:
        count+=1
    if term in doc2:
        count+=1
    if term in doc3:
        count+=1

    print("Count of Files in which ",term," occured is : ",count)

lb0 = Label(base, text="TERM FREQUENCY", fg="pink", font=("Arial Bold", 20))
lb0.place(x=120, y=5)

lb1 = Label(base, text="Enter Text : ")
lb1.place(x=50,y=50)
txt1 = Entry(base, width=30)
txt1.place(x=150,y=50)

lb2 = Label(base, text="Enter Word : ")
lb2.place(x=50,y=80)
txt2 = Entry(base, width=30)
txt2.place(x=150,y=80)

btn1 = Button(base, text="Term Frequency", bg="red", fg="white", font=("Arial Bold", 10), command=avgtm)
btn1.place(x=180,y=120)

lb3 = Label(base, text="")
lb3.place(x=50,y=160)

lb4 = Label(base, text="DOCUMENT FREQUENCY", fg="pink", font=("Arial Bold", 20))
lb4.place(x=90, y=190)

lb5 = Label(base, text="Enter Text1 : ")
lb5.place(x=50,y=240)
txt3 = Entry(base, width=30)
txt3.place(x=150,y=240)

lb6 = Label(base, text="Enter Text2 : ")
lb6.place(x=50,y=270)
txt4 = Entry(base, width=30)
txt4.place(x=150,y=270)

lb7 = Label(base, text="Enter Text3 : ")
lb7.place(x=50,y=300)
txt5 = Entry(base, width=30)
txt5.place(x=150,y=300)

lb8 = Label(base, text="Enter Word : ")
lb8.place(x=50,y=330)
txt6 = Entry(base, width=30)
txt6.place(x=150,y=330)

btn2 = Button(base, text="Document Frequency", bg="red", fg="white", font=("Arial Bold", 10), command=docTerm)
btn2.place(x=180,y=370)

base.mainloop()