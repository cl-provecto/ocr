import pytesseract
import cv2
import csv

imagem = cv2.imread("s16 (1).jpg")

# Define as coordenadas da ROI
x1, y1 = 274, 824  # Canto superior esquerdo
x2, y2 = 1160, 1100  # Canto inferior direito
# Calcula as coordenadas e dimensões da ROI
x = x1
y = y1
w = x2 - x1
h = y2 - y1
# Seleciona a região de interesse (ROI) na imagem original
roi = imagem[y:y+h, x:x+w]

caminho = r"C:\Program Files\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

texto = pytesseract.image_to_string(roi)
print(texto)

#print(pytesseract.image_to_boxes(imagem, lang="por"))
# cv2.imshow("Imagem", imagem)
# cv2.waitKey(0)

# Nome do arquivo original
nome_arquivo = "s16 (1).jpg"

# Abre o arquivo CSV para escrita (modo 'a' para adicionar no final)
with open('resultado.csv', mode='a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    
    # Escreve uma linha com nome do arquivo e texto reconhecido
    writer.writerow([nome_arquivo, texto])

print("Dados exportados para resultado.csv")