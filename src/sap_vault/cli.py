from sap_vault.services.auth_service import AuthService
from sap_vault.ui.desktop_ui import *

# Entry point of the application, the web UI is the "final" interface, while not available, loads the simpler desktop UI
def main():

    try:
        # tenta carregar a interface web
        from sap_vault.ui.web_ui import WebApp
        print("Carregando interface web...")
        app = WebApp()
        app.run()
    except (ImportError, ModuleNotFoundError) as e:
        # fallback para interface desktop
        print("Interface web não encontrada, carregando interface desktop...")
        from sap_vault.ui.desktop_ui import App
        app = App()
        app.mainloop()

if __name__ == "__main__":
    main()
