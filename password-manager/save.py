from tkinter import messagebox
from tkinter import *


class SavePassword:

    def __init__(self):
        self.email = None
        self.password = None
        self.website = None

    def save_password(self, website_entry, email_entry, password_entry):
        self.website = website_entry.get()
        self.email = email_entry.get()
        self.password = password_entry.get()

        if len(self.website) == 0 or len(self.password) == 0:
            messagebox.showwarning(title='WARNING', message='Kindly fill in the required fields')
        else:
            is_ok = messagebox.askokcancel(title=self.website,
                                           message=f'Website: {self.website}\nEmail: {self.email}\n'
                                                   f'Password: {self.password}\n'
                                                   'Click ok to save')
            if is_ok:
                with open('data.txt', mode='a') as f:
                    f.write(f'{self.website} | {self.email} | {self.password}\n')
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
