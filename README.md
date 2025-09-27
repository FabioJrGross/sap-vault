# SAP Vault – Local Secure SSO for Multiple SAP Connections

**Educational project for learning Python** and providing a more secure way for SAP professionals to manage multiple system connections.

## Problem
SAP support professionals often work with dozens of different client systems.  
In some cases:
- Companies do not provide SSFS (Secure Storage in the File System).
- Security policies prohibit password reuse.
- Users end up storing credentials in plain-text `.txt` files — which completely undermines security policies.

## Solution
This application aims to:
- Create a locally stored **encrypted vault** on the user’s PC.
- Protect it with a **master password**.
- Allow quick connection to any SAP system without exposing stored passwords.

⚠️ **Disclaimer**  
- SAP already provides the official solution: **SSFS (Secure Storage in the File System)**.  
- This project is **not a replacement** for SSFS.  
- Security is limited: the goal is to be **safer than plain text**, not to reach enterprise-level standards.

## Objectives
1. Learn Python by building a real-world inspired tool.  
2. Help SAP professionals simplify the management of multiple connections.  

## Status
Currently under development.
