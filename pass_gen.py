from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import string
import random
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Password Generator")
        self.root.geometry("650x500+370+140")

        self.main_frame = Frame(self.root, bd=5, relief=RIDGE)
        self.main_frame.place(x=0, y=0, width=650, height=500)

        title_lbl = Label(self.main_frame, text="PASSWORD GENERATOR SOFTWARE", font=("times new roman", 20, "bold"), fg="red", bg="white")
        title_lbl.place(x=0, y=0, width=650)

        home_lbl = Label(self.main_frame, text="STAY HOME STAY SAFE", font=("times new roman", 20, "bold"), fg="red", bg="white")
        home_lbl.pack(side=BOTTOM, fill=X)

        img1 = Image.open(r"C:\Users\hp\VS\Python\RANDOM PASS GEN\icon_pass.png")
        img1 = img1.resize((650, 90), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg = Label(self.main_frame, image=self.photoimage1)
        lblimg.place(x=0, y=40, width=650)

        lengthlbl = Label(self.main_frame, text="Enter Password Length", font=("times new roman", 20, "bold"), fg="blue")
        lengthlbl.place(x=40, y=150)

        self.var_entry = StringVar()
        entry_fill = ttk.Entry(self.main_frame, textvariable=self.var_entry, width=55, font=("times new roman", 15, "bold"))
        entry_fill.place(x=40, y=185)

        strength_lbl = Label(self.main_frame, text="Select Password Strength", font=("times new roman", 20, "bold"), fg="blue")
        strength_lbl.place(x=40, y=225)

        self.strength_var = StringVar(value="Strong")
        ttk.Radiobutton(self.main_frame, text="Weak", variable=self.strength_var, value="Weak", style="TRadiobutton").place(x=40, y=265)
        ttk.Radiobutton(self.main_frame, text="Moderate", variable=self.strength_var, value="Moderate", style="TRadiobutton").place(x=150, y=265)
        ttk.Radiobutton(self.main_frame, text="Strong", variable=self.strength_var, value="Strong", style="TRadiobutton").place(x=300, y=265)

        btn = Button(self.main_frame, text="GENERATE PASSWORD", font=("times new roman", 15, "bold"), fg="white", bg="red", bd=4, relief=SUNKEN, cursor="hand2", command=self.pass_generator)
        btn.place(x=40, y=310, width=555, height=35)

        self.pass_b1 = Label(self.main_frame, text="Generated Password will appear here", font=("times new roman", 15, "bold"), fg="blue")
        self.pass_b1.place(x=40, y=360)

        copy_btn = Button(self.main_frame, text="COPY TO CLIPBOARD", font=("times new roman", 15, "bold"), fg="white", bg="green", bd=4, relief=SUNKEN, cursor="hand2", command=self.copy_to_clipboard)
        copy_btn.place(x=40, y=400, width=555, height=35)

        self.generated_password = StringVar()

    def pass_generator(self):
        if self.var_entry.get() == "":
            messagebox.showerror("Error", "Please enter a length for the password")
        else:
            num = int(self.var_entry.get())
            s1 = string.ascii_lowercase
            s2 = string.ascii_uppercase
            s3 = string.digits
            s4 = string.punctuation

            s = []

            strength = self.strength_var.get()

            if strength == "Weak":
                s.extend(list(s1))
            elif strength == "Moderate":
                s.extend(list(s1 + s2))
            else:  # Strong
                s.extend(list(s1 + s2 + s3 + s4))

            random.shuffle(s)
            password = ''.join(random.choice(s) for i in range(num))

            self.generated_password.set(password)
            self.pass_b1.config(text=password)

    def copy_to_clipboard(self):
        pyperclip.copy(self.generated_password.get())
        messagebox.showinfo("Copied", "Password copied to clipboard successfully!")

if __name__ == "__main__":
    root = Tk()
    app = PasswordGenerator(root)
    root.mainloop()
