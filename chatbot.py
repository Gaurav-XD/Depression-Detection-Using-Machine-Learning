import tkinter as tk
from tkinter import*
from tkinter import ttk
import PIL
from PIL import Image
from PIL import ImageTk


class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        

        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()


        img_chat=Image.open('ChatBot.jpg')
        img_chat=img_chat.resize((200,70),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='CHAT ME',font=('arial',30,'bold'),fg='gray',bg='white')
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=5,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()

        label_1=Label(btn_frame,text='Type Something',font=('arial',10,'bold'),fg='green',bg='white')
        label_1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=ttk.Entry(btn_frame,width=40,font=('times new roman',10,'bold'))
        self.entry.grid(row=0,column=1,padx=5,sticky=W)


        self.send=Button(btn_frame,text="Send>>",command=self.send,font=('arial',16,'bold'),width=8,bg='gray')
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clr=Button(btn_frame,text='Clear Data',command=self.clear,font=('arial',16,'bold'),width=8,bg='gray')
        self.clr.grid(row=0,column=3,padx=5,sticky=W)

        self.msg=''
        self.label_11=Label(btn_frame,text=self.msg,font=('arial',10,'bold'),fg='green',bg='white')
        self.label_11.grid(row=1,column=1,padx=5,sticky=W)
    
        #---------------

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')


    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)

        if (self.entry.get()==''):
            self.msg='Please enter some input'
            self.label_11.config(text=self.msg,fg='red')
        else:
            self.msg=''
            self.label_11.config(text=self.msg,fg='red')

        if (self.entry.get()=="Hi"):
            self.text.insert(END,"\n\n"+"Bot: Hi, How are you feeling today?\n1. Not Good \n2. Lonely \n3. Broken \n4. Suicidal Thoughts ") 
        
    
        elif (self.entry.get()=="Not Good"):
            self.text.insert(END,"\n\n"+"Bot: How can I help you to change Your Mood?")

        elif (self.entry.get()=="I dont want to talk"):
            self.text.insert(END,"\n\n"+"Bot: Okay, You can call your friends and plan something Interesting. ") 

        elif (self.entry.get()=="ok"):
            self.text.insert(END,"\n\n"+"Bot: Alright, Have a great day ahead !") 
    
        elif (self.entry.get()=="Lonely"):
            self.text.insert(END,"\n\n"+"Bot: Do you want me to do something for you?")

        elif (self.entry.get()=="No"):
            self.text.insert(END,"\n\n"+"Bot: Okay,You can ask your friends for Hang Out.") 

        elif (self.entry.get()=="Broken"):
            self.text.insert(END,"\n\n"+"Bot: If You want you can share your feeling with me, May be I can help you.") 
        
        elif (self.entry.get()=="I dont want to share"):
            self.text.insert(END,"\n\n"+"Bot: Okay, I can provide you a number may be they can help you.") 

        elif (self.entry.get()=="Suicidal Thoughts"):
            self.text.insert(END,"\n\n"+"Bot: This is bad, You can talk to your parents.") 
        
     
    
         
    

        else:
            self.text.insert(END,"\n\n"+"Bot: I cant Understand")         




if __name__ == '__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()      

