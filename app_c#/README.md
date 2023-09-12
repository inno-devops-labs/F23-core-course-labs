# Pet App

## Description
Wep application collects information about the dog, makes calculations based on the data and displays the information received about it.

## Start
### Pre-install
- `.NET core 6.0`
- `Docker`

### Run from terminal
1) Build project - `dotnet build -c Release`
2) Run - `dotnet *path to .dll file*`

### Run using Docker
1) Build: 
    `docker build -t pet-app .`
2) Push: 
    `docker tag pet-app annadluzhinskaya/pet-app:latest`
    `docker push annadluzhinskaya/pet-app:latest`
3) Pull: 
    `docker pull annadluzhinskaya/pet-app:latest`
4) Run:
    `docker run -p 8000:80 annadluzhinskaya/pet-app:latest`

## Project structure

```text
app_c#/
|____PetApp
| |____Converters
| | |____AgeConverter.cs
| |____Models
| | |____ErrorViewModel.cs
| | |____Dog.cs
| |____Properties
| | |____launchSettings.json
| |____Controllers
| | |____DogController.cs
| |____Views
| | |____Dog
| | | |____Profile.cshtml
| | | |____Index.cshtml
| |____Program.cs
|____DOCKER.md
|____Dockerfile
|____README.md
|____PetApp.sln
|____C#.md
```
