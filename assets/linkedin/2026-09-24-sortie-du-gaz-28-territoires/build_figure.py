"""Douze des 28 territoires qui vont réduire leur réseau de gaz d'ici 2030.

Figure du post LinkedIn « 28 territoires pour sortir du gaz » (septembre 2026).

La figure ne calcule rien. C'est une mosaïque de photos des territoires retenus
par l'État pour réduire la taille de leur réseau de distribution de gaz. La liste
complète n'est pas publique : l'article de L'Opinion qui l'a révélée est payant,
et la presse ne reprend que douze noms. Le titre le dit (« 12 des 28 »), pour que
l'image ne se lise pas comme une liste complète. Les six métropoles sont les
seules confirmées par le dossier de presse du ministère (11/09/2026) ; les six
autres viennent de L'Opinion. Détail dans sources.md.

Les photos viennent de Wikimedia Commons. Le script refuse une licence qui ne
permet pas la réutilisation, et grave auteur et licence sur chaque vignette :
c'est la condition des licences CC BY / CC BY-SA. Provenance dans photos.json.

Deux vignettes ne montrent pas le chef-lieu du territoire, faute de photo libre
utile : elles sont légendées par le lieu réellement photographié, et ce lieu a
été vérifié dans l'intercommunalité (geo.api.gouv.fr) — Saint-Jean-en-Royans
est dans la CC du Royans-Vercors, Saint-Merd-les-Oussines dans Haute-Corrèze
Communauté. Pont-en-Royans, plus photogénique, n'y est PAS (CC Saint-Marcellin
Vercors Isère) : ne pas l'y remettre.

    python3 build_figure.py                     # deux formats, deux langues
    python3 build_figure.py --format paysage --lang fr
"""
import argparse
import hashlib
import io
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
CACHE = HERE / "photos"
PROVENANCE = HERE / "photos.json"

API = "https://commons.wikimedia.org/w/api.php"
UA = {"User-Agent": "LinkedinAtelier/1.0 (robin.girard@minesparis.psl.eu)"}
LICENCES_OK = re.compile(r"^(CC BY|CC BY-SA|CC0|Public domain|Attribution|FAL)", re.I)

# Palette : charte du cours (style_commun, palette « mines »).
SURFACE, INK, INK2 = "#ffffff", "#0E3658", "#3d5a73"
CAT_COULEUR = {"metro": "#0E3658", "agglo": "#005E9E", "rural": "#2E7D32"}

# (clé, catégorie, nom FR, nom EN, lieu photographié ou None, titre Commons, ancre)
# `ancre` : part gardée au recadrage (0 = gauche/haut, 1 = droite/bas).
TERRITOIRES = [
    ("lyon", "metro", "Lyon", "Lyon", None,
     "Lyon Panorama Saint-Jean Part-Dieu Fourvière Saone.JPG", 0.5),
    ("grenoble", "metro", "Grenoble", "Grenoble", None,
     "Grenoble-Bastille cable car - Téléphérique de Grenoble Bastille photo1.jpg", 0.5),
    ("nancy", "metro", "Nancy", "Nancy", None,
     "Nancy Place Stanislas BW 2015-07-18 13-49-46.jpg", 0.5),
    ("bordeaux", "metro", "Bordeaux", "Bordeaux", None,
     "Miroir d'eau et place de la Bourse (Bordeaux) (4).jpg", 0.35),
    ("strasbourg", "metro", "Strasbourg", "Strasbourg", None,
     "Straßburg (Frankreich), Petite France -- 2011 -- 1759.jpg", 0.5),
    ("metz", "metro", "Metz", "Metz", None,
     "Metz - View of Temple Neuf, Moselle river and Cathédrale Saint Etienne "
     "from Moyen Pont (Q22690).jpg", 0.4),
    ("bourg", "agglo", "Bassin de Bourg-en-Bresse", "Bourg-en-Bresse area", None,
     "Bourg-en-Bresse Monastère Royal de Brou Église Saint-Nicolas-de-Tolentin "
     "Extérieur Facade 1.jpg", 0.4),
    ("nevers", "agglo", "Nevers", "Nevers", None,
     "Nevers-Pont sur la Loire-Cathédrale Saint Cyr et Sainte Julitte-20160502.jpg", 0.4),
    ("annecy", "agglo", "Grand Annecy", "Greater Annecy", None,
     "Palais de l'Isle in Annecy 11.jpg", 0.5),
    ("paysbasque", "agglo", "Pays basque", "Basque Country", "Bayonne",
     "Bayonne-Nive 03.JPG", 0.5),
    ("royans", "rural", "Royans-Vercors", "Royans-Vercors", "Saint-Jean-en-Royans",
     "Saint-Jean-en-Royans from the east.jpg", 0.6),
    ("hautecorreze", "rural", "Haute-Corrèze", "Haute-Corrèze", "Saint-Merd-les-Oussines",
     "Paysage de la Réserve naturelle régionale de la haute vallée de la Vézère, "
     "la tourbière-étang de Chabannes, commune de Saint-Merd-les-Oussines, "
     "Correze, France, Europe.jpg", 0.5),
]

# Le champ « Artist » de Commons est parfois une consigne plutôt qu'un nom
# (« This picture belongs to Xavier Caré. Please credit : Xavier »). On grave le
# nom que l'auteur demande, relu sur la page du fichier.
AUTEUR = {"lyon": "Xavier Caré", "nevers": "Daniel Villafruela"}

T = {
    "fr": dict(
        titre="12 des 28 territoires qui vont réduire\nleur réseau de gaz d'ici 2030",
        soustitre=("Retenus par l'État parmi 109 territoires d'électrification. "
                   "Les 16 autres n'ont pas\nété nommés publiquement à ce jour (septembre 2026)."),
        cat={"metro": "MÉTROPOLE", "agglo": "AGGLOMÉRATION", "rural": "RURAL"},
        note=("Sources : L'Opinion, septembre 2026 ; dossier de presse du ministère chargé de "
              "l'Énergie, 11 septembre 2026.\nPhotos : Wikimedia Commons, auteur et licence "
              "sur chaque vignette.   Robin Girard, MINES Paris – PSL · 2026"),
    ),
    "en": dict(
        titre="12 of the 28 French territories set to\nshrink their gas network by 2030",
        soustitre=("Selected by the State among 109 “electrification territories”. The other 16 "
                   "have not\nbeen named publicly so far (September 2026)."),
        cat={"metro": "METROPOLIS", "agglo": "URBAN AREA", "rural": "RURAL"},
        note=("Sources: L'Opinion, September 2026; French energy ministry press kit, "
              "11 September 2026.\nPhotos: Wikimedia Commons, author and licence on each "
              "tile.   Robin Girard, MINES Paris – PSL · 2026"),
    ),
}

# Géométrie. Tout est écrit à l'échelle 1200 px de large, puis multiplié par S.
# Deux formats : `portrait` (3 × 4, 4:5 — occupe tout l'écran d'un téléphone) et
# `paysage` (4 × 3, 3:2 — le format des posts précédents, plus lisible sur ordinateur).
S = 1.5
FORMATS = {
    "portrait": dict(w=1200, h=1500, ncol=3, nlig=4, ratio=1.27, haut_titre=236,
                     titre=38, soustitre=18.5, y_soustitre=148, note=13.5, k=1.0,
                     une_ligne=False),
    "paysage": dict(w=1200, h=800, ncol=4, nlig=3, ratio=1.42, haut_titre=128,
                    titre=31, soustitre=15.5, y_soustitre=76, note=11.5, k=0.8,
                    une_ligne=True),
}
MARGE, GOUTTIERE = round(40 * S), round(12 * S)


def police(taille: float, graisse: str = "Regular") -> ImageFont.FreeTypeFont:
    for chemin in (Path.home() / f"Library/Fonts/Roboto-{graisse}.ttf",
                   Path("/System/Library/Fonts/Supplemental/Arial.ttf")):
        if chemin.exists():
            return ImageFont.truetype(str(chemin), round(taille * S))
    return ImageFont.load_default()


# --- Photos ---------------------------------------------------------------------
def _api(**kw) -> dict:
    kw.setdefault("format", "json")
    url = API + "?" + urllib.parse.urlencode(kw)
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA),
                                            timeout=90))


def _texte(html: str) -> str:
    return re.sub(r"\s+", " ", re.sub("<[^>]+>", "", html or "")).strip()


def fiche(titre: str) -> dict:
    """Métadonnées et vignette large d'un fichier Commons. Échoue si la licence n'est pas libre."""
    d = _api(action="query", titles=f"File:{titre}", prop="imageinfo",
             iiprop="url|size|extmetadata", iiurlwidth=1280)
    pages = list(d.get("query", {}).get("pages", {}).values())
    if not pages or "imageinfo" not in pages[0]:
        raise SystemExit(f"introuvable sur Commons : « {titre} »")
    ii = pages[0]["imageinfo"][0]
    em = ii.get("extmetadata", {})
    licence = _texte(em.get("LicenseShortName", {}).get("value", ""))
    if not LICENCES_OK.match(licence):
        raise SystemExit(f"licence non réutilisable pour « {titre} » : {licence or '?'}")
    auteur = _texte(em.get("Artist", {}).get("value", "")) or "auteur non nommé"
    auteur = re.split(r"\s+\d{1,2}:\d{2},", auteur)[0].strip(" ,;·")
    return dict(titre=titre, auteur=auteur[:60], licence=licence,
                page=f"https://commons.wikimedia.org/wiki/File:{urllib.parse.quote(titre)}",
                vignette=ii["thumburl"], taille=[ii["width"], ii["height"]])


def photos() -> dict[str, tuple[Image.Image, dict]]:
    """Télécharge une fois, puis relit le cache. photos.json garde la provenance."""
    CACHE.mkdir(exist_ok=True)
    prov = json.loads(PROVENANCE.read_text()) if PROVENANCE.exists() else {}
    out = {}
    for cle, *_, titre, _ancre in TERRITOIRES:
        chemin = CACHE / f"{cle}.jpg"
        if cle not in prov or prov[cle]["titre"] != titre or not chemin.exists():
            meta = fiche(titre)
            brut = urllib.request.urlopen(urllib.request.Request(meta["vignette"], headers=UA),
                                          timeout=90).read()
            Image.open(io.BytesIO(brut)).convert("RGB").save(chemin, quality=92)
            prov[cle] = meta
        out[cle] = (Image.open(chemin).convert("RGB"), prov[cle])
    PROVENANCE.write_text(json.dumps(prov, ensure_ascii=False, indent=1, sort_keys=True) + "\n")
    return out


def recadrer(im: Image.Image, ratio: float, ancre: float) -> Image.Image:
    """Rogne au format voulu sans jamais déformer."""
    w, h = im.size
    if w / h > ratio:
        nw = round(h * ratio)
        x = round((w - nw) * ancre)
        return im.crop((x, 0, x + nw, h))
    nh = round(w / ratio)
    y = round((h - nh) * ancre)
    return im.crop((0, y, w, y + nh))


# --- Mosaïque -------------------------------------------------------------------
def tuile(cle: str, im: Image.Image, meta: dict, cat: str, nom: str, lieu: str | None,
          etiquette: str, ancre: float, lang: str, tw: int, th: int, k: float) -> Image.Image:
    """Une vignette de tw × th px ; `k` réduit les textes pour le format paysage."""
    TUILE_W, TUILE_H = tw, th
    t = recadrer(im, TUILE_W / TUILE_H, ancre).resize((TUILE_W, TUILE_H), Image.LANCZOS)
    # Dégradé sombre en bas, pour que le nom reste lisible sur n'importe quelle photo.
    voile = Image.new("L", (1, TUILE_H))
    for y in range(TUILE_H):
        f = max(0.0, (y / TUILE_H - 0.45) / 0.55)
        voile.putpixel((0, y), round(200 * f ** 1.3))
    noir = Image.new("RGB", (TUILE_W, TUILE_H), (8, 16, 28))
    t = Image.composite(noir, t, voile.resize((TUILE_W, TUILE_H)))
    dr = ImageDraw.Draw(t)

    # Pastille de catégorie, en haut à gauche.
    pc = police(13 * k, "Bold")
    x0, y0 = round(10 * S * k), round(10 * S * k)
    bx = dr.textbbox((0, 0), etiquette, font=pc)
    pad = round(6 * S * k)
    dr.rounded_rectangle([x0, y0, x0 + bx[2] + 2 * pad, y0 + bx[3] + 2 * pad - round(2 * S)],
                         radius=round(4 * S), fill=CAT_COULEUR[cat])
    dr.text((x0 + pad, y0 + pad - round(1 * S)), etiquette, font=pc, fill="white")

    # Nom du territoire, et le lieu photographié quand ce n'est pas le même.
    bas = TUILE_H - round(12 * S * k)
    if lieu:
        dr.text((round(12 * S * k), bas), ("photo : " if lang == "fr" else "photo: ") + lieu,
                font=police(13 * k), fill=(235, 240, 245), anchor="ls")
        bas -= round(20 * S * k)
    taille = (27 if len(nom) <= 16 else 22) * k
    dr.text((round(12 * S * k), bas), nom, font=police(taille, "Bold"), fill="white", anchor="ls")

    # Crédit : il doit rester, c'est la condition des licences.
    credit = f"{AUTEUR.get(cle, meta['auteur'])} · {meta['licence']}"
    dr.text((TUILE_W - round(6 * S), round(6 * S)), credit, font=police(9.5 * max(k, 0.9)),
            fill=(255, 255, 255), anchor="ra", stroke_width=round(1.4 * S),
            stroke_fill=(0, 0, 0))
    return t


def construire(lang: str, ph: dict, fmt: str) -> Path:
    t, g = T[lang], FORMATS[fmt]
    W, H = round(g["w"] * S), round(g["h"] * S)
    ncol, nlig, haut_titre = g["ncol"], g["nlig"], round(g["haut_titre"] * S)
    tw = (W - 2 * MARGE - (ncol - 1) * GOUTTIERE) // ncol
    th = round(tw / g["ratio"])
    ligne = (lambda x: x.replace("\n", " ")) if g["une_ligne"] else (lambda x: x)

    fig = Image.new("RGB", (W, H), SURFACE)
    dr = ImageDraw.Draw(fig)
    dr.multiline_text((MARGE, round(34 * S)), ligne(t["titre"]), font=police(g["titre"], "Bold"),
                      fill=INK, spacing=round(6 * S))
    dr.multiline_text((MARGE, round(g["y_soustitre"] * S)), ligne(t["soustitre"]),
                      font=police(g["soustitre"]), fill=INK2, spacing=round(6 * S))

    for i, (cle, cat, nom_fr, nom_en, lieu, _titre, ancre) in enumerate(TERRITOIRES):
        im, meta = ph[cle]
        nom = nom_fr if lang == "fr" else nom_en
        x = MARGE + (i % ncol) * (tw + GOUTTIERE)
        y = haut_titre + (i // ncol) * (th + GOUTTIERE)
        fig.paste(tuile(cle, im, meta, cat, nom, lieu, t["cat"][cat], ancre, lang,
                        tw, th, g["k"]), (x, y))

    y_note = haut_titre + nlig * th + (nlig - 1) * GOUTTIERE + round(14 * S)
    dr.multiline_text((MARGE, y_note), t["note"], font=police(g["note"]), fill=INK2,
                      spacing=round(5 * S))
    if y_note + round(40 * S) > H:
        raise SystemExit(f"{fmt} : la note déborde de l'image ({y_note} px sur {H})")

    suffixe = "" if fmt == "portrait" else "_paysage"
    out = HERE / f"figure_territoires{suffixe}_{lang}.png"
    fig.save(out, optimize=True)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", choices=["fr", "en"])
    ap.add_argument("--format", choices=list(FORMATS))
    args = ap.parse_args()
    ph = photos()
    for fmt in ([args.format] if args.format else list(FORMATS)):
        for lang in ([args.lang] if args.lang else ["fr", "en"]):
            out = construire(lang, ph, fmt)
            sha = hashlib.sha256(out.read_bytes()).hexdigest()
            print(f"{out.name}  {Image.open(out).size}  sha256 {sha}")


if __name__ == "__main__":
    main()
