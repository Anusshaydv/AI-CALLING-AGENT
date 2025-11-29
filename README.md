# AI-CALLING-AGENT
# Hookfish AI Calling Agent — Internship Assignment

A lightweight AI Calling Agent prototype built as part of the Hookfish internship assignment.  
This project demonstrates the core logic behind an automated first-level calling workflow for real-estate leads using simple intent detection, dialogue management, and a console-based simulation.

The objective of this prototype is **not** to build real telephony or real AI models, but to show clear thinking, clean architecture, and a working demonstration aligned with the assignment requirements.

---

## Features Implemented

### Console-based calling simulation  
Simulates an AI agent calling a customer and conducting a short conversation.

### Intent detection  
Classifies customer responses into:
- **INTERESTED**
- **BUSY**
- **NOT INTERESTED**
- **UNKNOWN**

###  Dialogue management  
Routes users into appropriate flows:
- Collect location & budget for interested customers  
- Record follow-up time for busy customers  
- Close the call politely for rejects  

### Final call summary  
At the end of each run, the system prints:
- Final outcome  
- Follow-up time (if any)  
- All collected notes  

---

## 🔧 How to Install / Clone the Repository

You can download or clone this repository using the following command:

```bash
git clone https://github.com/<your-username>/AI-Calling-Agent.git

