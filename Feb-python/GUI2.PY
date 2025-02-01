import customtkinter as ctk

# Set appearance mode
ctk.set_appearance_mode("light")

# Create the main window
app = ctk.CTk()
app.geometry("500x400")

# Entry widget
entry = ctk.CTkEntry(master=app, placeholder_text="Alias", width=300)
entry.place(relx=0.5, rely=0.2, anchor="center")

# Button widget
button = ctk.CTkButton(master=app, text="Click Me", corner_radius=32)
button.place(relx=0.5, rely=0.5, anchor="center")

# Combobox widget
scroll_list = ctk.CTkComboBox(master=app, values=["guaro", "perico", "popper", "tussi", "sexo"])
scroll_list.place(relx=0.5, rely=0.7, anchor="center")

# Checkbox widget
check_box = ctk.CTkCheckBox(master=app, text="premium")
check_box.place(relx=0.5, rely=0.9, anchor="center")

# Run the application
app.mainloop()