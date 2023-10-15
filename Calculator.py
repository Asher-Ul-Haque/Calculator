'''                 CALCULATOR              '''
#===========================================

#The imports-
from tkinter import *
import tkinter.messagebox as tmsg
# - - - - - - - - - - - - - - - - - - - - -

#The colors and fonts-
bgColor='#202020'
buttonTextColor='#FFF0F0'
numButtonBgColor='#393939'
buttonBgColor='#303030'
entryColor='#FFFFFF'
equalColor='#FD5DA8'
entryFont=('SegoeUI', 30, 'bold')
buttonFont=('SegoeUI', 15)
#- - - - - - - - - - - - - - - - - - - - -

#The root
root=Tk()
root.geometry('320x305')
root.minsize(320, 330)
root.maxsize(320, 330)
root.title('Calculator V.1')
try:
    root.wm_iconbitmap("icon.ico")
except:
    pass
root.config(bg=bgColor)
# - - - - - - - - - - - - - - - - - - - - -

#The Variables-
output=DoubleVar()
output.set(0)
deciOn=False
decimalPlaces=0
num1=0
num2=0
operation='+'
# - - - - - - - - - - - - - - - - - - - - -

#The output box
#outputBox=Label(root, textvariable=output, font=entryFont, bg=bgColor, fg=entryColor, justify=RIGHT, padx=10, pady=40).pack(anchor='e')
outputBox=Entry(root, textvariable=output, font=entryFont, bg=bgColor, fg=entryColor, justify=RIGHT, borderwidth=0)
outputBox.pack(anchor='e', pady=40, padx=10)

# - - - - - - - - - - - - - - - - - - - - -

#The button commands-
def click(event):
    global deciOn
    global decimalPlaces
    print('A button was clicked')
    next=event.widget.cget("text")
    if deciOn==True:
        decimalPlaces += 1
        output.set(output.get()+float(next)*(10**-(decimalPlaces)))
    else:
        output.set((output.get() * 10) + float(next))
    outputBox.update()
#^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
def clickSignChange(event):
    print('A button was clicked')
    output.set(output.get() * -1)
    outputBox.update()
#^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
def clickDecimal(event):
    global deciOn
    print('A button was clicked')
    deciOn=True
#^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
def makeNumButton(num, position):
    numButton=Button(root, text=str(num), font=buttonFont, bg=numButtonBgColor, fg=entryColor, relief=FLAT, padx=25)
    numButton.bind("<Button-1>", click)
    numButton.place(x=position[0], y=position[1])
#^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

signButton=Button(root, text='+/-', font=buttonFont, bg=numButtonBgColor, fg=entryColor, relief=FLAT, padx=18)
signButton.bind("<Button-1>", clickSignChange)
signButton.place(x=6, y=282)

decimalButton=Button(root, text='.', font=buttonFont, bg=numButtonBgColor, fg=entryColor, relief=FLAT, padx=27)
decimalButton.bind("<Button-1>", clickDecimal)
decimalButton.place(x=164, y=282)

makeNumButton(7, (6, 150))
makeNumButton(8, (85, 150))
makeNumButton(9, (164, 150))
makeNumButton(4, (6, 194))
makeNumButton(5, (85, 194))
makeNumButton(6, (164, 194))
makeNumButton(1, (6, 238))
makeNumButton(2, (85, 238))
makeNumButton(3, (164, 238))
makeNumButton(0, (85, 282))
# - - - - - - - - - - - - - - - - - - - - - - - - - -

def clear(event):
    global deciOn
    global decimalPlaces
    print("A button was pressed")
    output.set(0)
    outputBox.update()
    deciOn=False
    decimalPlaces=0
#^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
CEButton=Button(root, text='CE', font=buttonFont, bg=buttonBgColor, fg=entryColor, relief=FLAT, padx=17)
CEButton.bind("<Button-1>", clear)
CEButton.place(x=6, y=106)
CButton=Button(root, text='C', font=buttonFont, bg=buttonBgColor, fg=entryColor, relief=FLAT, padx=24)
CButton.bind("<Button-1>", clear)
CButton.place(x=85, y=106)
# - - - - - - - - - - - - - - - - - - - - - - - - - - -

def backspace(event):
    global deciOn
    global decimalPlaces
    if deciOn==True and decimalPlaces>0:
        if decimalPlaces < 0:
            decimalPlaces = 0
        num=str(output.get())
        num=num[0:len(num)-1]
        output.set(float(num))
        print(decimalPlaces)
    else:
        output.set(output.get()//10)
        decimalPlaces-=1
        if decimalPlaces < 0:
            decimalPlaces = 0
    outputBox.update()
#^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
def fuckIt(event):
    print('Fuck it')
    global deciOn
    global decimalPlaces
    output.set(output.get() // 10)
    decimalPlaces -= 1
    if decimalPlaces < 0:
        decimalPlaces = 0
    outputBox.update()
#^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
backspaceButton=Button(root, text='<xl', font=buttonFont, bg=buttonBgColor, fg=entryColor, relief=FLAT, padx=18)
backspaceButton.bind("<Button-1>", backspace)
backspaceButton.bind("<Double-1>", fuckIt)
backspaceButton.place(x=165, y=106)
# - - - -- - - - - - - - - - - - - - - - - - - - - - -

#The operations
def noteOperation(event):
    global deciOn
    global num1
    global operation
    operation = event.widget.cget("text")
    print(operation)
    num1=output.get()
    output.set(0)
    deciOn=False
#^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
def findAnswer(event):
    global operation, ans
    global num1
    num2=output.get()
    if operation=='+':
        ans=num1+num2
    elif operation=='- ':
        ans=num1-num2
    elif operation=='x':
        ans=num1*num2
    elif operation=='/' and num2!=0:
        ans=num1/num2
    else:
        tmsg.showinfo('Invalid', 'Cannot divide by 0!')
    output.set(ans)
    outputBox.update()
#^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
divideButton=Button(root, text='/', font=buttonFont, bg=buttonBgColor, fg=entryColor, relief=FLAT, padx=25)
divideButton.bind("<Button-1>", noteOperation)
divideButton.place(x=245, y=106)
def placeOperatorButton(operation, position, padx):
    operatorButton = Button(root, text=operation, font=buttonFont, bg=buttonBgColor, fg=entryColor, relief=FLAT, padx=padx)
    operatorButton.bind("<Button-1>", noteOperation)
    operatorButton.place(x=position[0], y=position[1])
    #This is a sample line
#^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^

placeOperatorButton('x', (244, 150), 24)
placeOperatorButton('- ', (244, 194), 22)
placeOperatorButton('+', (244, 238), 22)

equalButton=Button(root, text='=', font=buttonFont, bg=equalColor, fg=bgColor, relief=FLAT, padx=22)
equalButton.bind("<Button-1>", findAnswer)
equalButton.place(x=244, y=282)
#- - - - - - - - - - - - - - - - - - - - - - - - - -
#Mainloop()
root.mainloop()