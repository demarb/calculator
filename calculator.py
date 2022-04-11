import tkinter as tk

class Calculator():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.configure(bg="#2F4F4F")
        self.root.geometry("223x242")
        self.root.minsize(223, 242)
        self.root.maxsize(223, 242)
        
        self.math_expression = ""
        self.grp_expression = ""
        
        self.create_widgets()
        
        self.root.mainloop()
        
    def create_widgets(self):
        
        self.btn0 = tk.Button(self.root, text= "0", padx=20, command=lambda: self.appendExpression("0"))
        self.btn1 = tk.Button(self.root, text= "1", padx=20, command=lambda: self.appendExpression("1"))
        self.btn2 = tk.Button(self.root, text= "2", padx=20, command=lambda: self.appendExpression("2"))
        self.btn3 = tk.Button(self.root, text= "3", padx=20, command=lambda: self.appendExpression("3"))
        self.btn4 = tk.Button(self.root, text= "4", padx=20, command=lambda: self.appendExpression("4"))
        self.btn5 = tk.Button(self.root, text= "5", padx=20, command=lambda: self.appendExpression("5"))
        self.btn6 = tk.Button(self.root, text= "6", padx=20, command=lambda: self.appendExpression("6"))
        self.btn7 = tk.Button(self.root, text= "7", padx=20, command=lambda: self.appendExpression("7"))
        self.btn8 = tk.Button(self.root, text= "8", padx=20, command=lambda: self.appendExpression("8"))
        self.btn9 = tk.Button(self.root, text= "9", padx=20, command=lambda: self.appendExpression("9"))
        self.btndecimal = tk.Button(self.root, text= ".", padx=20, command=lambda: self.appendExpression("."))
        self.btnequals = tk.Button(self.root, text= "=", padx=20, command=self.eval_expression)
        self.btnplus = tk.Button(self.root, text= "+", padx=20, command=lambda: self.appendExpression("+"))
        self.btnminus = tk.Button(self.root, text= "-", padx=20, command=lambda: self.appendExpression("-"))
        self.btnmultiply = tk.Button(self.root, text= "*", padx=20, command=lambda: self.appendExpression("*"))
        self.btndivide = tk.Button(self.root, text= "/", padx=20, command=lambda: self.appendExpression("/"))
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
        self.btndivide.grid(row=1, column=3, pady=0)
        self.btnclear.grid(row=1, column=2, pady=0)
        self.btnexit.grid(row=1, column=0, pady=0,  columnspan= 2, sticky='nsew')
        
        self.displayLabel = tk.Label(self.root, text="0", font=('Ariel',20) , pady=20, anchor="e" ,bg="white")
        self.displayLabel.grid(row=0, column=0, columnspan=4, sticky='nsew')
        
    def appendExpression(self, term):
        if ((term == "+") or (term == "-") or (term == "*") or  (term == "/")):
            self.math_expression += f" {term} "
            self.grp_expression= ""
            self.displayLabel["text"] = self.grp_expression
            
        else:
            self.math_expression += term
            self.grp_expression += term
            self.displayLabel["text"] = str(self.grp_expression)
            if (len(self.grp_expression) >14):          
                self.displayLabel["text"] = self.grp_expression[-14:] 
            
    def eval_expression(self):
        try:
            self.result = eval(self.math_expression)
            self.displayLabel["text"] = str(self.result)
            if (len(str(self.result)) >14):
                self.displayLabel["text"] = "{:e}".format(int(self.result))
        except(SyntaxError, NameError, TypeError, ZeroDivisionError):
            self.displayLabel["text"] = "Invalid Expression"
        finally:
            self.grp_expression= ""
            self.math_expression= ""
            
    def clr_screen(self):
        self.displayLabel["text"] = "0"
        self.grp_expression= ""
        self.math_expression= ""

    def exit_pogram(self):
        self.root.destroy()
        self.root.quit()
    
Calculator()