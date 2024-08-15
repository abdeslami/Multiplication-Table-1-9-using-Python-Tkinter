from tkinter import *
from tkinter import ttk
def action(event):
    s=listCombo.get()
    N=int(s[-1])
    result['text']="table de multiplication de "+str(N)
    for i in range(0,11):
        result['text']=result['text']+'\n'+str(i) + " x  "+str(N)+" = "+str(N*i)
root=Tk()
root.title("Table de Mutliplication")
root.geometry("500x255")
result=Label(root,text='Resultat ...............')
result.place(x=50,y=70)
listNumber=[
"table de multiplication de :0",
"table de multiplication de :1",
"table de multiplication de :2",
"table de multiplication de :3",
"table de multiplication de :4",
"table de multiplication de :5",
"table de multiplication de :6",
"table de multiplication de :7",
"table de multiplication de :8",
"table de multiplication de :9"]
listCombo=ttk.Combobox(root,values=listNumber,width=30)
listCombo.current(0)
listCombo.place(x=50,y=10)
listCombo.bind("<<ComboboxSelected>>",action)
root.mainloop()