import os
import pytesseract
import cv2
import csv

pasta = r"C:\temp\CR\siprov\19"

caminho = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

def texto_roi(imagem, x1, y1, x2, y2):
    
    # Calcula as coordenadas e dimensões da ROI
    x = x1
    y = y1
    w = x2 - x1
    h = y2 - y1
    # Seleciona a região de interesse (ROI) na imagem original
    roi = imagem[y:y+h, x:x+w]
    # Converte a região selecionada para texto usando OCR
    texto = pytesseract.image_to_string(roi)

    return texto

# Abre o arquivo CSV para escrita
with open('19resultado.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['Arquivo', 'Texto'])

    # Itera sobre todos os arquivos na pasta de imagens
    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.endswith('.jpg') or nome_arquivo.endswith('.jpeg') or nome_arquivo.endswith('.png'):
            # Caminho completo do arquivo
            caminho_arquivo = os.path.join(pasta, nome_arquivo)
            
            # Carrega a imagem
            imagem = cv2.imread(caminho_arquivo)
            
            # Coordenadas da região de interesse (ajuste conforme necessário)
            x1, y1 = 274, 824  # Canto superior esquerdo
            x2, y2 = 1160, 1100  # Canto inferior direito
            
            # Extrai texto da região de interesse
            texto = texto_roi(imagem, x1, y1, x2, y2)
            
            # Escreve no arquivo CSV
            writer.writerow([nome_arquivo, texto])
            
print("Processo concluído. Resultados salvos em resultado.csv")