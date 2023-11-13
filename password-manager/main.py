from tkinter import *
from password import GenPassword
from save import SavePassword

save_pass = SavePassword()
gen_pass = GenPassword()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=48)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "sample@test.com")
password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=lambda: gen_pass.generate_password(password_entry))
generate_password_button.grid(row=3, column=2)
search_button = Button(text="Search", width=11, command=lambda: save_pass.find_password(website_entry))
search_button.grid(row=1, column=2, columnspan=2)
add_button = Button(text="Add", width=41,
                    command=lambda: save_pass.save_password(website_entry, email_entry, password_entry))
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
