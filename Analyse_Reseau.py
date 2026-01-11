import sys
import os

print("--- 1. ANALYSEUR DE LOGS RÉSEAU ---")

# --- MODIFICATION : On demande le nom à l'utilisateur ---
fichier_entree = input("Entrez le nom du fichier à traiter (ex: fichier1000.txt) : ")

# Nettoyage du nom (enlève les guillemets si glisser-déposer)
fichier_entree = fichier_entree.strip().replace("'", "").replace('"', "")

fichier_sortie = "Resultat_Reseau.csv"

# Vérification : Est-ce que le fichier existe ?
if not os.path.exists(fichier_entree):
    print(f"❌ ERREUR : Le fichier '{fichier_entree}' n'existe pas !")
    print("Vérifie le nom ou place le fichier dans le même dossier.")
    sys.exit()

print(f"✅ Fichier trouvé ! Lecture de {fichier_entree}...")

try:
    with open(fichier_entree, 'r', encoding='utf-8') as f:
        lignes = f.readlines()
except Exception as e:
    print(f"ERREUR : Impossible de lire le fichier. {e}")
    sys.exit()

# --- TRAITEMENT DES LIGNES ---
donnees_csv = []
# On crée l'entête du tableau (séparé par des points-virgules pour Excel)
donnees_csv.append("Heure;IP_Source;IP_Dest;Flag;Info") 

print(f"Analyse de {len(lignes)} paquets en cours...")

for ligne in lignes:
    ligne = ligne.strip()
    
    # --- CORRECTION MAJEURE ICI ---
    # On utilise .split() sans rien pour gérer les espaces multiples
    morceaux = ligne.split()
    
    # On vérifie que la ligne ressemble bien à du trafic IP
    if len(morceaux) > 6 and "IP" in morceaux:
        try:
            heure = morceaux[0]      # L'heure (ex: 11:42:06...)
            
            # Recherche dynamique de la position du mot "IP"
            index_ip = morceaux.index("IP")
            
            ip_src = morceaux[index_ip + 1]     # Juste après "IP"
            ip_dest = morceaux[index_ip + 3]    # Après le ">"
            
            # Nettoyage : on enlève les deux points ":" à la fin des IP
            ip_dest = ip_dest.replace(":", "")
            
            # Recherche du Flag (S = SYN, . = ACK, etc.)
            flag = "Inconnu"
            if "Flags" in ligne:
                # On coupe au niveau de "Flags ["
                partie_flag = ligne.split("Flags [")[1]
                # On récupère juste la lettre avant le crochet "]"
                flag = partie_flag.split("]")[0]

            # On ajoute la ligne propre au tableau
            donnees_csv.append(f"{heure};{ip_src};{ip_dest};{flag};Paquet_Suspect")
            
        except Exception:
            # Si une ligne est bizarre, on l'ignore et on continue
            continue

# --- SAUVEGARDE ---
with open(fichier_sortie, 'w', encoding='utf-8') as f:
    for ligne in donnees_csv:
        f.write(ligne + "\n")

print(f"--- SUCCÈS ! ---")
print(f"Le fichier '{fichier_sortie}' a été créé.")
print("Tu peux lancer le script 2 (Graphe).")