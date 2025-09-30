# Responsible for managing SAP login process and session
class SAPLoginService:
        def login(self, usuario, senha, mandante, idioma):
        # Lógica simples para começar
        if usuario and senha and mandante:
            return True, "Login efetuado!"
        return False, "Dados inválidos!"