import tkinter as tk
import customtkinter as ctk
from PIL import Image
from CTkListbox import *
import os
from sap_vault.services.auth_service import AuthService
from sap_vault.services.connection_manager import ConnectionManager
from functools import partial

# Simple desktop UI using customtkinter
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        conn_manager = ConnectionManager()
        self.geometry("900x600")
        self.minsize(300, 200)
        self.title("SAP Vault")
        # self.iconbitmap("src/sap_vault/ui/assets/icon.ico"),
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.after(100, self.ask_master_password)

        self.title_frame = ctk.CTkFrame(self)
        self.title_frame.pack(side="top", fill="x")
        self.title_frame.columnconfigure(0, weight=1)
        self.title_frame.columnconfigure(1, weight=0)

        self.input_field = ctk.CTkEntry(self.title_frame, placeholder_text="Pesquisar sistema...") # Conforme vai digitando texto, vai filtrando a lista de sistemas
        self.input_field.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="ew")

        lock_icon_light = os.path.join(os.path.dirname(__file__), "icon_lightmode.ico")
        lock_icon_dark = os.path.join(os.path.dirname(__file__), "icon_darkmode.ico")

        if os.path.exists(lock_icon_light) and os.path.exists(lock_icon_dark):
            lock_image = ctk.CTkImage(  light_image=Image.open(lock_icon_light),
                                        dark_image=Image.open(lock_icon_dark),
                                        size=(20, 20))
        else:
            lock_image = None  # Fallback if image not found

        self.lock_button = ctk.CTkButton(self.title_frame, text="", image=lock_image, width=32, command=self.button_lock)
        self.lock_button.grid(row=0, column=1, padx=(5, 10), pady=10)

        self.title_frame.columnconfigure(0, weight=1)
        self.title_frame.columnconfigure(1, weight=0)

        panned = tk.PanedWindow(self, orient=tk.HORIZONTAL)
        panned.pack(fill=tk.BOTH, expand=True)

        self.system_list_frame = ctk.CTkFrame(panned)
        panned.add(self.system_list_frame, minsize=100)

        ctk.CTkButton(self.system_list_frame, text="Adicionar Sistema", command=self.button_new).pack(pady=10, padx=10, fill="x")

        listbox = CTkListbox(self.system_list_frame, command=self.show_value)
        listbox.pack(fill="both", expand=True)
        self.system_list_frame.grid_rowconfigure(0, weight=1)
        listbox.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        for idx, option in conn_manager.load_systems():
            listbox.insert(idx, option)

        self.main_frame = ctk.CTkFrame(panned)
        panned.add(self.main_frame, minsize=200)
        tabview = ctk.CTkTabview(self.main_frame)
        tabview.pack(fill="both", expand=True, padx=10, pady=10)

        tabview.add("DEV")
        tabview.add("QAS")
        tabview.add("PRD")
        tabview.add("+")
        tabview.set("DEV")

        tabdev = tabview.tab("DEV")

        # Configura o peso das colunas para controlar o redimensionamento
        tabdev.grid_columnconfigure(0, weight=0)  # Labels fixos
        tabdev.grid_columnconfigure(1, weight=1)  # Entradas principais (expandem)
        tabdev.grid_columnconfigure(2, weight=0)  # Label Idioma fixo
        tabdev.grid_columnconfigure(3, weight=0)  # Entrada Idioma fixa

        # Linha 0: Usuário
        usuario_label = ctk.CTkLabel(tabdev, text="Usuário:", width=80)
        usuario_label.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="e")  # 'e' alinha à direita
        usuario_entry = ctk.CTkEntry(tabdev, placeholder_text="Usuário SAP", width=200)
        usuario_entry.grid(row=0, column=1, columnspan=3, padx=(5, 10), pady=10, sticky="ew")

        # Linha 1: Senha
        senha_label = ctk.CTkLabel(tabdev, text="Senha:", width=80)
        senha_label.grid(row=1, column=0, padx=(10, 5), pady=10, sticky="e")
        senha_entry = ctk.CTkEntry(tabdev, placeholder_text="Senha SAP", show="*", width=200)
        senha_entry.grid(row=1, column=1, columnspan=3, padx=(5, 10), pady=10, sticky="ew")

        # Linha 2: Mandante
        mandante_label = ctk.CTkLabel(tabdev, text="Mandante:", width=80)
        mandante_label.grid(row=2, column=0, padx=(10, 5), pady=10, sticky="e")
        mandante_entry = ctk.CTkEntry(tabdev, placeholder_text="100", width=60, justify="center")
        mandante_entry.grid(row=2, column=1, padx=(5, 10), pady=10, sticky="ew")
        mandante_entry.insert(0, "100")

        # Espaço para idioma
        idioma_label = ctk.CTkLabel(tabdev, text="Idioma:", width=60)
        idioma_label.grid(row=2, column=2, padx=(10, 5), pady=10, sticky="e")
        idioma_entry = ctk.CTkEntry(tabdev, placeholder_text="PT", width=40)
        idioma_entry.grid(row=2, column=3, padx=(5, 10), pady=10, sticky="ew")
        idioma_entry.insert(0, "PT")
        # Linha 3: Botão Login
        login_button = ctk.CTkButton(tabdev, text="Login", command=self.button_login)
        login_button.grid(row=3, column=1, columnspan=2, padx=10, pady=(10, 10), sticky="ew")

# ========================
# POP-UP SENHA MESTRE
# ========================
class MasterPasswordPopUp(ctk.CTkToplevel):
    def __init__(self, master, on_submit):
        super().__init__(master)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        root = ctk.CTk()

        root.title("Senha Mestre")
        root.iconbitmap(os.path.join(os.path.dirname(__file__), "icon_darkmode.ico"))
        root.geometry("400x200")


    
    def input():
        dialog = ctk.CTkInputDialog(text="Digite a senha mestre:", title="Senha Mestre",
                                    fg_color="white",
                                    button_fg_color="green",
                                    button_hover_color="blue",
                                    button_text_color="white")
        
        master_password = dialog.get_input()
        if answer:


        #super().__init__(master)
        #self.title("Senha Mestre")
        #self.geometry("300x150")
        #self.resizable(False, False)
        #self.on_submit = on_submit

        #self.label = ctk.CTkLabel(self, text="Digite a senha mestre:")
        #self.label.pack(pady=(20, 5))

        #self.entry = ctk.CTkEntry(self, show="*")
        #self.entry.pack(pady=5, padx=20, fill="x")

        #self.button = ctk.CTkButton(self, text="Confirmar", command=self.submit)
        #self.button.pack(pady=15)

    #def submit(self):
        #senha = self.entry.get()
        #self.on_submit(senha)
        #self.destroy()

    # stubs temporários
    def button_lock(self):
        print("Sessão bloqueada pelo usuário.")

    def button_login(self):
        print("Login efetuado!")

    def button_new(self):
        print("Novo sistema adicionado!")

    def show_value(iself, ndex, selected_option):
        print(index, selected_option)
