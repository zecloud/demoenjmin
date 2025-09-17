# demoenjmin

Azure Functions Demo en Python

## Description

Ce projet contient une fonction Azure Functions en Python avec un trigger HTTP qui répond "plop" quand on fait un POST HTTP.

## Structure du projet

```
demoenjmin/
├── HttpTrigger/           # Fonction Azure HTTP trigger
│   ├── __init__.py        # Code de la fonction
│   └── function.json      # Configuration de la fonction
├── host.json              # Configuration de l'host Azure Functions
├── local.settings.json    # Configuration locale
├── requirements.txt       # Dépendances Python
└── README.md             # Ce fichier
```

## Installation

1. Installez les dépendances Python :
```bash
pip install -r requirements.txt
```

2. Installez Azure Functions Core Tools pour le développement local :
```bash
npm install -g azure-functions-core-tools@4 --unsafe-perm true
```

## Utilisation

### Développement local

1. Démarrez la fonction localement :
```bash
func start
```

2. Testez la fonction avec un POST HTTP :
```bash
curl -X POST http://localhost:7071/api/HttpTrigger
```

La fonction retournera "plop" avec un code de statut 200.

### Déploiement sur Azure

1. Créez une Function App sur Azure
2. Déployez avec Azure Functions Core Tools :
```bash
func azure functionapp publish <nom-de-votre-function-app>
```

## Fonctionnalité

La fonction `HttpTrigger` :
- Accepte uniquement les requêtes POST
- Retourne "plop" pour les requêtes POST valides
- Retourne une erreur 405 pour les autres méthodes HTTP

## Tests

Exécutez les tests unitaires :
```bash
python test_http_trigger.py
```