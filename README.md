# password_strength_analyzer_with_wordlist_generator

# Password Strength Analyzer with Custom Wordlist Generator

## Overview
This project is a Python-based tool that analyzes password strength and generates custom wordlists based on user-provided information. It is designed to demonstrate common password weaknesses and how attackers build targeted wordlists, from a defensive security perspective.

## Objectives
- Analyze password strength
- Understand common password patterns
- Generate customized wordlists for security testing
- Learn basic password attack and defense concepts

## Tools Used
- Python  
- zxcvbn  
- Command Line Interface (CLI)

## Features
- Password strength scoring (0–4)
- Estimated password crack time
- Custom wordlist generation using:
  - Names, pet names, and years
  - Leetspeak substitutions
  - Case variations
  - Common suffixes
- Wordlist export in `.txt` format

## How It Works
1. The user enters a password to analyze.
2. The tool evaluates the password using the zxcvbn library.
3. The user provides personal details such as name, pet name, and year.
4. The tool generates password variations based on common patterns.
5. The generated wordlist is saved as a text file.

## How to Run
```bash
pip install zxcvbn
python password_tool.py

