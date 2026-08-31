# Microsoft Fabric CI/CD Deployment Pipeline

Automated CI/CD workflow for deploying **Microsoft Fabric** artifacts across pipeline stages (**Development -> Test -> Production**) using **GitHub Actions** and the **Microsoft Fabric REST API**.

---

## 🎯 Deployment Strategy

* **Dev → Test (Automated):** Triggers automatically on every `push` to the `main` branch.
* **Test → Production (Manual):** Code in the Test stage must be verified before manually promoting to Production via the Fabric UI or a dedicated release trigger.

---

## 📌 Pipeline Identifiers

* **Pipeline Name:** `DP700_Enterprise_Pipeline`
* **Pipeline ID:** `86d8facc-25b0-4e36-bbc4-9d9965c01d66`

| Stage | Stage ID | Deployment Type |
| :--- | :--- | :--- |
| **Development** | `6fadcfc5-fc55-4adf-988c-08c73e0dc9cc` | Source Stage |
| **Test** | `e726e4a1-690d-4d6a-a795-9c3027ba729b` | **Automated** (via GitHub Push) |
| **Production** | `aace5bbc-19fe-475b-bb74-6d4307d8c4b0` | **Manual** (Post-Validation) |

---

## 📁 Repository Structure

```text
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions workflow (Dev to Test)
├── get_stages.py              # Python utility to fetch Fabric pipeline stage IDs
└── README.md                  # Documentation
