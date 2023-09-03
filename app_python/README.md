# Moscow Time Fetcher

This application is a UNIX-way inspired service which fetch current time in Moscow.

## Getting started
1. Install Python 3.8 or higher
2. Install required dependencies
```bash
python -m pip install -r requirements.txt
```
3. Run the application
```bash
uvicorn main:app
```

## Troubleshooting
### I use Arch btw. How to install deps?
```bash
pacman -S uvicorn python-starlette
```
