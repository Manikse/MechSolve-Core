# ⚙️ MechSolve-Core
![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen.svg)

> **Stop punching calculator buttons. Start engineering.**

Tired of manually calculating support reactions and bending moments before every single Strength of Materials assignment or lab? **MechSolve-Core** is a lightning-fast CLI utility that does the heavy lifting for you in a fraction of a second.

## ✨ Features
* **Instant Calculation:** Get support reactions ($R_a$, $R_b$) instantly.
* **Max Bending Moment:** Automatically computes the maximum bending moment ($M_{max}$) under the point of load.
* **CLI-First:** No bloated GUI. Just pure, fast terminal execution.
* **Error Proof:** Eliminates human error in routine pre-calculations.

## 🚀 Quick Start

### Installation
Clone the repository and navigate to the directory:
```bash
git clone [https://github.com/yourusername/mechsolve-core.git](https://github.com/yourusername/mechsolve-core.git)
cd mechsolve-core
UsageRun the script directly from your terminal by passing the beam length (-l), force (-f), and distance to the force (-d).Bashpython beam_calc.py -l 5 -f 10 -d 2
📊 Expected OutputPlaintext========================================
🔥 MechSolve-Core: Calculation Results 🔥
========================================
Beam length: 5.0 m
Force: 10.0 kN applied at 2.0 m
----------------------------------------
Reaction at Support A (Ra): 6.00 kN
Reaction at Support B (Rb): 4.00 kN
Max Bending Moment (M_max): 12.00 kN*m
========================================
📐 Mathematical BackgroundThis script calculates the maximum moment using the fundamental statics formula for a simply supported beam with a single point load:$$M_{max} = \frac{F \cdot a \cdot b}{L}$$🤝 Support the ProjectIf this script saved your sleep before an engineering deadline, consider buying me a coffee!
---

### 💻 Проєкт 2: `NextForge-API` (README.md)

```markdown
# ⚡️ NextForge-API
![Next.js](https://img.shields.io/badge/Next.js-App_Router-black.svg)
![Python](https://img.shields.io/badge/Python-Automation-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

> **Zero-to-API in 0.1 seconds. Stop writing boilerplate CRUD.**

How much time do you waste manually creating nested `app/api/.../route.ts` folders and typing out the exact same GET and POST structures every time you start a new Next.js SaaS? **NextForge-API** builds your entire App Router API structure from a simple JSON schema.

## 🔥 Why NextForge?
* **App Router Native:** Fully compatible with the latest Next.js App Router (`route.ts`).
* **Schema-Driven:** Define your database models once in a simple JSON file.
* **Instant Scaffolding:** Generates directories and files automatically.
* **TypeScript Ready:** Outputs clean, typed Next.js API endpoints.

## 🚀 How It Works

### 1. Define Your Schema
Create a `schema.json` file in the root directory:
```json
{
  "models": ["User", "Product", "Order", "Subscription"]
}