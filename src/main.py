import customtkinter as ctk

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Pymodoro")
        self.geometry("425x525")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.mainFrame = ctk.CTkFrame(self)
        self.mainFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        self.mainFrame.grid_columnconfigure(0, weight=1)
        self.mainFrame.grid_rowconfigure(0, weight=0)
        self.mainFrame.grid_rowconfigure(1, weight=1)
        self.mainFrame.grid_rowconfigure(2, weight=0)
        self.mainFrame.grid_rowconfigure(3, weight=0)

        # Titre
        self.bigTitle = ctk.CTkLabel(
            self.mainFrame,
            text="Pymodoro",
            font=ctk.CTkFont(size=22, weight="bold"),
        )
        self.bigTitle.grid(row=0, column=0, pady=20)

        # Timer
        self.timerTitle = ctk.CTkLabel(
            self.mainFrame, text="Temps de travail :"
        )
        self.timerTitle.grid(row=1, column=0, pady=(0, 80))

        self.timer = ctk.CTkLabel(
            self.mainFrame, text="25:00", font=ctk.CTkFont(size=35, weight="bold")
        )
        self.timer.grid(row=1, column=0)

        # OptionMenu
        self.timeOptions = ctk.CTkOptionMenu(
            self.mainFrame,
            width=100,
            height=35,
            values=["25/05", "50/10", "90/20"],
        )
        self.timeOptions.grid(row=2, column=0, pady=15)

        # --- Frame pour grouper les boutons Démarrer et Stopper côte à côte ---
        self.btnFrame = ctk.CTkFrame(self.mainFrame, fg_color="transparent")
        self.btnFrame.grid(row=3, column=0, pady=(10, 25))

        self.startBtn = ctk.CTkButton(
            self.btnFrame,
            text="Démarrer",
            command=self.startTimer,
            width=120,
            height=45,
        )
        self.startBtn.grid(row=0, column=0, padx=5)

        self.stopBtn = ctk.CTkButton(
            self.btnFrame,
            text="Stopper",
            command=self.stopTimer,
            width=120,
            height=45,
            fg_color="#C0392B",  # Rouge pour le bouton d'arrêt
            hover_color="#E74C3C",
        )
        self.stopBtn.grid(row=0, column=1, padx=5)

        # Variables de gestion du timer
        self.time = 0
        self.timeB = 0
        self.timerJob = (
            None  # Stockera la référence au after() pour pouvoir l'annuler
        )

    def setupDurations(self):
        option = self.timeOptions.get()
        if option == "25/05":
            work_min, break_min = 25, 5
        elif option == "50/10":
            work_min, break_min = 50, 10
        else:
            work_min, break_min = 90, 20

        self.time = work_min * 60
        self.timeB = break_min * 60

    def startTimer(self):
        # Si un timer tourne déjà, on le stoppe proprement avant de relancer
        if self.timerJob is not None:
            self.after_cancel(self.timerJob)
            self.timerJob = None

        self.setupDurations()
        self.timerTitle.configure(text="Temps de travail :")
        self.updateTimer()

    def stopTimer(self):
        # Annule l'appel automatique en attente si le timer est actif
        if self.timerJob is not None:
            self.after_cancel(self.timerJob)
            self.timerJob = None

        # Réinitialise l'affichage
        self.timerTitle.configure(text="Prêt")
        self.timer.configure(text="25:00")

    def updateTimer(self):
        if self.time > 0:
            self.time -= 1
            minutes = self.time // 60
            secondes = self.time % 60
            self.timer.configure(text=f"{minutes:02d}:{secondes:02d}")

            # On enregistre l'identifiant de la boucle after
            self.timerJob = self.after(1000, self.updateTimer)
        else:
            self.timer.configure(text="00:00")
            self.timeBreak()

    def timeBreak(self):
        self.timerTitle.configure(text="Temps de pause :")
        if self.timeB > 0:
            self.timeB -= 1
            minutesB = self.timeB // 60
            secondesB = self.timeB % 60
            self.timer.configure(text=f"{minutesB:02d}:{secondesB:02d}")

            # On enregistre également l'identifiant pendant la pause
            self.timerJob = self.after(1000, self.timeBreak)
        else:
            self.timer.configure(text="00:00")
            self.timerTitle.configure(text="Session terminée !")
            self.timerJob = None


app = App()
app.mainloop()