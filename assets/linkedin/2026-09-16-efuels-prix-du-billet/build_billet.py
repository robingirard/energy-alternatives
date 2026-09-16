"""Le billet de 1 500 km : surcoût de l'e-kérosène, et l'accise que ce vol ne paie pas.

Maquette d'atelier. Le code définitif ira dans `linkedinposts/efuels_aviation/`
quand les hypothèses seront arrêtées.

    python3 build_billet.py --lang fr
    python3 build_billet.py --lang en
"""
import argparse, sys, matplotlib.pyplot as plt
sys.path.insert(0, "/Users/rgirard/Documents/Communication/Linkedin/linkedinposts")
import style_commun as style

DIST, L_100PKM = 1500, 3.5                       # km ; L/100 pass.-km (DGAC/IATA)
PRIX_KERO = 0.678                                # €/L, kérosène soutes, France 2024
ACCISE_ROUTIER, ACCISE_ESSENCE = 0.4519, 0.691   # €/L : taux plancher TRM 2025 ; TICPE essence 2024
LITRES = L_100PKM * DIST / 100                   # 52,5 L par passager
BASE = LITRES * PRIX_KERO                        # 35,6 €

# (année, taux d'incorporation e-SAF de ReFuelEU, prix e-SAF / kérosène fossile)
JALONS = [("", 0.0, 1), ("2030", 0.012, 8), ("2035", 0.05, 6),
          ("2040", 0.10, 4.5), ("2045", 0.15, 3.5), ("2050", 0.35, 3)]

T = {
 "fr": dict(
  titre="Un vol de 1 500 km : le surcoût de l'e-kérosène, et l'accise que ce vol ne paie pas",
  millesime="Prix du kérosène et accises : France, 2024-2025.   Taux d'incorporation : ReFuelEU Aviation, 2030-2050.",
  auj="aujourd'hui\n2 % de bio-SAF", socle="le carburant\n{v:.0f} €\npar passager",
  y="euros par passager",
  routier="ce qu'un transporteur routier paie d'accise sur les mêmes 52 litres  —  24 €",
  essence="ce qu'un automobiliste paie sur les mêmes 52 litres  —  36 €",
  note=("Barcelone-Berlin, 3,5 L/100 passagers-km, kérosène des soutes à 0,678 €/L (France, 2024, dernier millésime publié). "
        "Prix de l'e-SAF supposé passer de ×8 du fossile en 2030 à ×3 en 2050.\n"
        "Accises : 45,19 c€/L, taux plancher du gazole professionnel après remboursement (2025) ; 69,1 c€/L, essence (2024).\n"
        "Le kérosène des soutes internationales n'est ni accisé ni soumis à la TVA : la barre bleue est tout ce que ce vol paie.")),
 "en": dict(
  titre="A 1,500 km flight: what e-kerosene adds, and the excise this flight does not pay",
  millesime="Kerosene price and excise rates: France, 2024-2025.   Blending mandate: ReFuelEU Aviation, 2030-2050.",
  auj="today\n2 % bio-SAF", socle="the fuel\n€{v:.0f}\nper passenger",
  y="euros per passenger",
  routier="what a road haulier pays in excise on the same 52 litres  —  €24",
  essence="what a motorist pays on the same 52 litres  —  €36",
  note=("Barcelona-Berlin, 3.5 L/100 passenger-km, bunker kerosene at €0.678/L (France, 2024, last published vintage). "
        "e-SAF price assumed to fall from 8× fossil in 2030 to 3× in 2050.\n"
        "Excise: 45.19 c€/L, floor rate on professional diesel after rebate (2025); 69.1 c€/L, petrol (2024).\n"
        "International bunker kerosene bears neither excise nor VAT: the dark bar is all this flight pays.")),
}

def build(lang: str) -> None:
    style.use("mines")
    t = T[lang]
    fig, ax = plt.subplots(figsize=(9.2, 6.0))
    style.dress(ax)
    c_kero = style.COMPONENT_COLORS["Energy & supply"]
    c_esaf = style.COMPONENT_COLORS["Network"]
    c_taxe = style.COMPONENT_COLORS["Environmental & excise"]

    for i, (an, a, x) in enumerate(JALONS):
        sur = BASE * a * (x - 1)
        ax.bar(i, BASE, color=c_kero, width=0.62)
        ax.bar(i, sur, bottom=BASE, color=c_esaf, width=0.62)
        if sur > 0.5:
            ax.text(i, BASE + sur + 1.1, f"+{sur:.0f} €", ha="center", fontsize=10.5,
                    color=style.readable(c_esaf), fontweight="bold")
    ax.text(0, BASE / 2, t["socle"].format(v=BASE), va="center", ha="center",
            fontsize=9.2, color="white", fontweight="bold", linespacing=1.45)

    for niveau, txt in ((ACCISE_ROUTIER, t["routier"]), (ACCISE_ESSENCE, t["essence"])):
        y = BASE + LITRES * niveau
        ax.axhline(y, color=c_taxe, lw=1.5, ls="--")
        ax.text(-0.44, y + 1.0, txt, ha="left", fontsize=9.5, color=style.readable(c_taxe))

    pct = {"fr": lambda v: f"{v:.1f} %".replace(".", ",").replace(",0 ", " "),
           "en": lambda v: f"{v:.1f} %".replace(".0 ", " ")}[lang]
    ax.set_xticks(range(len(JALONS)))
    ax.set_xticklabels([t["auj"] if not an else f"{an}\n{pct(a * 100)}" for an, a, _ in JALONS],
                       fontsize=9.5, color=style.INK)
    ax.set_ylabel(t["y"], fontsize=10.5, color=style.INK)
    ax.set_ylim(0, 82)
    ax.set_title(t["titre"], fontsize=12.5, color=style.INK, pad=26, loc="left")
    ax.text(0, 1.028, t["millesime"], transform=ax.transAxes, fontsize=9,
            color=style.INK2, va="bottom")
    fig.text(0.012, 0.015, t["note"], fontsize=7.8, color=style.INK2, linespacing=1.5)
    fig.tight_layout(rect=(0, 0.095, 1, 1))
    out = f"figure_billet_{lang}.png"
    fig.savefig(out, dpi=170, facecolor=style.SURFACE)
    plt.close(fig)
    # Fond OPAQUE, règle n°1 du ../README.md : un PNG en RGBA est aplati sur
    # blanc ou sur noir selon le thème du lecteur, et le gris disparaît.
    from PIL import Image
    Image.open(out).convert("RGB").save(out)
    print(f"  {out}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", choices=("fr", "en", "both"), default="both")
    a = ap.parse_args()
    print(f"{LITRES:.1f} L/passager, carburant {BASE:.1f} € ; "
          f"accise routier {LITRES*ACCISE_ROUTIER:.1f} €, essence {LITRES*ACCISE_ESSENCE:.1f} €")
    for lg in (("fr", "en") if a.lang == "both" else (a.lang,)):
        build(lg)
