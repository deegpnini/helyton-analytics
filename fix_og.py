import urllib.request
from PIL import Image
import io
import os

# O ID do arquivo no Drive
file_id = '19BBMiQ8hY1DInEfKAQAYSffJgC5P253e'
url = f'https://drive.google.com/uc?export=download&id={file_id}'

print("1. Baixando imagem do Drive...")
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        data = response.read()
    
    print(f"   Baixado: {len(data)} bytes")
    
    print("2. Abrindo e otimizando a imagem...")
    img = Image.open(io.BytesIO(data))
    img = img.convert('RGB')
    
    # Cria fundo do tamanho exato do Open Graph
    bg = Image.new('RGB', (1200, 630), (10, 10, 15))
    
    # Redimensiona a imagem mantendo a proporção
    img.thumbnail((1200, 630))
    
    # Centraliza
    x = (1200 - img.width) // 2
    y = (630 - img.height) // 2
    bg.paste(img, (x, y))
    
    print("3. Salvando og-image.png...")
    bg.save('og-image.png', format='PNG', optimize=True)
    
    # Mostra o tamanho final
    tamanho_final = os.path.getsize('og-image.png')
    print(f"✅ Sucesso! Tamanho final: {tamanho_final} bytes")
    
except Exception as e:
    print(f"❌ Erro: {e}")
