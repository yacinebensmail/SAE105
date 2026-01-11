import matplotlib.pyplot as plt
import sys
import os

print("--- 2. GÉNÉRATEUR DE GRAPHIQUES ---")

# On demande le fichier (Appuie juste sur Entrée pour le défaut)
fichier_csv = input("Nom du fichier CSV (Entrée pour 'Resultat_Reseau.csv') : ")

if fichier_csv == "":
    fichier_csv = "Resultat_Reseau.csv"

# Nettoyage
fichier_csv = fichier_csv.strip().replace("'", "").replace('"', "")

if not os.path.exists(fichier_csv):
    print(f"❌ ERREUR : Le fichier '{fichier_csv}' est introuvable !")
    print("Lance d'abord l'étape 1 (Analyse_Reseau.py).")
    sys.exit()

print(f"✅ Lecture de {fichier_csv}...")

# Compteurs
compteur_ip = {}   
compteur_flag = {} 

# Lecture du CSV
try:
    with open(fichier_csv, 'r', encoding='utf-8') as f:
        lignes = f.readlines()
except Exception as e:
    print(f"Erreur : {e}")
    sys.exit()

# Analyse des données
for ligne in lignes[1:]: # On saute la première ligne (titres)
    colonnes = ligne.strip().split(";")
    if len(colonnes) < 4: continue
    
    ip_src = colonnes[1]
    flag = colonnes[3]
    
    # Compte IP
    if ip_src in compteur_ip:
        compteur_ip[ip_src] += 1
    else:
        compteur_ip[ip_src] = 1
        
    # Compte Flag
    if flag in compteur_flag:
        compteur_flag[flag] += 1
    else:
        compteur_flag[flag] = 1

# --- GRAPHIQUE 1 : TOP 5 IPs (Barres) ---
top_ips = sorted(compteur_ip.items(), key=lambda x: x[1], reverse=True)[:5]
noms_ip = [x[0] for x in top_ips]
valeurs_ip = [x[1] for x in top_ips]

plt.figure(figsize=(10, 6))
plt.bar(noms_ip, valeurs_ip, color='red')
plt.title(f"TOP 5 IPs Suspectes - Source: {fichier_csv}")
plt.ylabel("Nombre de paquets")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("Preuve_1_IP_Attaquant.png")
print("-> Image 1 générée : Preuve_1_IP_Attaquant.png")

# --- GRAPHIQUE 2 : TYPES D'ATTAQUE (Camembert) ---
labels = list(compteur_flag.keys())
sizes = list(compteur_flag.values())

plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Répartition des Flags TCP (Types d'attaques)")
plt.savefig("Preuve_2_Type_Attaque.png")
print("-> Image 2 générée : Preuve_2_Type_Attaque.png")

print("TERMINÉ ! Tu peux lancer le script 3 (Rapport).")