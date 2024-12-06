import re

def rename_file(filename, regex):
    """
    Renomeia um arquivo com base na expressão regular fornecida.
    
    :param filename: O nome do arquivo a ser renomeado.
    :param regex: A expressão regular a ser usada para extrair e transformar partes do nome do arquivo.
    :return: O nome do arquivo renomeado ou uma mensagem de erro se o padrão não corresponder.
    """
    # Mapeamento para os meses
    month_map = {
        'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06',
        'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12',
        'Janeiro': '01', 'Fevereiro': '02', 'Março': '03', 'Abril': '04', 'Maio': '05', 'Junho': '06',
        'Julho': '07', 'Agosto': '08', 'Setembro': '09', 'Outubro': '10', 'Novembro': '11', 'Dezembro': '12'
    }
    
    # Tenta encontrar a correspondência usando a regex fornecida
    match = re.search(regex, filename)
    
    if match:
        # Se a regex capturou um grupo
        print('encontrou')
        
        groups = match.groups()
        print(groups)
        
        # Se a regex é para capturar a hora (e.g., '10:20')
        if re.match(r'\d{2}:\d{2}', filename):
            return filename  # Retorna o nome original para o caso de hora

        # Se a regex é para capturar a data (e.g., 'Planilha de Evidências S3 - Julho 2024')
        if len(groups) >= 2:
            month_name, year = groups[:2]
            day = groups[2] if len(groups) > 2 else '01'
            month_number = month_map.get(month_name)
            
            if month_number:
                # Formata a data como YYYY-MM-DD
                return f"{year}-{month_number}-{day.zfill(2)}"
            else:
                raise ValueError(f"Mês '{month_name}' não reconhecido")
    
    raise ValueError("Nome do arquivo não corresponde ao padrão esperado")

# Exemplos de uso
file_names = [
    ("infracoes-2024-07-01_2024-08-054290e955-050f", r'infracoes- (\d{4}-\d{2}-\d{2})'),
    ("movimentos-2024-08-31_2024-08-313f7d75a1-7130", r'movimentos- (\d{4}-\d{2}-\d{2})'),
    ("Planilha de Evidências S3 - Julho 2024", r'Planilha de Evidências S3 - (\w+) (\d{4})'),
    ("Planilha de Evidências S3 - Outubro 2024 15", r'Planilha de Evidências S3 - (\w+) (\d{4}) (\d{1,2})'),
    ("Arquivo aleatório sem data", r'(\d{2}:\d{2})')  # Exemplo que não corresponderá
]

for fname, rgx in file_names:
    try:
        new_name = rename_file(fname, rgx)
        print(f"Nome corrigido: {new_name}")
    except ValueError as e:
        print(f"Erro: {e}")
