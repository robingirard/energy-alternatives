import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager

# Langue : `python fig_emissions_pfas_europe.py [fr|en]`, francais par defaut.
# Le francais garde le nom de fichier historique, l'anglais prend le suffixe _en.
LANG = sys.argv[1] if len(sys.argv) > 1 else "fr"
assert LANG in ("fr", "en"), "langue attendue : fr ou en"
EN = LANG == "en"

# Données : émissions de PFAS en Europe (t/an), avis RAC de l'ECHA (2025-2026),
# évaluations sectorielles « Applications of fluorinated gases » et « Transport ».
USES = [
    (("Climatisation automobile", "Mobile air conditioning"), 17129, True),
    (("Climatisation et PAC fixes\n(bâtiment, inclut le R32)",
      "Stationary AC and heat pumps\n(buildings, includes R32)"), 13326, True),
    (("Réfrigération commerciale", "Commercial refrigeration"), 13050, True),
    (("Textiles, cuir, tapis", "Textiles, leather, carpets"), 6526, False),
    (("Mousses isolantes", "Insulation foams"), 5822, False),
    (("Réfrigération industrielle", "Industrial refrigeration"), 3987, True),
    (("Aérosols et propulseurs techniques", "Aerosols and technical propellants"), 1952, False),
    (("Froid des transports", "Transport refrigeration"), 1764, True),
    (("Agents extincteurs", "Fire suppressants"), 942, False),
    (("Lubrifiants", "Lubricants"), 815, False),
    (("Emballages alimentaires", "Food packaging"), 582, False),
    (("Électronique, semi-conducteurs", "Electronics, semiconductors"), 440, False),
    (("Produits de construction", "Construction products"), 426, False),
    (("Réfrigération domestique", "Domestic refrigeration"), 267, True),
    (("Dispositifs médicaux", "Medical devices"), 127, False),
]
data = [(lab[1] if EN else lab[0], v, c) for lab, v, c in USES]
total = 68315
listed = sum(v for _, v, _ in data)
data.append(("Other uses" if EN else "Autres usages", total - listed, False))

BLUE, GRAY = "#2a78d6", "#c3c2b7"
INK, INK2, MUTED, GRID, SURF = "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#fcfcfb"

plt.rcParams.update({"font.family": ["Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans"],
                     "font.size": 11})
fig, ax = plt.subplots(figsize=(10.5, 6.3), dpi=160)
fig.patch.set_facecolor(SURF); ax.set_facecolor(SURF)

labels = [d[0] for d in data][::-1]
vals = [d[1] for d in data][::-1]
cols = [BLUE if d[2] else GRAY for d in data][::-1]
y = range(len(vals))
ax.barh(y, vals, color=cols, height=0.62, zorder=3)
ax.set_yticks(list(y)); ax.set_yticklabels(labels, color=INK, fontsize=11)
for yi, v in zip(y, vals):
    ax.text(v + 250, yi, f"{v:,}".replace(",", "," if EN else " "), va="center", ha="left",
            color=INK2, fontsize=10.5, zorder=4)
ax.set_xlim(0, 20500)
ax.set_xticks([0, 5000, 10000, 15000, 20000])
ax.set_xticklabels(["0", "5,000", "10,000", "15,000", "20,000"] if EN
                   else ["0", "5 000", "10 000", "15 000", "20 000"], color=MUTED)
ax.xaxis.grid(True, color=GRID, lw=1, zorder=0); ax.set_axisbelow(True)
for s in ["top", "right", "left"]: ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(GRID)
ax.tick_params(axis="both", length=0)
ax.set_xlabel("Estimated PFAS emissions in Europe (tonnes per year)" if EN
              else "Émissions de PFAS estimées en Europe (tonnes par an)", color=INK2, fontsize=11)
ax.set_title("Where do PFAS emissions in Europe come from? Total: 68,315 t/yr" if EN
             else "D'où viennent les émissions de PFAS en Europe ? Total : 68 315 t/an",
             loc="left", color=INK, fontsize=14, fontweight="bold", pad=14)
# légende manuelle (2 séries → légende obligatoire)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=BLUE, label="Refrigeration, air conditioning, heat pumps (refrigerants)" if EN
                         else "Froid, climatisation, pompes à chaleur (fluides frigorigènes)"),
                   Patch(color=GRAY, label="Other PFAS uses" if EN else "Autres usages des PFAS")],
          loc="lower right", frameon=False, fontsize=10.5, labelcolor=INK2)
SOURCE_EN = ("Source: opinion of RAC (ECHA's Committee for Risk Assessment) on the PFAS restriction, "
             "sectoral evaluations \u201cfluorinated gases\u201d and \u201ctransport\u201d.\n"
             "The \u201cstationary AC and heat pumps\u201d item includes, by ECHA convention, R32, which is not a PFAS.")
SOURCE_FR = ("Source : avis du RAC (comité d'évaluation des risques de l'ECHA) sur la restriction PFAS, "
             "évaluations sectorielles « gaz fluorés » et « transport ».\n"
             "Le poste « climatisation et PAC fixes » inclut par convention de l'ECHA le R32, qui n'est pourtant pas un PFAS.")
ax.text(0, -0.13, SOURCE_EN if EN else SOURCE_FR,
        transform=ax.transAxes, color=MUTED, fontsize=9, va="top")
fig.tight_layout()
# Écrit dans le dossier courant : `python3 fig_emissions_pfas_europe.py [fr|en]`
out = "pfas_emissions_europe%s.png" % ("_en" if EN else "")
fig.savefig(out, facecolor=SURF, bbox_inches="tight", pad_inches=0.3)
print("wrote", out)
