NETWORK ANALYSIS TOOL - USER GUIDE
Version: 1.0
Author: Student Developer
Target Audience: Network Administration Team (India Site)
1. OVERVIEW
This toolkit allows you to analyze raw tcpdump logs to identify the source of network saturation. It automates data extraction, visualization, and reporting.
2. PREREQUISITES
Before running the tools, ensure you have Python 3 installed on your machine. You must install the following libraries:
Bash
pip install matplotlib markdown
3. INSTALLATION
1. Create a folder named Network_Analysis.
2. Place the following files inside:
○ Analyse_Reseau.py (Script 1)
○ Graphe_Attaque.py (Script 2)
○ Rapport_Reseau.py (Script 3)
○ Your log file (e.g., capture.txt)
4. HOW TO USE (Step-by-Step)
STEP 1: Data Extraction
● Goal: Convert the raw text file into a readable CSV format.
Action: Open a terminal and run: Bash python Analyse_Reseau.py
●
● Input: Enter the name of your log file when prompted (e.g., server_logs.txt).
● Output: The script generates Resultat_Reseau.csv.
○ Note: You can open this CSV file with Excel for manual verification.
STEP 2: Visualization
● Goal: Generate graphs to identify the attacker.
Action: Run the second script: Bash python Graphe_Attaque.py
●
● Output: Two images are created:
○ Preuve_1_IP_Attaquant.png (Top Talkers)
○ Preuve_2_Type_Attaque.png (Flag Distribution)
STEP 3: Reporting
● Goal: Generate a final HTML report for management.
Action: Run the final script: Bash python Rapport_Reseau.py
●
● Input: Enter the suspicious IP address found in Step 2.
● Output: Open Rapport_Incident_Reseau.html in your web browser to view the full incident report.
5. TROUBLESHOOTING
● Error: "File not found": Ensure your .txt file is in the same folder as the python scripts.
● Error: "Module not found": Run the pip install command listed in Section 2
