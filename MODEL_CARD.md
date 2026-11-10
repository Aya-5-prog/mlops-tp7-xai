# Model Card - fraude (version servie par l'alias production)

## Modele
Nom et version dans le registre MLflow : fraude, version 1 (alias production)
Famille et reglages : RandomForestClassifier, n_estimators=500, max_depth=16, random_state=42
Run d'origine (MLflow) : e3e0bf9d (experience tp2-registre, run rf-500-16, reconstruit via l'annexe A)

## Objectif et usage prevu
Detecter les transactions bancaires suspectes (montant, anciennete du client, frequence sur 24 h, paiement de nuit) pour les signaler a un conseiller.

## Usages exclus
Bloquer definitivement un compte ou refuser un paiement sans revue humaine. [Ajoute un second usage exclu et justifie-le par un resultat du TP, voir Question 10.]

## Donnees
Fichier : data/transactions.csv, 5 000 lignes, 568 fraudes ([calcule la part en %]), empreinte md5 : [valeur du tag donnees_md5]
Origine des donnees : synthetiques, generees par donnees.py (graine 7)

## Performances (jeu de test, 1 250 transactions)
F1 : 0.8669   precision : 0.8837   rappel : 0.8507   AUC : 0.9872

## Methodes d'explicabilite
Globale : importance par permutation (10 melanges, scoring F1) et SHAP TreeExplainer sur 400 transactions de test
Locale : SHAP (waterfall) et LIME (2 000 voisins, graine fixee a 0)
Variables les plus influentes : montant, puis freq_24h, anciennete et nuit [verifie avec tes tableaux]

## Comparaison avec un modele interpretable
Logistique avec log10(montant) : F1 0.8593 (113 fraudes sur 134) contre 0.8669 (114 sur 134) pour la foret ; ecart dans le bruit du test, lisible sans outil.

## Limites et risques connus
Donnees synthetiques ; seulement 134 fraudes dans le test ; LIME varie selon la graine ; SHAP decrit le modele, pas une causalite. [Ajoute une limite justifiee par un resultat, voir Question 10.]

## Recommandations d'utilisation et de surveillance
Revue humaine avant tout blocage ; surveiller la derive du montant et de la frequence ; relancer la comparaison avec le modele interpretable apres chaque reentrainement.

## Tracabilite
## Tracabilite
Run des explications (experience tp7-explicabilite) : xai-fraude-v1, run 06668142f500485ab6a19a9c473f5eda
Auteurs : Aya + Manal Date : 2026-11-10   Prochaine revue :  2027-02-10