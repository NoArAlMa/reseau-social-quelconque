# Projet Final NSI - Réseau Social "Twitter-like"

🚀 **Un réseau social minimaliste développé avec Nuxt 4, FastAPI et PostgreSQL** – par Les loups de la NSI Ahouuuuu.

---

## 📌 À quoi ça sert ?

Notre objectif : **créer une alternative open-source à Twitter**, avec :

- Authentification .
- Feed de posts en temps réel.
- Profils utilisateurs personnalisables.
- **Bonus** : Packaging desktop avec Tauri .

---

## 🛠 Stack Technique

| Partie       | Technologies                          |
| ------------ | ------------------------------------- |
| **Frontend** | Nuxt 4, TailwindCSS 4, Nuxt UI, Pinia |
| **Backend**  | FastAPI, PostgreSQL, SQLModel         |
| **Desktop**  | Tauri (Rust)                          |
| **Outils**   | GitHub Actions,                       |

---

| Partie                 | Nom                             |
| ---------------------- | ------------------------------- |
| **Leader du parti**    | Alexandre LARUE                 |
| **Frontend suppléant** | Noham Mocquard                  |
| **Backend**            | Arthur Michel et Maxime leFraix |

## 💻 Setup & Lancement

### Prérequis

- Node.js (v20+), Python (3.10+),pnpm.
- Un cerveau, oui parce que de ce que je vois, certaines personnes n'en ont pas ici !

---

## 📂 Architecture des dossiers

Suivez bien ça risque d'être dur pour vous

```bash
📦 projet-final-nsi
├── 📂 frontend/              # Nuxt 4
│   ├── 📂 components/        # Composants Vue
│   │   └── 📂 ui/            # Composants réutilisables (boutons, inputs, etc.)
│   ├── 📂 pages/             # Pages principales (index.vue, login.vue)
│   ├── 📂 stores/            # Stores Pinia (auth.ts, posts.ts)
│   ├── 📄 app.vue            # Layout principal
│   ├── 📄 nuxt.config.ts     # Configuration Nuxt
│   └── 📄 tailwind.config.js # Configuration TailwindCSS
│
├── 📂 backend/               # FastAPI
│   ├── 📂 api/               # Endpoints API
│   │   ├── 📄 auth.py        # Routes d'authentification
│   │   ├── 📄 posts.py       # Routes pour les posts
│   │   └── 📄 users.py       # Routes pour les utilisateurs
│   ├── 📂 models/            # Modèles SQLModel
│   │   ├── 📄 user.py        # Modèle utilisateur
│   │   └── 📄 post.py        # Modèle post
│   ├── 📂 schemas/           # Schémas Pydantic
│   ├── 📂 core/              # Configuration de base
│   │   ├── 📄 config.py      # Configuration de l'application
│   │   └── 📄 security.py    # Gestion de la sécurité (JWT, etc.)
│   ├── 📄 main.py            # Point d'entrée FastAPI
│   └── 📄 requirements.txt   # Dépendances Python
│
├── 📂 desktop/               # Tauri (Rust)
│   ├── 📂 src-tauri/         # Code source Rust
│   └── 📄 tauri.conf.json    # Configuration Tauri
│
│
├── 📂 docs/                  # Documentation
│   ├── 📄 CONTRIBUTING.md        # Guide de contribution
│
├── 📄 .gitignore             # Fichiers ignorés par Git
├── 📄 README.md              # Ce fichier

```
