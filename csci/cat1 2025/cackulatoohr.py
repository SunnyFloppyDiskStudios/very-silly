"""
Cackulatoohr.py

"""

import tkinter as tk
import re

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BODMAS Calculator")
        self.expression = ""

        self.input_text = tk.StringVar()

        self.create_gui()

    def create_gui(self):
        input_frame = tk.Frame(self.root)
        input_frame.pack()

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=('arial', 18), bd=10, insertwidth=2, width=14, borderwidth=4, relief='ridge', justify='right')
        input_field.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('^', 4, 2), ('+', 4, 3),
            ('(', 5, 0), (')', 5, 1), ('C', 5, 2), ('=', 5, 3),
        ]

        for (text, row, col) in buttons:
            action = lambda x=text: self.on_button_click(x)
            tk.Button(self.root, text=text, padx=20, pady=20, font=('arial', 14), command=action).grid(row=row, column=col)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.input_text.set("")
        elif char == '=':
            try:
                result = self.evaluate_expression(self.expression)
                self.input_text.set(result)
                self.expression = str(result)
            except Exception as e:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

    def evaluate_expression(self, expr):
        expr = expr.replace('^', '**')
        return self.parse_expression(expr)

    def parse_expression(self, expr):
        try:
            # Evaluate the expression using Python's eval after safety checks
            tokens = re.findall(r'[\d\.]+|[\+\-\*\/\(\)]|\*\*', expr)

            # Rebuild the expression to avoid security issues (optional validation)
            cleaned_expr = ''.join(tokens)

            # Evaluate with BODMAS using eval
            return eval(cleaned_expr)
        except:
            raise ValueError("Invalid Expression")

# Run the calculator
if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
