# Moscow Time
- Simple app that shows the current time in MSK Timezone.

## Used technology
- HTML, CSS, JS.
- Python (packages: Flask, Gunicorn).

## Endpoints
```bash
$ flask routes
Endpoint            Methods  Rule
------------------  -------  -----------------------
home                GET      /
static              GET      /static/<path:filename>
```

## Development

`python` and `pip` are used, make sure you have them installed and available in `$PATH` then execute the following:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python app.py

# or
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

## Testing

```bash
python -m pytest
```
