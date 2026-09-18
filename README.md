# 🐍 Python

A collection of small Python scripts and mini-projects documenting a learning journey through the language — from the basics all the way to more advanced topics like object-oriented programming, GUIs, databases, and a small bioinformatics package.

## 📂 Repository Contents

| File | Topic |
|---|---|
| `Functions.py` | Defining functions, parameters, and `return` values |
| `control flow.py` | `if / elif / else` statements through practical examples (age-based access, grade evaluation...) |
| `loops.py` | `while` and `for` loops, plus a number-guessing game example |
| `Errors.py` | Error handling: `raise`, and `try / except / else / finally` |
| `moduls.py` | Importing built-in modules (`random`, `sys`), and creating/using a custom module |
| `bulit in func.py` | Built-in Python functions like `any()`, `all()`, `bin()`, `id()`, `sum()` |
| `Handlining_fils.py` | File handling: opening, reading, writing, and different file modes (`r`, `w`, `a`, `r+`...) |
| `OOP.py` | Comparing the procedural paradigm vs. object-oriented programming (OOP) |
| `GUI.py` | Introduction to `Tkinter` for building GUIs (buttons, labels, entry, text, frames) |
| `PackagesUsing.py` | Using the `Pillow (PIL)` library to work with images (open, show, crop), plus docstrings |
| `PythonApplication_Database.py` | Working with an `SQLite` database (creating tables, inserting/updating data) |
| `PythonApplication_SKILLS_APP.py` | A console app using `sqlite3` to manage a user's "skills" (add, delete, update, view) |
| `Advanced_Lesson.py` / `EX_file.py` / `shehab.py` | Examples of importing functions from other files, and the difference between running a file directly vs. importing it |
| `bioinformatices.zip` | **BioPal** 🧬 — a small Python package for biological sequence analysis (DNA/RNA), including sequence generation, complement/reverse complement, nucleotide counting, transcription & translation, ORF detection, and sequence validation |
| `calculator.rar` | A compressed calculator project |

## 🎯 Purpose

This repository isn't a production library — it's a **personal learning log** covering:
- Python basics (variables, conditionals, loops, functions)
- Error and exception handling
- Files and modules
- Object-oriented vs. procedural programming
- GUI development with Tkinter
- Databases with SQLite
- Third-party libraries like Pillow
- A hands-on bioinformatics mini-project

## ⚙️ Requirements

- Python 3.x
- External libraries needed for a few scripts:
  ```bash
  pip install pillow
  ```
- `tkinter` and `sqlite3` ship with most default Python installations.

## ▶️ How to Run

Each file is self-contained and can be run on its own:
```bash
python "file_name.py"
```

> ⚠️ Note: some files (e.g. `PackagesUsing.py`) contain local Windows file paths that you'll need to update for your own machine.

## ✍️ Author

This repository was created by **Shehab Eldin Khalid**, a Biomedical Engineering student, as part of a personal Python learning journey.
