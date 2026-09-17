"""Les cinq couvertures en ligne, montées en bande pour le post LinkedIn.

Bâti sur les couvertures elles-mêmes (`energy-alternatives/assets/reels/acier_N.jpg`,
1080×1920, engendrées par `Reels/outils_couverture.py`) et non sur une capture d'écran
de la chaîne : l'ordre va de 1 à 5 au lieu du plus récent d'abord, rien du back-office
n'y figure, et la figure se refait à l'identique.

    python3 build_figure.py
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

COUVS = Path.home() / "Documents/Communication/energy-alternatives/assets/reels"
SORTIE = Path(__file__).resolve().parent / "figure_chaine_fr.png"

FOND = (250, 249, 247)          # le fond opaque de la série, pas de transparence
ENCRE, GRIS = (26, 26, 26), (110, 110, 110)
N = 5                            # les cinq reels en ligne au 16/09/2026
LARGE, MARGE, ECART = 1800, 56, 18
BANDEAU_H, PIED_H = 104, 74

POLICES = ("/System/Library/Fonts/Helvetica.ttc",
           "/System/Library/Fonts/Supplemental/Arial.ttf")


def police(taille: int, gras: bool = False) -> ImageFont.FreeTypeFont:
    for p in POLICES:
        if Path(p).exists():
            try:
                return ImageFont.truetype(p, taille, index=1 if gras else 0)
            except OSError:
                return ImageFont.truetype(p, taille)
    return ImageFont.load_default()


def main() -> None:
    vignette = (LARGE - 2 * MARGE - (N - 1) * ECART) // N
    hauteur_v = round(vignette * 1920 / 1080)
    haut = BANDEAU_H + hauteur_v + PIED_H
    img = Image.new("RGB", (LARGE, haut), FOND)
    d = ImageDraw.Draw(img)

    d.text((MARGE, 34), "Décarboner l'industrie — l'acier, en cinq séquences courtes",
           font=police(38, gras=True), fill=ENCRE)

    for i in range(N):
        c = Image.open(COUVS / f"acier_{i + 1}.jpg").convert("RGB")
        c = c.resize((vignette, hauteur_v), Image.LANCZOS)
        img.paste(c, (MARGE + i * (vignette + ECART), BANDEAU_H))

    d.text((MARGE, haut - PIED_H + 16),
           "youtube.com/@energy_alternatives  ·  septembre 2026",
           font=police(30), fill=GRIS)
    img.save(SORTIE)
    print(f"{SORTIE.name} — {img.size[0]}×{img.size[1]}")


if __name__ == "__main__":
    main()
