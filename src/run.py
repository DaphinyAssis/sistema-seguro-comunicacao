from GUI.screen import GInterface
from for_tests import *

class Run:
    def __init__(self):
        self.gui = GInterface()
        pass
        """Começar a integração do back com o front CHECK 
            1 - Registro de usuario CHECK
            2 - Login de usuario CHECK
            3 - Carregamento de chats Em andamento CHECK
            4 - Carregamentos de mensagens dentro do chat Em andamento CHECK
            5 - two-factory com numero de celular CHECK
        """
        """
            PRIORIDADE
            implementar botão de novo chat quando clicar colocar email e mensagem e criar um novo chat CHECK
            implementar a lista de chats e quando clicar em um chat mostrar a lista de mensagens CHECK
        """
        """
            POLIMENTO:
            Melhorar design da pagina register
            Melhorar design do celular CHECK
            Melhorar design da pagina Login
            Melhorar design do Chat app
        """

if __name__ == "__main__":
    run = Run()