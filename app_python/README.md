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

## Docker
This full application has been uploaded to [dockerhub](https://hub.docker.com/r/iviosab/moscow_time), you can fully test it by either pulling the image from dockerhub or building the Dockerfile in this directory and then running it. 
#### Build 
```bash
# make sure you are in the app_python directory
docker build -t <name> .
```
#### Pull
```bash
docker pull iviosab/moscow_time
```
#### Run
```bash
docker run --rm -p 5000:5000 iviosab/moscow_time
```