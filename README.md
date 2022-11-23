# Sample REST API with Python Flask

## Getting Started

1. Clone this repository and install dependencies

```
> git clone https://github.com/a-ndrewh27/pokemon-attrs.git .
> python3 -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt
```

2. Start server via command `python wsgi.py`

## GET Routes

| resource                | description                                                                 |
| :---------------------- | :-------------------------------------------------------------------------- |
| `/api/pokemon/top-five` | returns JSON object with `top_five` pokemon and `team_base_happiness` stats |

3. Sample API is running on `localhost:5000`

## Tests

Run tests via command

```
pytest
```
