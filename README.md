# DictPathNavigator

A simple Python utility that reads a JSON-like file and retrieves a deeply nested value based on a key path string (e.g. `a/b/c`).  
This tool helps navigate nested dictionaries using a path-based approach.

---

## 🚀 Features

- Read JSON-like data from a file
- Access nested dictionary values using key path format
- **No external libraries used** – pure built-in Python only
- Lightweight and beginner-friendly

---

## ⚠️ Warning: About `eval()`

This script uses Python's built-in `eval()` to convert a string into a dictionary.  
> ⚠️ **Never use `eval()` with untrusted data.** It can execute arbitrary code and may be dangerous.  
For safe use in production, consider replacing it with `json.loads()` or `ast.literal_eval()`.

---

## 📂 File Format

The input file (`data-1.json`, `data-2.json`) must contain a valid Python dictionary format (not standard JSON).

```python
{'a': {'b': {'c': 'hello'}}}
