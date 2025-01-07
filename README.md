# 🚀 Projet PING² 

Bienvenue sur le dépôt GitHub du projet **PING²**. Ce projet est un jeu de plateau interactif avec des surfaces de rebond robotisées, conçu pour aider à la rééducation et à la stimulation de la motricité, notamment pour les personnes à mobilité réduite.

## Description du projet

PING² est un système modulaire composé de deux sous-systèmes principaux :

1. **ESP32** – Dirige la plateforme mécanique, incluant les moteurs, capteurs et solénoïdes.
2. **Raspberry Pi** – Gère le déroulement de l'activité, les interfaces, la reconnaissance de la balle et la gestion des joueurs.

L'architecture est pensée pour évoluer facilement, avec un matériel modulaire permettant de nombreuses options de connexion. En plus de l'esp32 et de la raspberry, d'autres composants ont besoin d'être codé, comme les arduino Nano qui gèrent les manettes et l'interface de paramètrage.


## 📚 Description de la Branche

La branche principale contient les versions stables et testées des différents codes à flasher sur les composants du projet. Assurez-vous de mettre à jour régulièrement pour profiter de la meilleure expérience de jeu.

## 🔄 Workflow de Développement
- Développement Fonctionnel : Chaque branche ```hardware/*``` est dédiée au développement et à l'amélioration du code pour un matériel spécifique.
- Intégration dans dev : Les branches ```hardware/*``` sont ajoutées en tant que sous-modules à la branche dev. **Aucune modification du code source ne doit être effectué depuis la branche ```dev```.**
- Phase de Test : Les codes sont testés ensemble pour s'assurer qu'ils fonctionnent de manière cohérente sur l'ensemble du système.
- Validation : Une fois les tests concluants, la branche dev est fusionnée (merge) dans la branche main, qui représente alors la version stable et prête pour la production du projet.

  ## 📄 Instructions pour les Contributeurs
Les informations relatives aux contributions sont disponibles dans la branche [dev](https://github.com/2PING2/PING2/tree/dev)

### 📬 Contact
Pour toute question ou clarification, n'hésitez pas à contacter l'équipe de développement ou à ouvrir une Issue sur le dépôt GitHub.

## Licence

Ping² © 2024 by Antoine, Antoine, Robin, Simon, Thomas is licensed under [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International](https://creativecommons.org/licenses/by-nc-nd/4.0/)
