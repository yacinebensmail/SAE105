import markdown
import codecs
import sys
import datetime

# --- CONFIGURATION ---
image_1 = "Preuve_1_IP_Attaquant.png"
image_2 = "Preuve_2_Type_Attaque.png"
fichier_sortie = "Rapport_Incident_Reseau.html"
date_du_jour = datetime.datetime.now().strftime("%d/%m/%Y à %H:%M")

print("--- 3. GÉNÉRATEUR DE RAPPORT ---")

# Questions interactives pour remplir le rapport
nom_fichier = input("Quel fichier as-tu analysé ? (ex: logs_mars.txt) : ")
if nom_fichier == "": nom_fichier = "fichier_inconnu.txt"

ip_coupable = input("Quelle est l'IP de l'attaquant ? (regarde tes graphes) : ")
if ip_coupable == "": ip_coupable = "IP_NON_IDENTIFIÉE"

print("Génération du rapport HTML...")

# Contenu du rapport (Markdown)
texte_md = f"""
# 🛡️ Rapport d'Incident de Sécurité
### 📅 Date : {date_du_jour} | Document Confidentiel

<div class="alert-box">
<strong>ALERTE CRITIQUE</strong><br>
Analyse du fichier : <code>{nom_fichier}</code>.
</div>

## 1. Contexte
Suite à des lenteurs réseaux, nous avons analysé les logs bruts.
L'objectif est d'identifier la machine responsable de la saturation.

## 2. Preuve de l'Attaquant
Le graphique montre clairement une IP qui envoie beaucoup plus de données que les autres.

![Top Attaquants]({image_1})

* **IP Coupable :** `{ip_coupable}`
* **Volume :** Trafic anormalement élevé détecté.

## 3. Type d'Attaque (Flags)
L'analyse des "Flags" TCP permet de comprendre la méthode utilisée.

![Répartition Flags]({image_2})

* **Verdict :** Tentative de saturation (Déni de Service / DoS).

## 4. Actions Prises
1.  **Blocage** immédiat de l'IP `{ip_coupable}`.
2.  Sauvegarde des logs pour preuve.

---
*Généré par l'outil d'analyse SAÉ 1.05*
"""

# Transformation en HTML
try:
    html_corps = markdown.markdown(texte_md)
    
    html_final = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="utf-8">
        <title>Rapport Sécurité</title>
        <style>
            body {{ font-family: sans-serif; padding: 40px; background: #f4f4f4; }}
            .container {{ max-width: 800px; margin: auto; background: white; padding: 40px; border-radius: 8px; }}
            h1 {{ color: #c0392b; text-align: center; border-bottom: 2px solid #ddd; padding-bottom: 10px; }}
            h2 {{ color: #2980b9; margin-top: 30px; }}
            .alert-box {{ background: #fadbd8; border: 1px solid #e74c3c; color: #a93226; padding: 15px; text-align: center; font-weight: bold; border-radius: 5px; }}
            img {{ display: block; margin: 20px auto; max-width: 100%; border: 1px solid #ddd; }}
            code {{ background: #eee; padding: 3px; border-radius: 3px; }}
        </style>
    </head>
    <body>
        <div class="container">
            {html_corps}
        </div>
    </body>
    </html>
    """

    with codecs.open(fichier_sortie, "w", encoding="utf-8") as f:
        f.write(html_final)
        
    print(f"✅ SUCCÈS ! Rapport généré : {fichier_sortie}")
    print("Ouvre ce fichier pour voir ton travail final.")

except Exception as e:
    print(f"Erreur : {e}")
    print("As-tu bien installé markdown ? (pip install markdown)")