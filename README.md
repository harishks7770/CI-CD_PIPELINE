# Fabric CI/CD Selective Deployment Pipeline

This repository manages the version control and multi-stage CI/CD deployment pipeline for Microsoft Fabric data artifacts (Notebooks, Pipelines, and Dataflows). 

It implements a **selective deployment pattern**, ensuring only modified or targeted items are validated and deployed across environment workspaces (`dev` $\rightarrow$ `test` $\rightarrow$ `prod`).

---

## 🏗️ Deployment Architecture

```text
               ┌───────────────────────┐
               │    Git Repository     │
               │ (main / feature dev)  │
               └───────────┬───────────┘
                           │
             (Selective CI/CD Trigger)
                           │
       ┌───────────────────┼───────────────────┐
       ▼                   ▼                   ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ DEV Stage   │ ──> │ TEST Stage  │ ──> │ PROD Stage  │
│ Workspace   │     │ Workspace   │     │ Workspace   │
└─────────────┘     └─────────────┘     └─────────────┘


## 🛠️ Tech Stack

* **CI/CD & Source:** Git ➔ GitHub Actions / Azure Pipelines
* **Automation:** Python 3.11 (Selective Diff Scripting) ➔ Fabric REST API
* **Environments:** Microsoft Fabric Workspaces (`DEV` ➔ `TEST` ➔ `PROD`)
