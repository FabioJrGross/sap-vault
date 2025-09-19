# Local Secure SSO for Multiple SAP Connections (Learning Project)

This simple project has two objectives:

  1. Help me learn Python.

  3. Help professionals who work with SAP organize and simplify their numerous connections to various SAP systems.

The Problem: Especially for professionals working in support of SAP systems, it is common to have dozens of different connections to various client systems. Some companies lack an available SSFS and have complex security policies that prohibit password reuse across systems. In these cases, users often resort to storing their credentials in a plain-text .txt file on their computer, which completely negates all security policies.

What this app does (hopefully when finished): This application will create a locally stored, encrypted file on the user's PC. It will use a master password to secure a list of all SAP connections, allowing the user to connect to any system with a single click without revealing the passwords.


# ACKNOWLEDGMENTS

- SAP already provides SSFS, which is the standard and correct solution for this problem.

- This app may not be extremely secure, but its objective is to be a more secure alternative to storing passwords in plain text, not to provide Fort Knox-level security.

