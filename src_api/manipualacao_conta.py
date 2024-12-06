from simulador_bancario.controle_banco.BD_Class

def verificar_saldo(conta, digito)->float:
    query = """
    SELECT 
        saldo 
    FROM saldo_conta
    where
        conta = {conta}
        digito = {digito}
    """
    
    
    