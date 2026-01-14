# 🛡️ Network Traffic Analyzer (SAE 1.05)

**Student:** Yacine Bensmail (BUT R&T - IUT de Roanne)
**Context:** Network investigation for the India production site.

---

## 📋 Project Overview
This repository contains a set of Python tools designed to analyze raw network logs (`tcpdump` format).
The goal is to identify the cause of the network saturation reported between the France (Admin) and India (Production) sites.

### Key Features
* **Data Extraction:** Parses complex text logs into structured CSV files compatible with Excel.
* **Visualization:** Generates graphs (Bar charts & Pie charts) to spot the attacker immediately.
* **Reporting:** Creates an automated HTML incident report for management.

---

## 🛠️ Prerequisites
To run these scripts, you need **Python 3** installed.
You must also install the following libraries:

> pip install matplotlib markdown pandas openpyxl
> 
🚀 How to Use
Step 1: Analyze the Logs

Run the main script to clean the raw data.

> python Analyse_Reseau.py
Input: Enter the filename (e.g., fichier1000.txt). Output: A Resultat_Reseau.csv file is created.

Step 2: Generate Evidence (Graphs)

Visualize the traffic to find the suspicious IP.

> python Graphe_Attaque.py
Output: Generates Preuve_1_IP_Attaquant.png (Top Talkers).

Step 3: Create the Report

Generate the final HTML report.

> python Rapport_Reseau.py
Input: Enter the suspicious IP found in Step 2. Output: Open Rapport_Incident_Reseau.html in your browser.

📂 Project Structure
File	Description
Analyse_Reseau.py	Main parsing script (Python to CSV).
Graphe_Attaque.py	Visualization script (Matplotlib).
Rapport_Reseau.py	Reporting tool (Markdown/HTML).
Conversion_Excel.py	Tool to convert CSV to Excel (.xlsx).
fichier1000.txt	Sample log file for testing.
⚠️ Troubleshooting
File not found: Ensure your .txt log file is in the same folder as the scripts.

Module errors: Run the pip install command listed in Prerequisites.

IUT de Roanne
