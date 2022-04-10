import tkinter as tk

class Calculator():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.configure(bg="#2F4F4F")
        self.root.geometry("223x260")
        self.root.minsize(223, 260)
        self.root.maxsize(223, 260)
        
        self.math_expression = ""
        
        self.create_widgets()
        
        
        self.root.mainloop()
        
    def create_widgets(self):
        
        self.btn0 = tk.Button(self.root, text= "0", padx=20, command=self.appendExpression)
        self.btn1 = tk.Button(self.root, text= "1", padx=20, command=self.appendExpression)
        self.btn2 = tk.Button(self.root, text= "2", padx=20, command=self.appendExpression)
        self.btn3 = tk.Button(self.root, text= "3", padx=20, command=self.appendExpression)
        self.btn4 = tk.Button(self.root, text= "4", padx=20, command=self.appendExpression)
        self.btn5 = tk.Button(self.root, text= "5", padx=20, command=self.appendExpression)
        self.btn6 = tk.Button(self.root, text= "6", padx=20, command=self.appendExpression)
        self.btn7 = tk.Button(self.root, text= "7", padx=20, command=self.appendExpression)
        self.btn8 = tk.Button(self.root, text= "8", padx=20, command=self.appendExpression)
        self.btn9 = tk.Button(self.root, text= "9", padx=20, command=self.appendExpression)
        self.btndecimal = tk.Button(self.root, text= ".", padx=20, command=self.appendExpression)
        self.btnequals = tk.Button(self.root, text= "=", padx=20, command=self.appendExpression)
        self.btnplus = tk.Button(self.root, text= "+", padx=20, command=self.appendExpression)
        self.btnminus = tk.Button(self.root, text= "-", padx=20, command=self.appendExpression)
        self.btnmultiply = tk.Button(self.root, text= "*", padx=20, command=self.appendExpression)
        self.btndivide = tk.Button(self.root, text= "/", padx=20, command=self.appendExpression)
        self.btnclear = tk.Button(self.root, text= "C", padx=20, command=self.clr_screen)
        self.btnexit = tk.Button(self.root, text= "Exit", background="#AE1111", padx=20, command=self.exit_pogram)

        self.btn0.grid(row=5, column=0, pady=5)
        self.btn1.grid(row=4, column=0, pady=5)
        self.btn2.grid(row=4, column=1, pady=5)
        self.btn3.grid(row=4, column=2, pady=5)
        self.btn4.grid(row=3, column=0, pady=5)
        self.btn5.grid(row=3, column=1, pady=5)
        self.btn6.grid(row=3, column=2, pady=5)
        self.btn7.grid(row=2, column=0, pady=5)
        self.btn8.grid(row=2, column=1, pady=5)
        self.btn9.grid(row=2, column=2, pady=5)
        self.btndecimal.grid(row=5, column=1, pady=5)
        self.btnequals.grid(row=5, column=2, pady=5,   columnspan= 2, sticky='nsew')
        self.btnplus.grid(row=4, column=3, pady=5)
        self.btnminus.grid(row=3, column=3, pady=5)
        self.btnmultiply.grid(row=2, column=3, pady=5)
        self.btndivide.grid(row=1, column=3, pady=5)
        self.btnclear.grid(row=1, column=2, pady=5)
        self.btnexit.grid(row=1, column=0, pady=5,  columnspan= 2, sticky='nsew')
        
        self.displayLabel = tk.Label(self.root, text="0", font=('Ariel',20) , pady=20, anchor="e" ,bg="white")
        self.displayLabel.grid(row=0, column=0, columnspan=4, sticky='nsew')
        
        
    def appendExpression(self):
        pass
    
    def clr_screen(self):
        self.displayLabel["text"] = "0"

    def exit_pogram(self):
        self.root.destroy()
        self.root.quit()
    
Calculator()