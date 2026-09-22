"""Deux étages du calcul — le facteur MACF, et l'assiette sur laquelle il porte.

Variante « avant / après » de la figure du post MACF. Le reproche fait à la
version 1 : on y annote la décision du Conseil du 16 septembre 2026 sans jamais
la montrer. On ne peut pas la montrer sur le facteur MACF, parce qu'elle ne le
touche pas (c'est le piège du post, voir sources.md §5). Mais elle a un
avant/après, et il est ailleurs : dans les référentiels de repli.

  panneau gauche  — le facteur MACF : quelle FRACTION de l'allocation reste
                    gratuite. Directive (UE) 2023/959. Inchangé par le vote.
  panneau droit   — les référentiels chaleur et combustibles : SUR QUELLE
                    ASSIETTE ce pourcentage s'applique. Avant = règlement
                    d'exécution (UE) 2026/1412 du 26 juin 2026 ; après =
                    mandat du Conseil du 16 septembre 2026.

Les deux valeurs de droite sont lues, pas déduites : 31,2 et 28,1 quotas/TJ en
annexe du règlement de juin, 43,0 et 38,7 dans le mandat du Conseil. Le rapport
2021-2025 (≈ 47,3) n'apparaît PAS ici : il est déduit et non vérifié
(sources.md, alerte du point 2).

    python3 build_figure_v2.py            # les deux langues
    python3 build_figure_v2.py --lang fr
"""
import argparse, pathlib, sys
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "linkedinposts"))
import style_commun as style

# (année, facteur MACF en %) — directive (UE) 2023/959, art. 10 bis §1 bis.
FACTEUR = [(2025, 100.0), (2026, 97.5), (2027, 95.0), (2028, 90.0), (2029, 77.5),
           (2030, 51.5), (2031, 39.0), (2032, 26.5), (2033, 14.0), (2034, 0.0)]

# (référentiel, valeur de juin 2026, valeur après correction, repère gaz)
# Valeurs : règl. d'exécution (UE) 2026/1412, annexe section 3 ; mandat Coreper
# du 16/09/2026. Toutes en quotas/TJ, et 1 quota = 1 tCO2e.
#
# Le repère est la grandeur physique sur laquelle chaque référentiel de repli a
# été construit — c'est ce qui rend les barres représentables :
#   chaleur      : une chaudière à gaz à haut rendement, 62,3 tCO2e par TJ de
#                  CHALEUR utile (56,1 kgCO2/GJ de gaz ÷ 90 % de rendement) ;
#   combustibles : la combustion du gaz elle-même, 56,1 tCO2e par TJ de
#                  COMBUSTIBLE (pas de rendement à appliquer : le dénominateur
#                  est déjà le combustible consommé).
# Les deux référentiels tombent aux mêmes 50 % / 69 % de leur repère : ils ont
# été coupés puis relevés du même taux.
# (référentiel, 2021-2025, juin 2026, Conseil sept. 2026, repère gaz, clé)
# 2021-2025 : fiches de référentiels de la DG CLIMA accompagnant le règlement
# d'exécution (UE) 2021/447 — « Benchmark value for 2021-2025 » : 47,3 et 42,6.
# Sans cette troisième barre, la figure disait « + 38 % » et laissait croire à
# un cadeau net. Avec elle, on voit que juin coupait d'un tiers et que le
# Conseil ne rend pas tout : le solde reste à − 9 % de la période précédente.
REPLI = [("chaleur", 47.3, 31.2, 43.0, 62.3, "rc"),
         ("combustibles", 42.6, 28.1, 38.7, 56.1, "rf")]

T = {
 "fr": dict(
  sur="Le vote du 16 septembre ne touche pas le calendrier. Il rend ce que juin avait pris.",
  millesime="Directive (UE) 2023/959 · règlement (UE) 2026/1412 · Conseil, 16 septembre 2026.   Millésime : septembre 2026.",
  tg="La fraction qui reste gratuite",
  tg2="facteur MACF — inchangé",
  td="L'assiette sur laquelle elle porte",
  td2="référentiels de repli — juin prend, septembre rend",
  rc="chaudière à gaz",
  rf="combustion du gaz",
  yg="part de l'allocation de référence, en %",
  yd="quotas gratuits par térajoule\n(1 quota = 1 tCO₂e)",
  lab_gratuit="quotas encore alloués gratuitement",
  lab_payant="exposé au prix du carbone",
  lab_socle="2021-2025, période précédente",
  lab_avant="règlement du 26 juin 2026",
  m1="− {p} %", m2="+ {p} %",
  lab_apres="après le Conseil du 16 sept. 2026",
  noms=["référentiel\nchaleur", "référentiel\ncombustibles"],
  note=("En 2026, 2,5 % de l'allocation est exposée au prix du carbone (gauche) ; relever les référentiels de 38 % (droite) ne change pas ce calendrier, cela augmente la dotation à laquelle il s'applique.\n"
        "Lecture des barres de droite, en fraction du repère gaz : 76 % sur 2021-2025, 50 % après le règlement de juin, 69 % après le Conseil. Le solde reste à − 9 % de la période précédente."),
 ),
 "en": dict(
  sur="The 16 September vote does not touch the schedule. It gives back what June took.",
  millesime="Directive (EU) 2023/959 · Regulation (EU) 2026/1412 · Council, 16 September 2026.   Vintage: September 2026.",
  tg="The share that stays free",
  tg2="CBAM factor — unchanged",
  td="The base it applies to",
  td2="fallback benchmarks — June takes, September returns",
  rc="gas boiler",
  rf="gas combustion",
  yg="share of the reference allocation, in %",
  yd="free allowances per terajoule\n(1 allowance = 1 tCO₂e)",
  lab_gratuit="allowances still handed out for free",
  lab_payant="exposed to the carbon price",
  lab_socle="2021-2025, previous period",
  lab_avant="Regulation of 26 June 2026",
  m1="− {p} %", m2="+ {p} %",
  lab_apres="after the Council of 16 Sept. 2026",
  noms=["heat\nbenchmark", "fuel\nbenchmark"],
  note=("In 2026, 2.5 % of the allocation is exposed to the carbon price (left); raising the benchmarks by 38 % (right) does not change that schedule, it increases the allocation it applies to.\n"
        "Reading the right-hand bars, as a share of the gas reference: 76 % over 2021-2025, 50 % after the June Regulation, 69 % after the Council. The net is still − 9 % below the previous period."),
 ),
}


def num(x, lang, dec=1):
    s = f"{x:.{dec}f}"
    return s.replace(".", ",") if lang == "fr" else s


def build(lang: str) -> None:
    style.use("mines")
    t = T[lang]
    fig, (axg, axd) = plt.subplots(
        1, 2, figsize=(12.4, 6.4), gridspec_kw=dict(width_ratios=[2.45, 1], wspace=0.24))
    for ax in (axg, axd):
        style.dress(ax)

    c_gratuit = style.COMPONENT_COLORS["Energy & supply"]        # froid : ce qui reste donné
    c_payant = style.COMPONENT_COLORS["Environmental & excise"]  # chaud : ce que le carbone prend

    # ---- gauche : le facteur MACF, identique à la version 1 -----------------
    xs = range(len(FACTEUR))
    for i, (an, f) in zip(xs, FACTEUR):
        axg.bar(i, f, color=c_gratuit, width=0.66)
        axg.bar(i, 100 - f, bottom=f, color=c_payant, width=0.66)
        if 100 - f >= 2:
            axg.text(i, 101.5, f"{num(100 - f, lang, 1).rstrip('0').rstrip(',.')} %", ha="center", fontsize=9.6,
                     color=style.readable(c_payant), fontweight="bold")

    leg = axg.legend(handles=[Patch(facecolor=c_payant, label=t["lab_payant"]),
                              Patch(facecolor=c_gratuit, label=t["lab_gratuit"])],
                     loc="lower left", bbox_to_anchor=(0.005, 0.012), ncol=1,
                     frameon=True, framealpha=0.92, edgecolor="none",
                     facecolor=style.SURFACE, fontsize=9.2,
                     handlelength=1.4, handleheight=1.0)
    for txt in leg.get_texts():
        txt.set_color(style.INK)

    axg.set_xticks(list(xs))
    axg.set_xticklabels([str(a) for a, _ in FACTEUR], fontsize=9.6, color=style.INK)
    axg.set_ylabel(t["yg"], fontsize=10, color=style.INK)
    axg.set_ylim(0, 112)
    axg.set_yticks([0, 25, 50, 75, 100])

    # ---- droite : l'assiette, avant / après --------------------------------
    # Gris pour l'avant, couleur pleine pour l'après : l'œil va sur ce qui a été
    # ajouté, et la surface ajoutée est la mesure elle-même.
    c_socle, c_avant, c_apres = "#dadada", style.MUTED, c_gratuit
    w = 0.25
    for j, (_nom, socle, avant, apres, repere, cle) in enumerate(REPLI):
        xs3 = (j - w - 0.015, j, j + w + 0.015)
        for x, v, col, gras in ((xs3[0], socle, c_socle, False),
                                (xs3[1], avant, c_avant, False),
                                (xs3[2], apres, c_apres, True)):
            axd.bar(x, v, width=w, color=col)
            axd.text(x, v + 0.9, num(v, lang), ha="center", fontsize=9.2,
                     color=style.INK if gras else style.INK2,
                     fontweight="bold" if gras else "normal")
            axd.text(x, v / 2, num(round(v / repere * 100), lang, 0) + " %",
                     ha="center", va="center", fontsize=9.2,
                     color=style.SURFACE if gras else style.INK,
                     fontweight="bold" if gras else "normal")
        # les deux mouvements, chacun au-dessus de son couple de barres
        if j == 0:
            for x0, x1, v0, v1, lab in (
                    (xs3[0], xs3[1], socle, avant, t["m1"].format(
                        p=num(abs(round((avant / socle - 1) * 100)), lang, 0))),
                    (xs3[1], xs3[2], avant, apres, t["m2"].format(
                        p=num(round((apres / avant - 1) * 100), lang, 0)))):
                y = max(v0, v1) + 7.0
                axd.annotate("", xy=(x1, y), xytext=(x0, y),
                             arrowprops=dict(arrowstyle="->", color=style.INK2, lw=1.0))
                axd.text((x0 + x1) / 2, y + 1.2, lab, ha="center", fontsize=9.4,
                         color=style.INK, fontweight="bold")
        # le repère physique du référentiel
        axd.plot([j - 0.44, j + 0.44], [repere, repere], color=style.INK2,
                 lw=1.1, ls=(0, (5, 3)), zorder=3)
        axd.text(j, repere + 1.0, f"{t[cle]} — {num(repere, lang)}",
                 ha="center", fontsize=8.6, color=style.INK2)

    legd = axd.legend(handles=[Patch(facecolor=c_socle, label=t["lab_socle"]),
                               Patch(facecolor=c_avant, label=t["lab_avant"]),
                               Patch(facecolor=c_apres, label=t["lab_apres"])],
                      loc="upper left", bbox_to_anchor=(0.005, 0.995), ncol=1,
                      frameon=True, framealpha=0.92, edgecolor="none",
                      facecolor=style.SURFACE, fontsize=9.2,
                      handlelength=1.4, handleheight=1.0)
    for txt in legd.get_texts():
        txt.set_color(style.INK)

    axd.set_xticks(range(len(REPLI)))
    axd.set_xticklabels(t["noms"], fontsize=9.6, color=style.INK)
    axd.set_xlim(-0.70, len(REPLI) - 0.30)
    axd.set_ylabel(t["yd"], fontsize=10, color=style.INK)
    axd.set_ylim(0, 84)

    # ---- titres de panneaux et chapeau -------------------------------------
    # Marges explicites : tight_layout se bat avec les textes posés en
    # coordonnées de figure et empile le chapeau sur les titres de panneaux.
    fig.subplots_adjust(left=0.062, right=0.985, top=0.775, bottom=0.145, wspace=0.26)

    for ax, titre, sous in ((axg, t["tg"], t["tg2"]), (axd, t["td"], t["td2"])):
        ax.set_title(titre, fontsize=12.2, color=style.INK, pad=40, loc="left")
        ax.text(0, 1.045, sous, transform=ax.transAxes, fontsize=8.8,
                color=style.INK2, va="bottom")

    fig.suptitle(t["sur"], fontsize=14.5, color=style.INK, x=0.012, y=0.962,
                 ha="left")
    fig.text(0.012, 0.905, t["millesime"], fontsize=8.6, color=style.INK2, va="bottom")
    fig.text(0.012, 0.022, t["note"], fontsize=8.4, color=style.INK2, linespacing=1.6)

    out = f"figure_macf_v2_{lang}.png"
    fig.savefig(out, dpi=170, facecolor=style.SURFACE)
    plt.close(fig)
    from PIL import Image
    Image.open(out).convert("RGB").save(out)   # fond opaque, règle n°1
    print(f"  {out}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", choices=("fr", "en", "both"), default="both")
    a = ap.parse_args()
    for nom, socle, avant, apres, repere, _cle in REPLI:
        print(f"référentiel {nom:12} : {socle} -> {avant} -> {apres} quotas/TJ   "
              f"({(avant/socle-1)*100:+.0f} % puis {(apres/avant-1)*100:+.0f} %, "
              f"solde {(apres/socle-1)*100:+.1f} %)   "
              f"{socle/repere:.0%} / {avant/repere:.0%} / {apres/repere:.0%} du repère {repere}")
    for lg in (("fr", "en") if a.lang == "both" else (a.lang,)):
        build(lg)
