import qrcode
from PIL import Image

# Função para gerar o QR code com logomarca no centro
def generate_qr_with_logo(data, logo_path, output_path):
    # Criar o objeto QR code com o nível de correção de erro alto
    qr = qrcode.QRCode(
        version=1,  # Controla o tamanho do QR code (quanto maior o número, mais detalhes)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Nível de correção de erro alto (até 30%)
        box_size=5,  # Tamanho de cada quadrado do QR code
        border=1,  # Tamanho da borda branca ao redor do QR code
    )

    # Adiciona os dados ao QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Gera a imagem do QR code
    qr_img = qr.make_image(fill='black', back_color='white').convert('RGB')

    # Abrir a logomarca
    logo = Image.open(logo_path)

    # Calcular o tamanho ideal da logomarca (10% do tamanho do QR code)
    qr_size = qr_img.size[0]  # QR code é um quadrado, então só precisamos da largura
    logo_size = int(qr_size * 0.4)  # Reduzindo o logo para 10% do tamanho do QR code
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

    # Calcular a posição onde o logo será inserido (centro do QR code)
    logo_position = (
        (qr_img.size[0] - logo_size) // 2,
        (qr_img.size[1] - logo_size) // 2
    )

    # Colar a logomarca no centro do QR code
    qr_img.paste(logo, logo_position, logo)

    # Salvar a imagem final com o QR code e o logo
    qr_img.save(output_path)

# Exemplo de uso
data = "https://m5seguranca.com.br/"
logo_path = "Z:\Rafael\ARTES\M5 SEGURANÇA\LOGO\M5png.png"  # Substitua pelo caminho correto do arquivo PNG
output_path = "qr_code_com_logo.png"

generate_qr_with_logo(data, logo_path, output_path)
