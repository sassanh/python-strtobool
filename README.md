# 🐍 Python `strtobool`

Convert string to boolean value using `str_to_bool` function.

## 🛠 Usage

```python
from strtobool import str_to_bool

# Convert string to boolean value
value = str_to_bool('true')
```

## 📝 Supported values

All values are case-insensitive. Any value not listed below will raise a `ValueError`.

### True values

- `true`
- `t`
- `yes`
- `y`
- `on`
- `1`

### False values

- `false`
- `f`
- `no`
- `n`
- `off`
- `0`

## 📦 Installation

### Pip

```bash
pip install python-strtobool
```

### Poetry

```bash
poetry add python-strtobool
```

## 📜 License

This project is released under the Apache-2.0 License. See the [LICENSE](./LICENSE)
file for more details.
