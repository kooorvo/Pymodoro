import customtkinter as ctk 


# App
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # option de base

        self.title("Pymodoro")
        self.geometry("425x525")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # on défini la frame etc

        self.mainFrame = ctk.CTkFrame(self)
        self.mainFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        # On place les premiers éléments sur la frame

        self.bigTitle = ctk.CTkLabel(self.mainFrame, text="Pymodoro", font=ctk.CTkFont(size=22, weight="bold"))
        self.bigTitle.pack(pady=30)

            # à remplacer par un vrai minuteur
        self.timer = ctk.CTkLabel(self.mainFrame, text="25m", font=ctk.CTkFont(size=35, weight="bold"))
        self.timer.place(relx=0.5, rely=0.5, anchor="center") # place le texte au centre absolu de la fenêtre

        self.timeOptions = ctk.CTkOptionMenu(self.mainFrame, width=80, height=50, )

app = App()
app.mainloop()