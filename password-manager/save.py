from tkinter import messagebox
from tkinter import *
import json


class SavePassword:

    def __init__(self):
        self.email = None
        self.password = None
        self.website = None

    def find_password(self, website_entry):
        self.website = website_entry.get().title()
        try:
            with open('data.json') as data_file:
                data = json.load(data_file)
                found_entry = data[self.website]
        except KeyError:
            messagebox.showerror(title='Error', message=f'No details for the {self.website} exists')
        except FileNotFoundError:
            messagebox.showerror(title='Error', message='No Data File Found. Kindly add details.')
        else:
            messagebox.showinfo(title=self.website, message=f"Email: {found_entry['email']}\n"
                                                            f"Password: {found_entry['password']}")
        finally:
            website_entry.delete(0, END)

    def save_password(self, website_entry, email_entry, password_entry):
        self.website = website_entry.get().title()
        self.email = email_entry.get()
        self.password = password_entry.get()
        new_data = {
            self.website: {
                'email': self.email,
                'password': self.password,
            }
        }

        if len(self.website) == 0 or len(self.password) == 0:
            messagebox.showwarning(title='WARNING', message='Kindly fill in the required fields')
        else:
            is_ok = messagebox.askokcancel(title=self.website,
                                           message=f'Website: {self.website.title()}\nEmail: {self.email}\n'
                                                   f'Password: {self.password}\n'
                                                   'Click ok to save')
            if is_ok:
                # with open('data.txt', mode='a') as f:
                #     f.write(f'{self.website} | {self.email} | {self.password}\n')
                try:
                    with open('data.json', 'r') as data_file:
                        # Read Old Data from existing file #
                        data = json.load(data_file)
                except FileNotFoundError:
                    # Create file if it does not exist by handling exception #
                    with open('data.json', 'w') as data_file:
                        # Write new data to the json file #
                        json.dump(new_data, data_file, indent=4)
                else:
                    # Update with new data added to the dictionary #
                    data.update(new_data)
                    with open('data.json', 'w') as data_file:
                        # Write appended data to the json file #
                        json.dump(data, data_file, indent=4)
                finally:
                    # Reset the text fields #
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
