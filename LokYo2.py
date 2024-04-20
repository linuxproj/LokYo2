import tkinter as tk
from tkinter import messagebox

class LokYo2Interpreter:
    def __init__(self):
        self.variables = {}
    
    def run(self, code):
        lines = code.splitlines()
        for line in lines:
            line = line.strip()
            if line.startswith("loki"):
                command = line[len("loki"):].strip()
                self.execute_command(command)
            else:
                messagebox.showerror("Error", f"Invalid command - {line}")
                return
    
    def execute_command(self, command):
        parts = command.split()
        if not parts:
            return
        
        if parts[0] == "Declare":
            self.handle_declaration(parts[1:])
        elif parts[0] == "Set":
            self.handle_assignment(parts[1:])
        elif parts[0] == "Print":
            self.handle_print(parts[1:])
        else:
            messagebox.showerror("Error", f"Unknown command - {command}")
    
    def handle_declaration(self, declaration_tokens):
        if len(declaration_tokens) != 2:
            messagebox.showerror("Error", "Invalid declaration")
            return
        
        var_name, var_type = declaration_tokens
        self.variables[var_name] = None  # Initialize variable
    
    def handle_assignment(self, assignment_tokens):
        if len(assignment_tokens) < 3 or assignment_tokens[1] != "to":
            messagebox.showerror("Error", "Invalid assignment")
            return
        
        var_name = assignment_tokens[0]
        value_tokens = assignment_tokens[2:]
        value = " ".join(value_tokens)  # Reconstruct the value
        
        # Check if the value is a string literal (enclosed in double quotes)
        if value.startswith('"') and value.endswith('"'):
            # Strip the quotes and assign the string value
            self.variables[var_name] = value[1:-1]
        else:
            # Assume it's a numeric value (integer)
            try:
                self.variables[var_name] = int(value)
            except ValueError:
                messagebox.showerror("Error", "Invalid value")
    
    def handle_print(self, print_tokens):
        if not print_tokens:
            messagebox.showerror("Error", "Invalid print statement")
            return
        
        output_parts = []
        for token in print_tokens:
            if token in self.variables:
                output_parts.append(str(self.variables[token]))
            else:
                output_parts.append(token)
        
        output_message = " ".join(output_parts)
        messagebox.showinfo("Print Result", output_message)

def run_lokyo2_interpreter():
    code = code_entry.get("1.0", tk.END)
    interpreter = LokYo2Interpreter()
    interpreter.run(code)

# Create a Tkinter GUI
root = tk.Tk()
root.title("LokYo2 Interpreter")

# Code input area
code_label = tk.Label(root, text="Enter LokYo2 code below:")
code_label.pack()

code_entry = tk.Text(root, height=10, width=50)
code_entry.pack()

# Run button
run_button = tk.Button(root, text="Run LokYo2 Code", command=run_lokyo2_interpreter)
run_button.pack()

root.mainloop()
