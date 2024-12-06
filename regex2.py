import re

def rename_file(filename, regex):
    """
    Renomeia um arquivo com base na expressão regular fornecida e formata a data no formato YYYY-MM-DD.
    
    :param filename: O nome do arquivo a ser renomeado.
    :param regex: A expressão regular a ser usada para extrair e transformar partes do nome do arquivo.
    :return: O nome do arquivo renomeado no formato YYYY-MM-DD ou uma mensagem de erro se o padrão não corresponder.
    """
    # Mapeamento para os meses em inglês e português
    month_map = {
        'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06',
        'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12',
        'Janeiro': '01', 'Fevereiro': '02', 'Março': '03', 'Abril': '04', 'Maio': '05', 'Junho': '06',
        'Julho': '07', 'Agosto': '08', 'Setembro': '09', 'Outubro': '10', 'Novembro': '11', 'Dezembro': '12'
    }
    
    
    
    # Tenta encontrar a correspondência usando a regex fornecida
    match = re.search(regex, filename)
    
    if match:
        groups = match.groups()
        # Verifica se a correspondência é uma data no formato YYYY-MM-DD
        if len(groups) == 1 and re.match(r'\d{4}-\d{2}-\d{2}', groups[0]):
            return groups[0]
        
        # Verifica se a correspondência é uma data no formato de mês e ano
        if len(groups) >= 2:
            indice_month  = None
            indice_year = None
            indice_day = None

            # Itera sobre os grupos e seus índices
            for index, group in enumerate(groups):
                try:
                    # Tenta converter o grupo para um inteiro
                    value = int(group)
                    
                    # Verifica se é um ano (4 dígitos e maior que 2000)
                    if len(group) == 4 and value > 2000:
                        indice_year = index
                    # Verifica se é um dia (1 ou 2 dígitos, entre 1 e 31)
                    elif len(group) <= 2 and 1 <= value <= 31:
                        indice_day = index
                except ValueError:
                    # Se a conversão falhar, o grupo é uma string
                    indice_month = index
                
            
            year = groups[indice_year]
            month_name = groups[indice_month]
            month_number = month_map.get(month_name) 
            day = groups[indice_day] if indice_day is not None else '01'
            
            if month_number:
                return f"{year}-{month_number}-{day.zfill(2)}"
            else:
                raise ValueError(f"Mês '{month_name}' não reconhecido")
    
    raise ValueError("Nome do arquivo não corresponde ao padrão esperado")

# Exemplos de uso
file_names = [
    # ("infracoes-2024-07-01_2024-08-054290e955-050f", r'infracoes-(\d{4}-\d{2}-\d{2})'),
    # ("movimentos-2024-08-31_2024-08-313f7d75a1-7130", r'movimentos-(\d{4}-\d{2}-\d{2})'),
    ("Planilha de Evidências S3 - Julho 2024", r'Planilha de Evidências S3 - (\w+) (\d{4})'),
    ("Planilha de Evidências S3 - Outubro 2024 15", r'Planilha de Evidências S3 - (\w+) (\d{4}) (\d{1,2})'),
    ("Planilha de Evidências S3 - 15 July 2024", r'Planilha de Evidências S3 - (\d{1,2}) (\w+) (\d{4})'),
    ("Arquivo aleatório sem data-2024-07-01", r'Arquivo aleatório sem data-(\d{4}-\d{2}-\d{2})')  # Exemplo que não corresponderá
]

for fname, rgx in file_names:
    try:
        new_name = rename_file(fname, rgx)
        print(f"Nome corrigido: {new_name}")
    except ValueError as e:
        print(f"Erro: {e}")
