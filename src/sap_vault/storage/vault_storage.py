# Responsible for dealing with the encrypted file storage and decrypted data
class VaultStorage:
    def __init__(self):
        self.systems = []

    def load_vault(self, master_password):
        #Carrega o arquivo do cofre, descriptografando-o (exceto a senha)
        pass

    def get_password(self, system_uuid: str, connection_name: str) -> str:
        #Retorna a senha de uma conexão específica, descriptografando apenas no momento necessário
        pass