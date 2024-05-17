#Imports tkinter, defines the master, creates the alphabet and enables the tickbox to work as a variable using 'reverse'.
from tkinter import *

master = Tk()

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
reverse = IntVar()

#A function to turn a string into an array of the strings components.
def Convert(string): 
        list1 = [] 
        list1[:0] = string
        return list1

#A function that the button calls that converts the text based on the cipher.
def Cipher():
    #Takes the text box inputs and converts the input into an array.
    text = e1.get()
    gronsfieldKey = e2.get()
    text = Convert(text)

    #Checks if the reverse checkbox is ticked and then reverses the key.
    if reverse.get() == 1:
        gronsfieldKey = Convert(gronsfieldKey)

        for index in range(0,len(gronsfieldKey)):
            current = int(gronsfieldKey[index])
            gronsfieldKey[index] = current - 2 * current

    #Replaces the letters with the ciphered varients.
    for index in range(0,len(text)):
        #This finds the index value of the current letter getting replaced from the alphabet array.
        try:
                currentLetter = alphabet.index(text[index])
        except ValueError:
                continue
        
        #This finds the current number in the cipher key, to be used as a cipher.
        try:
                currentCipher = int(gronsfieldKey[index % len(gronsfieldKey)])
        except ValueError:
                currentCipher = alphabet.index(gronsfieldKey[index])
                print(currentCipher)

        #This ciphers the letter using the current cipher.
        text[index] = alphabet[currentLetter + currentCipher]
        
        
    print(text)

#This creates the lables, text boxes and checkbuttons.
Label(master,text="Text").grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)

Label(master,text="Cipher").grid(row=1)
e2 = Entry(master)
e2.grid(row=1, column=1)

Button(master, 
          text = 'Calculate', command = Cipher).grid(row=8,column=1, sticky=W, pady=4)

Checkbutton(master, text="Reverse?", variable = reverse).grid(row=3)

mainloop()
