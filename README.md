# Specification

- I work for a company that makes academic maths papers easier to read

- The product scans through maths papers looking for sums

- It extracts those sums as strings

- The extracted sum strings are then evaluated and the evaluated result is outputted along with the extracted sum string

- Would like you to build us a prototype that evaluates sum strings that contain either one or two terms

-------------

Terms would be what is separated by the operators

## Inputs

Should be a string, operators separated by spaces (can throw a math error if not separated by spaces)

If an empty string

If given any other text as input, output a math error saying 'Input should be a valid mathematical sum separated by spaces'

Any other data type could result in an argument error 

## Outputs

An array containing the inputted string, and a Number, the evaluation of the sum (default 1dp, max 2dp)

## Test Cases

`"1"` => `["1", 1.0]`

`"1 + 1"` => `["1 + 1", 2.0]`

`""` => `["", 0.0]`

## Algorithm 

- Create an array, `output`, adding the given input string as first el
- Split input string into an array by whitespace, assign to a variable `input_array`
- If length of `input_array` is 1
  - Convert the first element to a Number to 1dp
  - append the first element to `output` and return it
- Else if leength of `input_array` is 3
  - Check which operator is being used in the 2nd el of `input_array` -> * / + =
  - Calculate the result by converting 1st and 3rd el to Numbers and using the operator provided


### Additional error handling for further iterations:

- Check for empty strings
- Check for invalid args  
  

### Getting Started

`git clone https://github.com/tomcarmichael/makers-string-calculator-tech-test.git`

`source venv/bin/activate`

`pytest`
