import os
import xml.etree.ElementTree as ET

def buscar_palavra_em_tag_xml(palavra, tag, caminho_pasta):
    resultados = {}

    # Itera por todos os arquivos na pasta
    for arquivo in os.listdir(caminho_pasta):
        if arquivo.endswith('.xml'):  # Verifica se o arquivo é XML
            caminho_arquivo = os.path.join(caminho_pasta, arquivo)
            try:
                # Carrega e parseia o arquivo XML
                tree = ET.parse(caminho_arquivo)
                root = tree.getroot()

                # Busca a palavra dentro das tags específicas
                matches = []
                for elem in root.iter(tag):
                    if palavra.lower() in (elem.text or '').lower():
                        matches.append(elem.tag)

                if matches:
                    resultados[arquivo] = matches

            except ET.ParseError:
                print(f"Erro ao processar o arquivo {arquivo}. Verifique se ele é um XML válido.")

    return resultados


# Exemplo de uso
if __name__ == "__main__":
    palavra_para_buscar = input("Digite a palavra que deseja buscar: ")
    tag_especifica = input("Digite a tag XML onde deseja buscar: ")
    pasta_xmls = input("Digite o caminho para a pasta com os arquivos XML: ")

    resultados_busca = buscar_palavra_em_tag_xml(palavra_para_buscar, tag_especifica, pasta_xmls)

    if resultados_busca:
        print("\nResultados encontrados:")
        for arquivo, elementos in resultados_busca.items():
            print(f"- Arquivo: {arquivo}")
            print(f"  Tag onde '{palavra_para_buscar}' foi encontrada: {', '.join(elementos)}")
    else:
        print("Nenhuma ocorrência encontrada.")
