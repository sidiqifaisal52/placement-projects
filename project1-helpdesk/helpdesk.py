import tkinter as tk

window = tk.Tk()

window.title("IT Helpdesk Ticket System")

window.geometry("700x500")

window.configure(bg="#F4F6F9")

title = tk.Label(
    window,
    text="IT Helpdesk Ticket System",
    font=("Segoe UI", 22, "bold"),
    bg="#C6D5F7",
    fg="#336AB1"
)

title.pack(pady=40)

window.mainloop()