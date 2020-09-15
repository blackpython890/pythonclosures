# Session : 8

## Objective

- Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable - 200
- Write a closure that gives you the next Fibonacci number - 100
- We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a  global dictionary variable with the counts - 250
- Modify above such that now we can pass in different dictionary variables to update different dictionaries - 250

&nbsp;

     check_fn_docs, __doc__, next_fibo_number, mul, add, div, function_counter

&nbsp;
- Write a test file, that tests all of the functions mentioned above and also includes the other basic ones. 
- Test file must contain at least 1 tests for each function.


---
&nbsp;

## Files
 - Test File : [PyTest file](https://github.com/jagatabhay/pythonclosures/blob/master/test_session8.py)
 - Code: [Method Implemantation](https://github.com/jagatabhay/pythonclosures/blob/master/session8.py)

---

&nbsp;

## Functions
| Serial No  | Name | Functionality |
| ---------- | --------- | ------ |
| 1 | check_fn_docs | The function takes in function as parameters and returns True/False based on length of docstring is greater than 50 characters or not|  
| 2 | next_fibo_number | This function returns the next number from fibnocci series |
| 3 | function_counter |The function takes in function as parameters and returns the global dictionary which gives the frequency of each function |
| 4 | counter2 | The function takes in function as parameters and returns the separate dictionary which gives the frequency of each function for different user |


## Test Cases Results
| Serial No  | Test Case | Result |
| ---------- | --------- | ------ |
| 1 | README File Exists | Pass |
| 2 | RREADME Words Counts | Pass |
| 3 | README proper description | Pass |
| 4 | RREADME Formatting | Pass |
| 5 | Function name not defined with capital letters | Pass |
| 6 | fourspace | Pass |
| 7 | test docstring length | Pass |
| 8 |  test fibonacci | Pass |
| 9 | check count functional called | Pass |
| 10 | test_function_called user wise | Pass | 

---

## Contributors:
- Email : jagatabhay@gmail.com
