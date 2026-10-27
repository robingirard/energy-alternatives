"""Le pic pétrolier de 2030, décomposé — et il se joue à 0,3 %.

Deux entrées, toutes deux publiées, aucune modélisation :

1. La demande mondiale de pétrole par produit raffiné, 1980-2024, en milliers de
   barils par jour. Energy Institute, Statistical Review of World Energy 2025,
   feuille « Oil - Regional Consumption », région World. Recopiée depuis
   Enseignement/Thematic_analysis/Ressources_fossiles/oil/data/.
2. Le déplacement de pétrole par les véhicules électriques : environ 5 Mb/j en
   2030, dans les deux scénarios exploratoires de l'AIE (Current Policies et
   Stated Policies). Global EV Outlook 2026, chapitre « Oil displacement ».

Depuis le 18/09, ce second chiffre n'est plus pris tel quel : il est RECONSTRUIT
à partir des ventes mondiales de voitures électriques, pour qu'on puisse y
substituer le rythme observé en 2026 au lieu du rythme supposé par l'AIE. La
reconstruction se cale toute seule sur l'AIE (voir `deplacement_2030`), ce qui
est le contrôle du procédé.

Le calcul prolonge chaque poste HORS ROUTE à son taux observé 2014-2024, et le
confronte aux 5 Mb/j. Ce n'est pas une prévision : c'est le test « à quelle
vitesse le reste devrait ralentir pour que le pic n'ait pas lieu ».

    python3 calcul_bilan_2030.py
"""
import argparse, csv, pathlib

CSV = pathlib.Path(__file__).with_name("donnees_petrole_par_produit_kbj.csv")
DEPLACEMENT_VE_2030 = 5.0        # Mb/j — AIE, Global EV Outlook 2026
A, B, HORIZON = 2014, 2024, 2030 # années de calage du taux, et cible

# ─────────────────────────────────────────────────────────────────────────────
# Le déplacement, ramené à ce qui l'engendre : les ventes mondiales de voitures.
# Toutes ces valeurs sont lues dans le Global EV Outlook 2026 (PDF archivé),
# sauf les ventes 2025, qui viennent de Rho Motion — l'AIE écrit « plus de 20
# millions », Rho Motion donne 20,7, les deux sont compatibles.
PARC_VE_LEGERS_2025 = 76.0   # millions de véhicules légers électriques (ch. 6)
DEPL_VOITURES_2025  = 1.2    # Mb/j déplacés par les seules voitures (ch. 1)
DEPL_TOTAL_2025     = 1.7    # Mb/j déplacés par tous les VE (ch. 11)
PART_VOITURES_2030  = 0.75   # part des voitures dans le déplacement de 2030,
                             # interpolée entre 70 % (2025) et 80 % (2035, ch. 11)
VENTES_VE_2025      = 20.7   # millions de voitures électriques vendues en 2025
CROISSANCE_OBSERVEE = 0.04   # +4 % — Rho Motion, cumul janvier-août 2026

GROUPES = {
    "Pétrochimie (éthane/GPL + naphta)": ["ethane_lpg", "naphtha"],
    "Aviation (kérosène)":               ["jet_kerosene"],
    "Fioul lourd":                       ["fuel_oil"],
    "Autres (bitume, lubrifiants…)":     ["others_bitumen_lubes_waxes_etc"],
}
ROUTE = ["gasoline", "diesel_gasoil"]

serie = {int(x["year"]): {k: float(v) for k, v in x.items() if k != "year"}
         for x in csv.DictReader(CSV.open(encoding="utf-8"))}

def mbj(an, cles): return sum(serie[an][c] for c in cles) / 1000
def taux(cles):    return (mbj(B, cles) / mbj(A, cles)) ** (1 / (B - A)) - 1


def deplacement_2030(croissance_ventes: float) -> float:
    """Mb/j déplacés en 2030 si les ventes mondiales croissent à ce taux annuel.

    Une règle de trois sur le parc, en trois pas :

    1. Le parc de 2030 = le parc de fin 2025 + les ventes de 2026 à 2030,
       cumulées au taux donné. Aucune sortie de parc : les VE ont en moyenne
       quatre ans, presque aucun n'atteint la casse d'ici 2030. Cette hypothèse
       SURESTIME le parc, donc le déplacement, donc le pic — elle est
       conservatrice dans le sens contraire à la conclusion ci-dessous.
    2. Le déplacement par les voitures est proportionnel au parc, au ratio
       observé en 2025 (1,2 Mb/j pour 76 millions).
    3. Ce que déplacent les camions, les bus et les deux-roues est pris à
       l'AIE tel quel : c'est le quart restant de ses 5 Mb/j de 2030, et il ne
       dépend pas de l'hypothèse sur les voitures.
    """
    ventes = sum(VENTES_VE_2025 * (1 + croissance_ventes) ** k for k in range(1, 6))
    parc = PARC_VE_LEGERS_2025 + ventes
    voitures = parc * DEPL_VOITURES_2025 / PARC_VE_LEGERS_2025
    hors_voitures = DEPLACEMENT_VE_2030 * (1 - PART_VOITURES_2030)
    return voitures + hors_voitures


def croissance_pour(cible: float) -> float:
    """Le taux de croissance des ventes qui produit `cible` Mb/j en 2030."""
    bas, haut = -0.50, 1.00
    for _ in range(200):
        milieu = (bas + haut) / 2
        if deplacement_2030(milieu) < cible: bas = milieu
        else:                                haut = milieu
    return (bas + haut) / 2

def main() -> None:
    n = HORIZON - B
    print(f"Demande mondiale {B} : {mbj(B, ['total']):.2f} Mb/j  "
          f"(dont route {mbj(B, ROUTE):.2f})\n")
    print(f"Prolongement des postes hors route à leur taux {A}-{B}, sur {n} ans :\n")
    hausse = 0.0
    for nom, cles in GROUPES.items():
        t, base = taux(cles), mbj(B, cles)
        proj = base * (1 + t) ** n
        hausse += proj - base
        print(f"  {nom:36s} {base:6.2f} → {proj:6.2f}   ({t*100:+5.2f} %/an)   {proj-base:+5.2f}")
    print(f"\n  Hausse hors route à {HORIZON}            {hausse:+6.2f} Mb/j")
    print(f"  Déplacement par les VE (AIE)        {-DEPLACEMENT_VE_2030:+6.2f} Mb/j")
    print(f"  {'-'*52}")
    solde = hausse - DEPLACEMENT_VE_2030
    print(f"  Solde, à demande routière constante {solde:+6.2f} Mb/j"
          f"   soit {100*solde/mbj(B,['total']):+.2f} % de la demande {B}")
    print(f"\n  Le pic tient à {abs(solde):.2f} Mb/j sur {mbj(B,['total']):.0f}. "
          f"C'est la marge, et c'est le sujet.")
    # Le seuil qui renverse la conclusion.
    petro = mbj(B, GROUPES["Pétrochimie (éthane/GPL + naphta)"])
    autres = GROUPES["Autres (bitume, lubrifiants…)"]
    reste = sum((mbj(B, c) * (1 + taux(c)) ** n - mbj(B, c))
                for k, c in GROUPES.items() if k != "Pétrochimie (éthane/GPL + naphta)")
    besoin = DEPLACEMENT_VE_2030 - reste
    seuil = (( (petro + besoin) / petro) ** (1 / n) - 1) * 100
    print(f"\n  Bascule : au-dessus de {seuil:+.2f} %/an de croissance pétrochimique, "
          f"il n'y a pas de pic en {HORIZON}.")
    print(f"  Taux observé {A}-{B} : {taux(GROUPES['Pétrochimie (éthane/GPL + naphta)'])*100:+.2f} %/an.")

    # Sensibilité au déplacement, qui est la seule entrée non observée du bilan.
    # Question de Robin le 17/09 : si l'accélération post-Ormuz dépasse
    # l'hypothèse de l'AIE, de combien le pic se dégage-t-il ?
    print(f"\n  Sensibilité au déplacement par les VE en {HORIZON} :")
    print(f"    {'Mb/j déplacés':>14s}  {'solde':>8s}  {'% demande':>10s}")
    for d in (4.0, 4.5, 5.0, 5.5, 6.0, 7.5):
        sd = hausse - d
        marque = "   <- AIE, CPS et STEPS" if abs(d - 5.0) < 1e-9 else (
                 "   <- AIE, NZE" if abs(d - 7.5) < 1e-9 else "")
        print(f"    {d:14.2f}  {sd:+8.2f}  {100*sd/mbj(B,['total']):+9.2f} %{marque}")

    # ── Ce que les ventes observées font au déplacement ──────────────────────
    # Question de Robin le 17/09 : l'AIE n'a-t-elle pas sous-estimé les rythmes ?
    # Les ventes de mai à septembre 2026, trouvées le 18/09, répondent — et dans
    # l'autre sens. Le bloc traduit un rythme de ventes en Mb/j déplacés.
    g_aie = croissance_pour(DEPLACEMENT_VE_2030)
    print(f"\n  Contrôle du procédé : les {DEPLACEMENT_VE_2030:.1f} Mb/j de l'AIE "
          f"correspondent à {g_aie*100:+.1f} %/an de ventes mondiales,")
    print(f"  et l'AIE suppose elle-même +15 % pour 2026 (20,0 → 23,0 millions). "
          f"La reconstruction tombe juste.")
    seuil_g = croissance_pour(hausse)   # le taux qui annule exactement le solde
    print(f"\n  Croissance des ventes mondiales de voitures électriques, "
          f"2026-2030 → pic ou pas :")
    print(f"    {'%/an':>8s}  {'parc 2030':>10s}  {'Mb/j dépl.':>11s}  {'solde':>8s}")
    for g in (0.00, 0.04, 0.08, seuil_g, 0.12, 0.15, 0.20):
        d = deplacement_2030(g)
        parc = PARC_VE_LEGERS_2025 + sum(VENTES_VE_2025 * (1+g)**k for k in range(1, 6))
        marque = ("   <- observé en 2026 (Rho Motion, janv.-août)"
                  if abs(g - CROISSANCE_OBSERVEE) < 1e-9 else
                  "   <- le seuil : en dessous, pas de pic" if abs(g - seuil_g) < 1e-9 else
                  "   <- hypothèse AIE" if abs(g - 0.15) < 1e-9 else "")
        print(f"    {g*100:+7.1f}  {parc:9.0f} M  {d:10.2f}  {hausse-d:+8.2f}{marque}")
    print(f"\n  Le seuil est à {seuil_g*100:+.1f} %/an. Les ventes mondiales ont "
          f"crû de {CROISSANCE_OBSERVEE*100:+.0f} % sur janvier-août 2026.")
    print(f"""
  ⚠️  DEUX CHOSES À NE PAS TIRER DE CE TABLEAU (Robin, 18/09) :

  1. La ligne +4 % est une BORNE BASSE, pas un scénario. Le creux de 2026 a une
     cause datée — la taxe chinoise à l'achat des VE passe de l'exonération au
     demi-tarif le 1er janvier 2026, après une ruée en fin 2025 — et un rebond
     est attendu. On ne prolonge pas un contrecoup fiscal sur quatre ans.

  2. « Déplacement » est un CONTREFACTUEL, pas un solde : les km faits par les
     VE, au litre qu'une thermique aurait bu (AIE, GEO 2026, annexe A). Il ne
     dit rien des thermiques qui SORTENT du parc. Or les ventes de voitures
     thermiques en Chine chutent de 30 % sur un an, contre 12 % pour les VE :
     cet effet-là baisse la demande de pétrole sans passer par le déplacement,
     et le bilan ci-dessus ne le voit pas. Les deux effets jouent en sens
     CONTRAIRE. Voir README.md, « La critique de Robin ».""")


if __name__ == "__main__":
    argparse.ArgumentParser(description=__doc__.splitlines()[0]).parse_args()
    main()
