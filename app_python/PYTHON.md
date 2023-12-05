## Web application 

I choose the flask framework cause it's best choice to do simple web app. 
Flask is suitable for small projects and easily scalable for the applications


## Best practices:
+ Minimalism
+ Readable codes
+ Created file requirements where store list of necessary libraries 
+ Created virtual environment

## Coding Standards
+ PEP8 coding standards followed. To be ensure you can check with `flake8`  

## Testing 
+ `app_test.py` file cover this tests: 
  + Make sure that web app return correct time 
  + Checking that refreshing page after two seconds will change the response

+ Best practices:
  + Tested one thing in each test 
  + Tests easy to read and maintain 
  + Avoided setup and teardown code 
  + Used `fixture` from pytest for complex set up
  + Cover both positive and negative tests 
