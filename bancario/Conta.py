class Conta:
    def __init__(self, documento: str = None, conta: str = None, agencia: str = None, digito: int = None) -> None:
        """
        Inicializa uma instância da classe Conta.

        Parameters:
            documento (str): O número do documento associado à conta.
            conta (str): O número da conta.
            agencia (str): O número da agência.
            digito (int): O dígito verificador da conta.
        """
        self._documento = documento
        self._conta = conta
        self._agencia = agencia
        self._digito = digito

    @property
    def documento(self) -> str:
        """
        Getter para o número do documento associado à conta.
        """
        return self._documento

    @documento.setter
    def documento(self, value: str) -> None:
        """
        Setter para o número do documento associado à conta.

        Parameters:
            value (str): O novo número do documento.
        """
        self._documento = value

    @property
    def conta(self) -> str:
        """
        Getter para o número da conta.
        """
        return self._conta

    @conta.setter
    def conta(self, value: str) -> None:
        """
        Setter para o número da conta.

        Parameters:
            value (str): O novo número da conta.
        """
        self._conta = value

    @property
    def agencia(self) -> str:
        """
        Getter para o número da agência.
        """
        return self._agencia

    @agencia.setter
    def agencia(self, value: str) -> None:
        """
        Setter para o número da agência.

        Parameters:
            value (str): O novo número da agência.
        """
        self._agencia = value

    @property
    def digito(self) -> int:
        """
        Getter para o dígito verificador da conta.
        """
        return self._digito

    @digito.setter
    def digito(self, value: int) -> None:
        """
        Setter para o dígito verificador da conta.

        Parameters:
            value (int): O novo dígito verificador.
        """
        self._digito = value
