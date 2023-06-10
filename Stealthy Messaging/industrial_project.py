##importing mmodules

from tkinter import *
import base64

#initialize window
root = Tk()
root.geometry('500x300')
root.resizable(1,1)
root.configure(bg="dark green")

#title of the window
root.title("DataFlair - Message Encode and Decode")



#label

Label(root, text =' PYTHON PROJECT FOR ENCODING DECODING MESSAGES', font = 'arial 20 bold',bg="light green").pack()

Label(root, text ='DataFlair', font = 'arial 20  bold', bg="light green").pack(side =BOTTOM)


#define variables

Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()


#######define function#####

#function to encode

def Encode(key,message):
    enc=[]
    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))
        
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

#function to decode

def Decode(key,message):
    dec=[]
    message = base64.urlsafe_b64decode(message).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i])- ord(key_c)) % 256))
        
    return "".join(dec)

#function to set mode
def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')



#Function to exit window
        
def Exit():
    root.destroy()


#Function to reset
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")


#################### Label and Button #############

#Message
Label(root, font= 'arial 18 bold', text='PLEASE ENTER THE MESSAGE YOU WANT TO ENCODE OR DECODE:',bg="light green").place(x= 60,y=180)
Entry(root, font = 'arial 19', textvariable = Text, bg = 'ghost white').place(x=890, y = 180)

#key
Label(root, font = 'arial 18 bold', text ='PLEASE ENTER THE KEY FOR ENCRYPTIION OR DECRYPTION :',bg="light green").place(x=60, y = 250)
Entry(root, font = 'arial 19', textvariable = private_key , bg ='ghost white').place(x=890, y = 250)


#mode
Label(root, font = 'arial 18 bold', text ='ENTER THE MODE(e-ENCODE, d-DECODE):', bg="light green").place(x=60, y = 320)
Entry(root, font = 'arial 19', textvariable = mode , bg= 'white').place(x=890, y = 320)





######result button
Button(root, font = 'arial 18 bold', text = '***********RESULT********** ' ,padx =2,bg ='light green' ,command = Mode).place(x=530, y = 390)

#result
Entry(root, font = 'arial 50 bold', textvariable = Result, bg ='ghost white').place(x=270, y = 500)



#reset button
Button(root, font = 'arial 20 bold' ,text ='RESET' ,width =6, command = Reset,bg = 'light green', padx=2).place(x=180, y = 590)

#exit button
Button(root, font = 'arial 20 bold',text= 'EXIT' , width = 6, command = Exit,bg = 'light green', padx=2, pady=2).place(x=980, y = 590)
root.mainloop()
