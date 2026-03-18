import tkinter as tk

class CalculatorButton(tk.Button):
    def __init__(self, master, text, command, bg="#e1e1e1", fg="#000000", hover_bg="#d0d0d0", **kwargs):
        super().__init__(
            master, 
            text=text, 
            command=command, 
            bg=bg, 
            fg=fg, 
            relief="flat",
            activebackground=hover_bg,
            **kwargs
        )
        self.default_bg = bg
        self.hover_bg = hover_bg
        
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self.config(bg=self.hover_bg)

    def on_leave(self, event):
        self.config(bg=self.default_bg)

class DisplayLabel(tk.Label):
    def __init__(self, master, bg="#f0f0f0", fg="#000000", font=("Arial", 24), **kwargs):
        super().__init__(
            master, 
            bg=bg, 
            fg=fg, 
            font=font, 
            anchor="e", 
            padx=10, 
            **kwargs
        )
