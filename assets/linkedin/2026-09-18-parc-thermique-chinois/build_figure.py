"""Le flux a basculé, le stock non — la part des VE dans les ventes et dans le parc.

Figure du post LinkedIn « Le parc thermique chinois ». Deux courbes et un seul
écart : la part des véhicules électriques dans les VENTES intérieures chinoises,
et leur part dans le PARC qui roule. La première est à 51 % en 2025, la seconde à
12 %. Trente-neuf points séparent ce qu'on achète de ce qui brûle de l'essence, et
c'est le stock qui brûle.

Pourquoi cette figure et pas le tableau de bascule (part de VE × taux de casse).
Le tableau montre mieux le résultat du calcul ; ces deux courbes montrent mieux
le malentendu que le post défait, et un post LinkedIn corrige un malentendu avant
de publier un résultat. Le tableau reste dans `bilan_parc_chine.py`, qui l'écrit
sur la sortie standard.

Données : `donnees_flux_stock.csv`, où chaque année porte sa provenance.

    python3 build_figure.py            # les deux langues
    python3 build_figure.py --lang fr
"""
import argparse, csv, pathlib, sys
import matplotlib.pyplot as plt

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parents[1] / "linkedinposts"))
import style_commun as style

VENTES_C = "#005E9E"   # bleu Mines : le flux, ce qu'on achète
PARC_C   = "#0E3658"   # navy : le stock, ce qui roule

T = {
 "fr": dict(
  titre="Une voiture neuve sur deux est électrique. Neuf voitures qui roulent sur dix sont thermiques.",
  millesime=("Chine, part des véhicules électriques (NEV). Ventes intérieures, exportations exclues (CAAM/CPCA via OIES) ;\n"
             "parc au 31 décembre (ministère chinois de la Sécurité publique).   Millésime : septembre 2026."),
  y="part des véhicules électriques, en %",
  lab_ventes="dans les VENTES de l'année",
  lab_parc="dans le PARC qui roule",
  ecart="trente-neuf points d'écart",
  note=("Lecture : en 2025, 51 % des voitures neuves vendues en Chine sont électriques, mais elles ne sont que 12 % du parc en\n"
        "circulation — 44 millions de véhicules sur 366. Le flux a basculé, le stock non, et c'est le stock qui brûle de l'essence.\n"
        "Pour que le parc thermique recule, vendre des électriques ne suffit pas : il faut aussi que les anciens sortent, et la\n"
        "vitesse à laquelle ils sortent est une prime à la casse, révisée chaque année.\n"
        "Unité : pourcentage de véhicules — ni des kilomètres parcourus, ni du pétrole consommé."),
 ),
 "en": dict(
  titre="One in two new cars is electric. Nine in ten cars on the road burn petrol.",
  millesime=("China, share of electric vehicles (NEV). Domestic sales, exports excluded (CAAM/CPCA via OIES); "
             "fleet at 31 December (Ministry of Public Security).   Vintage: September 2026."),
  y="share of electric vehicles, in %",
  lab_ventes="in the year's SALES",
  lab_parc="in the FLEET on the road",
  ecart="thirty-nine points apart",
  note=("How to read it: in 2025, 51 % of new cars sold in China are electric, yet they are only 12 % of the fleet on the road —\n"
        "44 million vehicles out of 366. The flow has flipped, the stock has not, and it is the stock that burns fuel.\n"
        "For the combustion fleet to shrink, selling electric cars is not enough: the old ones have to leave, and the speed at\n"
        "which they leave is a scrappage subsidy, revised every year.\n"
        "Unit: percentage of vehicles — neither of kilometres driven, nor of oil consumed."),
 ),
}


def lire():
    lignes = [l for l in (ICI / "donnees_flux_stock.csv").read_text().splitlines()
              if l and not l.startswith("#")]
    return list(csv.DictReader(lignes))


def build(lang: str, rows) -> None:
    style.use("mines")
    t = T[lang]
    an = [int(r["annee"]) for r in rows]
    ventes = [float(r["part_ventes_pct"]) for r in rows]
    parc = [float(r["part_parc_pct"]) for r in rows]

    fig, ax = plt.subplots(figsize=(9.6, 6.2))
    style.dress(ax)

    # L'écart est le sujet : on le remplit, les deux courbes n'en sont que les bords.
    ax.fill_between(an, parc, ventes, color=VENTES_C, alpha=0.11, lw=0)
    ax.plot(an, ventes, color=VENTES_C, lw=3.0, marker="o", ms=6,
            mfc=style.SURFACE, mew=2.0, zorder=3)
    ax.plot(an, parc, color=PARC_C, lw=2.4, ls=(0, (5, 2)), marker="o", ms=5.5,
            mfc=style.SURFACE, mew=1.8, zorder=3)

    virgule = (lambda s: s.replace(".", ",")) if lang == "fr" else (lambda s: s)
    for x, y, c in ((an[-1], ventes[-1], VENTES_C), (an[-1], parc[-1], PARC_C)):
        ax.annotate(virgule(f"{y:g} %"), (x, y), xytext=(10, 0),
                    textcoords="offset points", va="center", fontsize=12.5,
                    fontweight="bold", color=c)

    # La flèche à double tête dit l'écart sans qu'on ait à soustraire de tête.
    xe = an[-1] - 0.42
    ax.annotate("", xy=(xe, ventes[-1]), xytext=(xe, parc[-1]),
                arrowprops=dict(arrowstyle="<->", color=style.INK2, lw=1.1))
    ax.text(xe - 0.12, (ventes[-1] + parc[-1]) / 2, t["ecart"], rotation=90,
            ha="right", va="center", fontsize=9.6, color=style.INK2)

    # Les deux libellés vont dans le vide laissé par les courbes, pas dessus :
    # « VENTES » au-dessus du flux entre 2021 et 2022, « PARC » sous le stock.
    ax.text(an[0] + 0.15, 37.0, t["lab_ventes"], fontsize=10.6,
            fontweight="bold", color=VENTES_C, va="bottom")
    ax.text(an[1], -2.6, t["lab_parc"], fontsize=10.6,
            fontweight="bold", color=PARC_C, va="top")

    ax.set_xticks(an)
    ax.set_xticklabels([str(a) for a in an], fontsize=10.5, color=style.INK)
    ax.set_xlim(an[0] - 0.25, an[-1] + 0.85)
    ax.set_ylim(-5.5, 58)
    ax.set_yticks([0, 10, 20, 30, 40, 50])
    ax.set_ylabel(t["y"], fontsize=10.5, color=style.INK)
    ax.set_title(t["titre"], fontsize=13, color=style.INK, pad=44, loc="left")
    ax.text(0, 1.035, t["millesime"], transform=ax.transAxes, fontsize=8.3,
            color=style.INK2, va="bottom", linespacing=1.5)
    fig.text(0.012, 0.015, t["note"], fontsize=7.8, color=style.INK2, linespacing=1.5)
    fig.tight_layout(rect=(0, 0.135, 1, 1))

    out = ICI / f"figure_flux_stock_{lang}.png"
    fig.savefig(out, dpi=170, facecolor=style.SURFACE)
    plt.close(fig)
    # Fond OPAQUE, règle n°1 de ../../README.md : un PNG en RGBA est aplati sur
    # blanc ou sur noir selon le thème du lecteur, et le gris disparaît.
    from PIL import Image
    Image.open(out).convert("RGB").save(out)
    print(f"  {out.name}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", choices=("fr", "en", "both"), default="both")
    a = ap.parse_args()
    rows = lire()
    print("écart ventes − parc, en points : " +
          ", ".join(f"{r['annee']} {float(r['part_ventes_pct']) - float(r['part_parc_pct']):.1f}"
                    for r in rows))
    for lg in (("fr", "en") if a.lang == "both" else (a.lang,)):
        build(lg, rows)
