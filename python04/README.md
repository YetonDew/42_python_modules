# 🛰️ Python Module 04 — Cyber Archives

This module practices Python file handling and stream management through a cyber-archive theme.

## Contents

- `ex0/ft_ancient_text.py` — Read an existing archive file with safe error handling.
- `ex1/ft_archive_creation.py` — Create and write a new archive file.
- `ex2/ft_stream_management.py` — Use `stdin`, `stdout`, and `stderr` channels correctly.
- `ex3/ft_vault_security.py` — Read protected data and write updated security protocols.
- `ex4/ft_crisis_response.py` — Handle multiple file-access crisis scenarios with exceptions.

## Project Files

- `sample_data.json` — Sample data file for archive practice.
- `data_generator.py` — Optional helper to generate data files.

## How to Run

From the repository root:

```bash
python3 python04/ex0/ft_ancient_text.py
python3 python04/ex1/ft_archive_creation.py
python3 python04/ex2/ft_stream_management.py
python3 python04/ex3/ft_vault_security.py
python3 python04/ex4/ft_crisis_response.py
```

Or from inside `python04/`:

```bash
python3 ex0/ft_ancient_text.py
python3 ex1/ft_archive_creation.py
python3 ex2/ft_stream_management.py
python3 ex3/ft_vault_security.py
python3 ex4/ft_crisis_response.py
```

## Notes

- Some exercises rely on files existing in the same exercise folder.
- For `ex4`, behavior depends on available files and current file permissions.
- If a file is missing, the script should trigger and handle the corresponding exception.
