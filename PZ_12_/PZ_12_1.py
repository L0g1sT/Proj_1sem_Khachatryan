from tkinter import *

root = Tk()
root.title("PZ_12_1")
root.geometry("600x800")

label1 = Label(root, text="Contact Form", font='arial 20')
label1.place(x=12, y=0)

label2 = Label(root, text="Name", font='arial 10')
label2.place(x=10, y=60)

text1 = Text(root, height=1, width=75, font='arial 10', wrap=WORD)
text1.place(x=11, y=83)

label3 = Label(root, text="Email", font='arial 10')
label3.place(x=10, y=120)

text2 = Text(root, height=1, width=75, font='arial 10', wrap=WORD)
text2.place(x=11, y=143)

label4 = Label(root, text="Phone Number", font='arial 10')
label4.place(x=10, y=180)

text3 = Text(root, height=1, width=75, font='arial 10', wrap=WORD)
text3.place(x=11, y=203)

label5 = Label(root, text="Subject", font='arial 10')
label5.place(x=10, y=240)

text4 = Text(root, height=1, width=75, font='arial 10', wrap=WORD)
text4.place(x=11, y=263)

label6 = Label(root, text="Leave us a few words", font='arial 10')
label6.place(x=10, y=300)

text5 = Text(root, height=3, width=75, font='arial 10', wrap=WORD)
text5.place(x=11, y=323)

label7 = Label(root, text="File Attachements", font='arial 10')
label7.place(x=10, y=400)

button1 = Button(root, height=1, width=12, text='Choose Files', bg='light gray', font='arial 10')
button1.place(x=20, y=423)

text6 = Text(root, height=1, width=20, font='arial 10')
text6.place(x=140, y=426)

button2 = Button(root, height=2, width=8, text='Submit', bg='blue', font='arial 10', fg='white')
button2.place(x=20, y=500)

root.mainloop()
