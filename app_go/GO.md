# Go web application

This is a simple web application that shows the current exchange rate of cryptocurrencies (BTC, ETH, DOGE and SOL) to USD.

## How it works

The current rate of cryptocurrencies allows program to get a [coin api](https://docs.coinapi.io/market-data/rest-api/exchange-rates) using a apikey. I chose this service because it is free and has good documentation. In serious projects, such things as keys, passwords or addresses for connecting to internal services are usually taken out to the secret repository, but I did not hide it, since this key is not important for me and anyone can get it after registering on the platform, as well as connecting a secret vault would unnecessarily complicate the project.

## Best practices & Coding standarts 

1. Naming. In the project i use a camel сase, which complies with the recommended standards for programming in the Go language. 

*NOTE: In Go access modification is done by naming, the lowercase functionality is only available within the package, while the capitalized functionality is available everywhere.*

2. Packages and project structure. The entire project is divided into packages, each of which describes a certain application logic. [Go project layout](https://github.com/golang-standards/project-layout)

3. Interfaces. Interfaces in Go are a powerful tool for avoiding high coupling. In the project, interfaces are used for the repository pattern. In case the api I have chosen is not suitable for further purposes, I can choose another way to get the exchange rate. To do this, it will be enough for me just to implement the `ExchangeRepo ` interface, the rest of the project logic will not need to be changed.

In addition, the code has comments, transparent logic and is easily scalable if new requirements are added.

However, there is a small drawback - this is the use of a method `Spinft` from the `fmt` package. This method is considered not the fastest for string concatenation, I can use the bytes package instead, but this will be over-optimization.