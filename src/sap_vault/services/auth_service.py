# Resposible for authorization and authentication of the application, keeps track of session state and password/token management
class AuthService:

    def __init__(self):
        self.__master_password: str | None = None
        self._is_authenticated: bool = False

    def login(self, password: str) -> bool:
        # Simples verificação de senha mestre
        if password == "senha_mestre":  # Substitua por uma verificação real
            self.__master_password = password
            self._is_authenticated = True
            return True
        return False
