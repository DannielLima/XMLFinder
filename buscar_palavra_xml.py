import os
import xml.etree.ElementTree as ET

def buscar_palavra_no_xml(caminho_arquivo, palavra):
    """
    Busca uma palavra em qualquer parte de um arquivo XML (tags ou conteúdo).
    Retorna True se a palavra for encontrada.
    """
    try:
        tree = ET.parse(caminho_arquivo)
        root = tree.getroot()
        palavra_lower = palavra.lower()

        # Verifica em todas as tags e textos
        for elemento in root.iter():
            if palavra_lower in (elemento.tag.lower() or '') or palavra_lower in (elemento.text or '').lower():
                return True
    except Exception as e:
        print(f"Erro ao processar {caminho_arquivo}: {e}")
    return False


def analisar_pasta(pasta, palavra):
    """
    Analisa todos os arquivos XML em uma pasta e busca pela palavra.
    Retorna uma lista com os arquivos que contêm a palavra.
    """
    arquivos_encontrados = []

    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        if os.path.isfile(caminho_arquivo) and arquivo.endswith('.xml'):
            if buscar_palavra_no_xml(caminho_arquivo, palavra):
                arquivos_encontrados.append(arquivo)

    return arquivos_encontrados


# Configurações
pasta_xmls = "C:/Users/Danniel O Brabo/Desktop/GUIMARAES XML/ERRADOS"  # Pasta onde estão os arquivos XML
palavra_buscar = input("Digite a palavra para buscar nos arquivos XML: ")

# Processar
arquivos_com_palavra = analisar_pasta(pasta_xmls, palavra_buscar)

# Resultado
if arquivos_com_palavra:
    print("\nArquivos que contêm a palavra:")
    for arquivo in arquivos_com_palavra:
        print(f"- {arquivo}")
else:
    print("\nNenhum arquivo contém a palavra buscada.")
