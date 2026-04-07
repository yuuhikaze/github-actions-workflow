# Github Actions Workflow

## Tests

Run tests with:

```bash
python -m pytest # assumes you have pytest available on your system
```

## Usage

Test addition:

```bash
curl -X POST https://sd-api.yhkze.net/add \
  -H "Content-Type: application/json" \
  -d '{"a": 5, "b": 3}'
```

> Expected response: {"result":8,"operation":"add"}

Test subtraction:

```bash
curl -X POST https://sd-api.yhkze.net/subtract \
  -H "Content-Type: application/json" \
  -d '{"a": 10, "b": 4}'
```

> Expected response: {"result":6,"operation":"subtract"}

Test multiplication:

```bash
curl -X POST https://sd-api.yhkze.net/multiply \
  -H "Content-Type: application/json" \
  -d '{"a": 6, "b": 7}'
```

> Expected response: {"result":42,"operation":"multiply"}
