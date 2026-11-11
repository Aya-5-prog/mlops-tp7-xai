# Model Card - fraude (version servie par l'alias production)

## Modele
Nom et version dans le registre MLflow : fraude, version 1 (alias production)
Famille et reglages : RandomForestClassifier, n_estimators=500, max_depth=16, random_state=42
Run d'origine (MLflow) : e3e0bf9d (experience tp2-registre, run rf-500-16, modele recree via l'annexe A du TP07)

## Objectif et usage prevu
Detecter les transactions bancaires suspectes a partir de quatre variables (montant, anciennete du client, nombre de transactions sur 24 h, paiement de nuit) et les signaler a un conseiller pour verification.

## Usages exclus
Bloquer definitivement un compte ou refuser un paiement sans revue humaine : le modele laisse passer 20 fraudes et signale a tort 15 clients legitimes sur 1 250 transactions de test.
Utilisation sur des donnees reelles sans nouvelle validation : le modele a ete entraine et evalue sur des donnees synthetiques.

## Donnees
Fichier : data/transactions.csv, 5 000 lignes, 568 fraudes (11,4 %), empreinte md5 (tag donnees_md5) : VALEUR_MD5
Origine des donnees : synthetiques, generees par donnees.py (graine 7)

## Performances (jeu de test, 1 250 transactions)
F1 : 0.8669   precision : 0.8837   rappel : 0.8507   AUC : 0.9872
Matrice de confusion : [[1101, 15], [20, 114]] (114 fraudes detectees sur 134)

## Methodes d'explicabilite
Globale : importance par permutation (10 melanges, scoring F1) et SHAP TreeExplainer sur 400 transactions de test.
Locale : SHAP (waterfall) et LIME (2 000 voisins, graine fixee a 0) sur la transaction de Mme Benali et sur la transaction de test la plus suspecte (index 668).
Variables les plus influentes : montant, puis freq_24h, anciennete et nuit (permutation : 0,593 / 0,269 / 0,268 / 0,196). SHAP global : montant 0,1157, anciennete 0,0576, nuit 0,0571, freq_24h 0,0556.

## Comparaison avec un modele interpretable
Logistique avec log10(montant) : F1 0.8593 (113 fraudes sur 134) contre 0.8669 (114 sur 134) pour la foret. L'ecart est dans le bruit du test et la logistique se lit sans outil. Avec le montant brut, la logistique tombe a F1 0.7407 (90 sur 134). Arbre de profondeur 3 : F1 0.5737 (72 sur 134).

## Limites et risques connus
Donnees synthetiques : les performances ne sont pas garanties sur des transactions reelles.
Seulement 134 fraudes dans le test : l'ecart entre la foret (114 detectees) et la logistique log10 (113) est de 1 fraude, soit du bruit.
LIME varie selon la graine et SHAP decrit le modele, pas une causalite.
Erreurs residuelles : 20 fraudes non detectees et 15 clients legitimes signales a tort.

## Recommandations d'utilisation et de surveillance
Revue humaine avant tout blocage ; surveiller la derive du montant et de la frequence ; relancer la comparaison avec le modele interpretable apres chaque reentrainement ; refaire les explications a chaque changement de version derriere l'alias production.

## Tracabilite
Run des explications (experience tp7-explicabilite) : xai-fraude-v1, run 06668142f500485ab6a19a9c473f5eda
Auteurs : Aya + Manal   Date : 2026-11-10   Prochaine revue : 2027-02-10