# Web App 

## Description 

The simple web application where show the weather on specific city. 
To choose city you should write name of the city on url, then the app will return temperature of this city.

## Development 

- Created http server that listen on port 3000. 
- Handling request by URL "/(city)" where write name of city 

## Library 
+ colly - to web scraping 
+ net/http - to build http server
+ html/templates - to show html pages
+ log - to logging all errors 

## Best practices 
+ Used module to store libs
+ meaningful variable names 
+ Avoid nesting by handling errors
+ DRY(don't repeat yourself)

## Testing 

1 Make sure that Golang installed

2 Clone the repository 

3 Init the module, to do write this command on terminal 
- `go mod init weather` - to initialize module
- `go mod tidy` - to get all need libs

4 Run the code: `go run weather.go`

5 Open the any browser and write this url `localhost:3000/"name_of_city"`

![](example.png)