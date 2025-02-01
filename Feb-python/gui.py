from tkinter import *
import customtkinter

#theme and color
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#app(window) itself
app = customtkinter.CTk()
app.geometry("600x400")
app.title("Titulo")
app.resizable(width=True, height=True)

#background frames
top_frame = customtkinter.CTkFrame(master=app, fg_color="light gray")
top_frame.pack(side="top", fill="both", expand=True)
bottom_frame = customtkinter.CTkFrame(master=app, fg_color="dark gray")
bottom_frame.pack(side="top", fill="both", expand=True)

#first layer frames
frame1 = customtkinter.CTkFrame(master=top_frame, fg_color="dark orange")
frame1.pack(side="left", fill="both", expand=True)
frame2 = customtkinter.CTkFrame(master=top_frame, fg_color="dark blue")
frame2.pack(side="left", fill="both", expand=True)
frame3 = customtkinter.CTkFrame(master=bottom_frame, fg_color="dark green")
frame3.pack(side="left", fill="both", expand=True)
frame4 = customtkinter.CTkFrame(master=bottom_frame,fg_color="dark red")
frame4.pack(side="left", fill="both", expand=True)

#buttons
button1 = customtkinter.CTkButton(master=frame1, text="Bucaros", fg_color="yellow", text_color="dark grey")
button1.place(relx=0.5, rely=0.5, anchor="center")
button2 = customtkinter.CTkButton(master=frame2, text="Millos", fg_color="blue", text_color="dark grey")
button2.place(relx=0.5, rely=0.5, anchor="center")
button3 = customtkinter.CTkButton(master=frame3, text="Verde", fg_color="green", text_color="dark grey")
button3.place(relx=0.5, rely=0.5, anchor="center")
button4 = customtkinter.CTkButton(master=frame4, text="Stfe", fg_color="red", text_color="dark grey")
button4.place(relx=0.5, rely=0.5, anchor="center")






app.mainloop()

