import tkinter as tk

MESSAGE = """##############################
#
# Testing Terminal
#
##############################     
"""

def run_command(event=None):
    command = entry_command.get()

    if command == "":
        return
    
    output_command(f"$ {command}")
    match command:
        case "hello":
            output_command(f"Hello World!")
        case "cls":
            clean_console()
        case _:
            clean_console()
            output_command(f"Command not recognized: {command}")
    
    entry_command.delete(0, tk.END)

def clean_console():
    text_console.config(state=tk.NORMAL)
    text_console.delete(1.0, tk.END)
    text_console.config(state=tk.DISABLED)
    output_command(MESSAGE)

def output_command(texto):
    text_console.config(state=tk.NORMAL)
    text_console.insert(tk.END, texto + "\n")
    text_console.config(state=tk.DISABLED)
    text_console.yview(tk.END)

def on_focus_in(event):
    entry_command.config(bg="black")

def on_focus_out(event):
    entry_command.config(bg="black")

def set_focus(event):
    entry_command.focus_set()

def adjust_size_entry():
    texto = entry_command.get()
    width = max(len(texto) + 4, 10)
    entry_command.config(width=width)

window = tk.Tk()
window.title("Terminal")

window.configure(bg="black")

window.resizable(False, False)

window_height = 500
window_width = 900

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

frame_initial = tk.Frame(window, bg="black")
frame_initial.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

text_console = tk.Text(frame_initial, height=20, width=80, bg="black", fg="lightgreen", font=("Monospace", 12), insertbackground="white", bd=0, padx=10, pady=10)
text_console.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
text_console.config(state=tk.DISABLED)

label_prompt = tk.Label(frame_initial, text="$", fg="lightgreen", bg="black", font=("Monospace", 12))
label_prompt.pack(side=tk.LEFT, padx=(0, 1), anchor="nw", pady=(0, 5))

entry_command = tk.Entry(frame_initial, fg="lightgreen", font=("Monospace", 12), insertbackground="white", bd=0)
entry_command.pack(padx=(0, 10), pady=(0, 5), fill=tk.X)

line_inferior = tk.Canvas(frame_initial, height=1, bg="lightgreen", bd=0, highlightthickness=0)
line_inferior.pack(padx=(0, 10), pady=(0, 5), fill=tk.X)

entry_command.bind("<Return>", run_command)

output_command(MESSAGE)

entry_command.bind("<FocusIn>", on_focus_in)
entry_command.bind("<FocusOut>", on_focus_out)

window.bind("<Button-1>", set_focus)

entry_command.focus_set()

window.after(100, adjust_size_entry)

window.mainloop()
