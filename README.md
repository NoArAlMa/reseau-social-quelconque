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

├── frontend/ # Application Nuxt V4
│ ├── components/ # Composants Vue (ex: PostCard.vue, Navbar.vue)
│ │ ├── ui/ # Composants réutilisables (boutons, inputs)
│ ├── pages/ # Pages principales (ex: index.vue, login.vue)
│ ├── stores/ # Stores Pinia (ex: auth.ts, posts.ts)
│ └── nuxt.config.ts # Configuration Nuxt
│
├── backend/ # API FastAPI
│ ├── api/ # Endpoints (ex: auth.py, posts.py)
│ ├── models/ # Modèles SQLModel (ex: user.py, post.py)
│ ├── schemas/ # Schémas Pydantic
│ ├── core/ # Configuration (DB, sécurité)
│ └── main.py # Point d'entrée FastAPI
│
├── Taurii/ # Notre build pour l'app de bureau
│
├── docs/ # Documentation
│ ├── CONTRIBUTING.md # C'est le prochain que vous allez lire
│
└── README.md # Ce fichier !
