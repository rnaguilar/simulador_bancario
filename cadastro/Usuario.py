from simulador_bancario.bancario.Conta import Conta

class Usuario:

    def __init__(self) -> None:
        """
        Inicializa um objeto da classe Usuario.
        """
        self._documento = None
        self._nome = None
        self._email = None
        self._senha = None
        self._contas: list[Conta] = []

    @property
    def documento(self) -> str:
        """
        Obtém o documento do usuário.

        Returns:
            str: O documento do usuário.
        """
        return self._documento

    @documento.setter
    def documento(self, novo_documento: str) -> None:
        """
        Define o documento do usuário.

        Args:
            novo_documento (str): O novo documento do usuário.
        """
        self._documento = novo_documento

    @property
    def nome(self) -> str:
        """
        Obtém o nome do usuário.

        Returns:
            str: O nome do usuário.
        """
        return self._nome

    @nome.setter
    def nome(self, novo_nome: str) -> None:
        """
        Define o nome do usuário.

        Args:
            novo_nome (str): O novo nome do usuário.
        """
        self._nome = novo_nome

    @property
    def email(self) -> str:
        """
        Obtém o e-mail do usuário.

        Returns:
            str: O e-mail do usuário.
        """
        return self._email

    @email.setter
    def email(self, novo_email: str) -> None:
        """
        Define o e-mail do usuário.

        Args:
            novo_email (str): O novo e-mail do usuário.
        """
        self._email = novo_email

    @property
    def senha(self) -> str:
        """
        Obtém a senha do usuário.

        Returns:
            str: A senha do usuário.
        """
        return self._senha

    @senha.setter
    def senha(self, nova_senha: str) -> None:
        """
        Define a senha do usuário.

        Args:
            nova_senha (str): A nova senha do usuário.
        """
        self._senha = nova_senha

    @property
    def contas(self) -> list[Conta]:
        """
        Obtém a lista de contas associadas ao usuário.

        Returns:
            list[Conta]: A lista de contas do usuário.
        """
        return self._contas

    def atrelar_conta(self, conta: Conta) -> None:
        """
        Adiciona uma conta à lista de contas do usuário.

        Args:
            conta (Conta): A conta a ser associada ao usuário.
        """
        self._contas.append(conta)
