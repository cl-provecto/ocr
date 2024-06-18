OCR em Região Específica de Imagens usando Python
Este script Python automatiza o processo de aplicação de OCR (Optical Character Recognition) em uma região específica de imagens. Ele foi desenvolvido para processar múltiplos arquivos de imagem em uma pasta específica (C:\s16 neste exemplo), extrair texto de uma região delimitada e salvar os resultados em um arquivo CSV.

Requisitos
Python 3.x
Bibliotecas Python: opencv-python, pytesseract, csv
Certifique-se de ter o Tesseract OCR instalado e configurado corretamente no seu sistema.

Instalação das Dependências
Instale as dependências necessárias usando pip:

bash
Copiar código
pip install opencv-python pytesseract
Certifique-se de que o Tesseract OCR esteja instalado no seu sistema. Você pode baixá-lo e instalá-lo a partir do site oficial do Tesseract OCR.

Uso
Clone este repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
Navegue até o diretório do projeto:

bash
Copiar código
cd seu-repositorio
Configure o caminho para a pasta de imagens no arquivo ocr_process.py:

python
Copiar código
pasta_imagens = r"C:\s16"
Execute o script Python:

bash
Copiar código
python ocr_process.py
Isso irá processar todas as imagens na pasta C:\s16, extrair o texto de uma região específica (definida no código) de cada imagem usando OCR e salvar os resultados em um arquivo resultado.csv dentro da mesma pasta.

Personalização
Região de Interesse (ROI): Ajuste as coordenadas (x1, y1, x2, y2) na função extrair_texto_roi no arquivo ocr_process.py para definir a área específica da imagem que deseja extrair texto.

Formato de Saída: Modifique o script conforme necessário para atender às suas necessidades específicas de processamento de imagem e OCR.

Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request com melhorias.
