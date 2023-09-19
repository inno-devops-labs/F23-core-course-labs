# Framework Choice

In order to create a web application that will provide a functionality to users to see current Moscow time,
we have to understand what technologies fit out task best of all. In this section I will discuss why using Flask
framework is the best option for my use-case.

## Options

There exist various different frameworks that provide unique functionality for developers to create web applications.
I considered the following options:
- Flask
- Django

Our objectives are the following:
* Easy and fast development
* Unit testing
* Scalable in future prospective

### Flask
Flask is a Python web framework which allows building web application. It very easy to use. Flask is also fast and scalable.

#### Pros
* Flask is flexible and comfortable
* It allows unit testing
* Flask is very simple to use which is very useful for beginners and small projects
#### Cons
* Flask uses modules what can result in security leaks


### Django
A Python web framework Django enables the quick creation of safe and dependable websites. Django handles a lot of the hassle associated with web development, allowing you to concentrate on developing your app without having to invent the wheel.

#### Pros
* The Django code structure is simple and efficient
* Django is a REST framework (Django Rest Framework or DRF) - allows to create Web APIs
* As Django has modular and customizable architecture the development process becomes easy
* Django is secure and reliable framework
#### Cons
* Django can have low performance because of how is internally processes modules 
* Django supports only primitive Models

## Conclusion

Considering all pros and cons of both approaches I decided to stick with Flask option. It allows to build projects at a high speed
because of its simplicity. It is also scalable and supports Unit testing what can be handy to verify that the software is working.

# Best Practices

In this section I will describe what best practices I used during the project development.

## Coding Standards

* Comments: I left some general comments for my code to make it readable and understandable to others
* Code: PEP 8 style format was used to ensure its readability and quality
* Variables: I also named variables in a readable way

## Testing

Having unit tests is a necessary and very important process that allows us to make sure that all components are consistent and work.
I created the following tests for my application:
- `test_get_response`: tests that server responds with 200 code
- `test_return_time_format`: tests returned message's time format
- `test_time_changed`: tests whether time was changed after the page refresh


## Conclusion

Following best practices of code writing and project development can allow us to develop products with a high quality that
will serve us and our users in a long term.