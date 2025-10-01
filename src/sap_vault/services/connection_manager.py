# Responsible for managing connections to SAP systems
class ConnectionManager:
    def __init__(self):
        self.systems = []  # Lista de objetos System
        self.vault_storage = None  # Deve ser uma instância de VaultStorage
        
    def load_systems(self):
        # Deve buscar a lista de sistemas e conexões salvas no arquivo seguro e retornar a lista de sistemas no formato (index, "System Name")
        # Simulação inicial
        return [(0, "ECC"), (1, "S/4HANA"), (2, "BW"), (3, "CRM"), 
                (4, "SRM"), (5, "SCM"), (6, "PI"), (7, "PO"), (8, "GRC"), 
                (9, "Fiori"), (10, "Solution Manager")]
    
    def load_systems_from_file(self, filepath):
        # Carrega uma lista inicial de sistemas com base no arquivo xml de configuração do sap logon
        pass

    def add_system(self, system_name):
        # Lógica para adicionar um sistema
        # Um sistema tem um nome (SolMan) e um ou mais conexões
        pass

    def remove_system(self, system_name):
        # Lógica para remover um sistema
        pass

    def add_connection(self, system_name, connection_details):
        # Lógica para adicionar uma conexão a um sistema
        # Uma conexão tem um nome (DEV), mandante (199), usuário (fabio), senha (***) e idioma (PT)
        pass

    def remove_connection(self, system_name, connection_details):

        pass


class Connection:
    def __init__(self, vault_storage):
        self.name  = vault_sorage.get_username()
        self.mandt = vault_sorage.mandante
        self.usuer = vault_sorage.usuario
        
        # Só deve buscar senha no momento de estabelecer a conexão com o sistema SAP
        if vault_sorage.hasPassword():
            self.password = True
        else:
            self.password = False
        
        self.language = vault_storage.language

class System:
    def __init__(self, system_name):
        self.name = system_name
        self.connections = []  # Lista de objetos Connection

    def add_connection(self, connection):
        self.connections.append(connection)

    def remove_connection(self, connection):
        self.connections.remove(connection)