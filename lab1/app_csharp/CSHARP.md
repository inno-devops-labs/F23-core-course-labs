# Lab 1 - C# solution

## Researched best practices
After some time of research, I see several options here:
1. Use standard C# `System.Net` library
pros: easy to use, C# built-in package
cons: doesn't support asynchronous requests, which can help when we have too large amounts of requests

2. Use `ASP .NET Core`(https://github.com/aio-libs/aiohttp)
pros: easy to use, supports asynchronous requests, supports Blazor Pages which helps with HTML
cons: too complex for our problem

I decided to use `ASP .NET Core` because in the future, when developing our application, we will have much less problems with this

## Linters for Python and Markdown
For C# I use default JetBrains Rider linter, for Markdown VScode extension `Markdown All in One`