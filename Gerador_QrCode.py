import qrcode

# Dados que você deseja codificar no QR code
data = "https://m5seguranca.com.br/"

# Cria uma instância do QRCode
qr = qrcode.QRCode(
    version=1,  # controla o tamanho do QR Code (1 a 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # nível de correção de erros
    box_size=10,  # tamanho de cada caixa do QR Code
    border=4,  # espessura da borda (em caixas)
)

# Adiciona os dados ao QR Code
qr.add_data(data)
qr.make(fit=True)

# Gera a imagem do QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Salva a imagem em um arquivo
img.save("qrcode_exemplo.png")

print("QR Code gerado e salvo como 'qrcode_exemplo.png'")
