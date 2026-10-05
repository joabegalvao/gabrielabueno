#!/usr/bin/env python3
"""Gera as imagens otimizadas da landing page a partir dos arquivos originais.

Uso (na raiz do projeto):
    python3 tools/optimize-images.py

Requer Pillow (pip install pillow) e a pasta materiais-de-origem/. Os
originais nunca são alterados. Para trocar uma foto, substitua o arquivo de
origem ou edite a lista PHOTOS e rode o script novamente.

A imagem de compartilhamento (1200x630) é montada pelo Chromium, com as
fontes do site, por outro script:
    node tools/render-compartilhamento.js
"""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "materiais-de-origem"
SRC = SOURCES / "fotos"
LOGO_SRC = SOURCES / "logo" / "Logo.png"
OUT = ROOT / "assets" / "img"

GOLD = (160, 113, 39)   # #a07127, medido no logo
IVORY = (247, 243, 237)  # #f7f3ed, fundo da página

# Nada é ampliado: a maior versão gerada é a do original.
WIDTHS = (480, 800, 1200)

# nome de saída -> (arquivo em materiais-de-origem/fotos, área usada ou None)
# A área é (esquerda, topo, direita, base) em pixels do original. As capturas
# do Instagram trazem a seta do carrossel na borda direita e os pontos de
# paginação embaixo: ficam de fora.
PHOTOS = {
    # retratos (capturas do Instagram)
    "loiro-ondulado": ("Screenshot 2026-10-05 142946.png", (3, 3, 668, 868)),
    "loiro-longo": ("Screenshot 2026-10-05 143002.png", (3, 3, 666, 828)),
    "loiro-mel": ("Screenshot 2026-10-05 143022.png", (3, 3, 668, 870)),
    "morena-iluminada": ("Screenshot 2026-10-05 143038.png", (3, 3, 666, 868)),
    "loiro-curto": ("Screenshot 2026-10-05 143228.png", (3, 3, 559, 747)),
    # fotos do salão e de trabalhos (arquivos maiores)
    "salao": ("imagem-01.png", None),
    "produtos": ("imagem-02.png", None),
    "costas-mel": ("imagem-03.png", None),
    "costas-castanho": ("imagem-04.png", None),
}
# imagem-05.png (o monograma em relevo sobre a parede) é uma imagem gerada,
# não uma foto do salão; não é usada na página.


def resize_to_width(im: Image.Image, width: int) -> Image.Image:
    if im.width <= width:
        return im.copy()
    height = round(im.height * width / im.width)
    return im.resize((width, height), Image.LANCZOS)


def save_set(im: Image.Image, name: str) -> None:
    for width in WIDTHS:
        if width < im.width:
            resize_to_width(im, width).save(OUT / f"{name}-{width}.webp", "WEBP", quality=80, method=6)
    im.save(OUT / f"{name}-{im.width}.webp", "WEBP", quality=80, method=6)
    # fallback JPEG para navegadores sem WebP
    im.save(OUT / f"{name}-{im.width}.jpg", "JPEG", quality=82, optimize=True, progressive=True)
    print(f"{name}: {im.width}x{im.height}")


def build_photos() -> None:
    for name, (source, area) in PHOTOS.items():
        im = Image.open(SRC / source).convert("RGB")
        save_set(im.crop(area) if area else im, name)


def build_logo() -> None:
    """O logo veio em PNG sobre branco (1254x1254). Separa o monograma do
    fundo pela luminosidade, pinta com o dourado medido e salva com
    transparência; assim ele serve sobre o marfim e sobre o marrom."""
    src = Image.open(LOGO_SRC).convert("L")
    box = src.point(lambda v: 255 if v < 235 else 0).getbbox()
    margin = 12
    src = src.crop((box[0] - margin, box[1] - margin, box[2] + margin, box[3] + margin))
    # branco (255) vira transparente; o dourado (~120) vira opaco
    alpha = src.point(lambda v: max(0, min(255, round((255 - v) * 255 / 135))))
    for name, color in (("monograma", GOLD), ("monograma-claro", (236, 214, 176))):
        for size in (640, 320, 160):
            a = alpha.resize((size, round(alpha.height * size / alpha.width)), Image.LANCZOS)
            out = Image.new("RGBA", a.size, color + (0,))
            out.putalpha(a)
            out.save(OUT / f"{name}-{size}.png", optimize=True)
            out.save(OUT / f"{name}-{size}.webp", "WEBP", quality=90, method=6)
    print(f"monograma: {alpha.width}x{alpha.height} (salvo em 640, 320 e 160)")

    # ícones: o monograma dourado sobre o marfim
    for name, size in (("favicon-32", 32), ("apple-touch-icon", 180), ("icon-192", 192)):
        tile = Image.new("RGBA", (512, 512), IVORY + (255,))
        a = alpha.resize((400, round(alpha.height * 400 / alpha.width)), Image.LANCZOS)
        mark = Image.new("RGBA", a.size, GOLD + (0,))
        mark.putalpha(a)
        tile.alpha_composite(mark, ((512 - mark.width) // 2, (512 - mark.height) // 2))
        tile.convert("RGB").resize((size, size), Image.LANCZOS).save(OUT / f"{name}.png", optimize=True)


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    build_photos()
    build_logo()
    total = sum(f.stat().st_size for f in OUT.iterdir())
    print(f"{len(list(OUT.iterdir()))} arquivos, {total / 1024:.0f} KB no total")
