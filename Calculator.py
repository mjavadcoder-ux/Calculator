


import tkinter as tk

window = tk.Tk()
window.geometry("330x450")
window.title("Calculator")
window.resizable(False , False)


def click( number ):
    dispaly.insert(tk.END, number)
    
def op_cilick(op):
    dispaly.insert(tk.END, op)

def equal():
    e = dispaly.get()
    try:
       result = eval(e)
       dispaly.delete(0,tk.END)
       dispaly.insert(tk.END,result)
    except SyntaxError:
        dispaly.delete(0 ,tk.END)
        dispaly.insert(tk.END ,'Error')
    except NameError:
        dispaly.delete(0 ,tk.END)
        dispaly.insert(tk.END ,'Error')
    except ZeroDivisionError:
        dispaly.delete(0 ,tk.END)
        dispaly.insert(tk.END ,'Error')

def clear_button():
    dispaly.delete(0 , tk.END)

dispaly = tk.Entry(window ,border=15 , font=('Dosis SemiBold',20) , justify='right')
button1 = tk.Button(window, text="1" ,font=('Dosis SemiBold',15) , command= lambda c = 1: click(c))
button2 = tk.Button(window, text="2" ,font=('Dosis SemiBold',15) ,command= lambda c = 2: click(c))
button3 = tk.Button(window, text="3" ,font=('Dosis SemiBold',15), command= lambda c = 3: click(c))
button4 = tk.Button(window, text="4" ,font=('Dosis SemiBold',15) ,command= lambda c = 4: click(c))
button5 = tk.Button(window, text="5" ,font=('Dosis SemiBold',15) ,command= lambda c = 5: click(c))
button6 = tk.Button(window, text="6", font=('Dosis SemiBold',15) ,command= lambda c = 6: click(c))
button7 = tk.Button(window, text="7", font=('Dosis SemiBold',15) ,command= lambda c = 7: click(c))
button8 = tk.Button(window, text="8" ,font=('Dosis SemiBold',15) ,command= lambda c = 8: click(c))
button9 = tk.Button(window, text="9" ,font=('Dosis SemiBold',15) ,command= lambda c = 9: click(c))
button0 = tk.Button(window, text="0" ,font=('Dosis SemiBold',15) ,command= lambda c = 0: click(c))
buttonSum = tk.Button(window, text="+" ,font=('Dosis SemiBold',15),command= lambda o = '+': op_cilick(o))
buttonsub = tk.Button(window, text="-" ,font=('Dosis SemiBold',15) ,command= lambda o = '-': op_cilick(o))
buttonMul = tk.Button(window, text="*" ,font=('Dosis SemiBold',15),command= lambda o = '*': op_cilick(o))
buttonDiv = tk.Button(window, text="/" ,font=('Dosis SemiBold',15),command= lambda o = '/': op_cilick(o))
buttonEqual = tk.Button(window, text="=", font=('Dosis SemiBold',15),command=equal)
buttonC = tk.Button(window, text="C" ,font=('Dosis SemiBold',15) , command=clear_button)

dispaly.grid(row=0 , column=0 , columnspan=4 , sticky="news")

button7.grid(row=1 , column=0 ,sticky="news" , padx=5 , pady=5)
button8.grid(row=1 , column=1 ,sticky="news" ,padx=5 , pady=5)
button9.grid(row=1 , column=2 ,sticky="news", padx=5 , pady=5)
buttonSum.grid(row=1 , column=3 ,sticky="news", padx=5 , pady=5)

button4.grid(row=2 , column=0 ,sticky="news", padx=5 , pady=5)
button5.grid(row=2 , column=1 ,sticky="news", padx=5 , pady=5)
button6.grid(row=2 , column=2 ,sticky="news", padx=5 , pady=5)
buttonsub.grid(row=2 , column=3 ,sticky="news", padx=5 , pady=5)

button1.grid(row=3 , column=0 ,sticky="news", padx=5 , pady=5)
button2.grid(row=3 , column=1 ,sticky="news", padx=5 , pady=5)
button3.grid(row=3 , column=2 ,sticky="news", padx=5 , pady=5)
buttonMul.grid(row=3 , column=3 ,sticky="news", padx=5 , pady=5)

buttonC.grid(row=4 , column=0 ,sticky="news" ,padx=5 , pady=5)
button0.grid(row=4 , column=1 ,sticky="news", padx=5 , pady=5)
buttonEqual.grid(row=4 , column=2 ,sticky="news", padx=5 , pady=5)
buttonDiv.grid(row=4 , column=3 ,sticky="news" ,padx=5 , pady=5)


for i in range(0 ,5):
    for j in range(0 ,4):
        window.rowconfigure(i , weight=1)
        window.rowconfigure(j, weight=1)




window.mainloop()