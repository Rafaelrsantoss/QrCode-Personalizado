Você pode gerar um QR code personalizado com uma logomarca no centro usando a biblioteca qrcode e Pillow (PIL) em Python. O código abaixo cria um QR code, sobrepõe uma imagem de logomarca no centro e salva o resultado em um arquivo de imagem.

Aqui está o exemplo de código para criar um QR code com uma logomarca no centro:

Passos:
Instalar as bibliotecas necessárias:

qrcode: para gerar o QR code.
Pillow: para manipular imagens.
Execute o seguinte comando no terminal para instalar as bibliotecas: pip install qrcode[pil] Pillow

Explicação:
QRCode: Gera o código QR com os dados fornecidos.

Logo: O logo em formato PNG é redimensionado para ser cerca de 20% do tamanho total do QR code e sobreposto no centro.

Error Correction: O nível de correção de erro é ajustado para ERROR_CORRECT_H (até 30%) para que o QR code continue legível, mesmo com a inserção do logo no centro.

Detalhes Importantes:
Ajuste do tamanho do logo: Para evitar que o QR code perca legibilidade, o tamanho do logo é ajustado para cerca de 20% do QR code.
Posicionamento central: A logomarca é centralizada dentro da imagem do QR code.
Esse código gera um QR code com uma logomarca personalizada e salva como uma imagem .png. Você pode usar qualquer imagem no formato PNG como logomarca, ajustando o caminho da imagem para o arquivo correto.
