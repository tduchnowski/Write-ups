Challenge: I'm So Random

Description: We're given a source code for some sort of number generator
(chall.py). The server prompts us to make a decision about whether we wish to
generate a new number or guess the next one.

Example:
```
Would you like to get a random output [r], or guess the next random number [g]?r
6286247646136908
Would you like to get a random output [r], or guess the next random number [g]?g
What is your guess to the next value generated?11
Incorrect!
```
We have only three chances to read a number before guessing.

Solution:
The number generator first generates two 8-digit numbers and each time user
makes a decision it uses this method:
```python
def getNum(self):
    self.seed = int(str(self.seed**2).rjust(self.DIGITS*2, "0")[self.DIGITS//2:self.DIGITS + self.DIGITS//2])
    return self.seed
```
to generate a new 8-digit number. What's worth noting is that this generation is
not random and if you know the current number you will know the next one.
After this, it multiplies the two numbers and outputs them to the client.

Our goal is to make a correct guess and to do that we have to find the two
currently generated numbers. We can factorize the product given to us and try to
deduce something from it. If it turns out for example that the product is
actually made up by two prime numbers, we can identify the seeds easily as those two primes. That'd be an ideal
case.
Using sympy library we can factorize each given number.
If the number is something like this:
```
2558734384060680 = 2*2*2*3*5*7*4695653*648709
```
then it's bad. We can't deduce which combination of primes and their exponents
gives us our two numbers. However, this:
```
4081259704173037 = 37*523*3631*58085077
```
is good. There is one 8-digit number which can't be combined with any
other prime in this factorization, because other primes are bigger than 10 and
hence the resulting number would be 9 or more digits so it can't possibly be our
original number. Therefore, this 8-digit prime in the factorization above is our original number and the second one is made of the
rest of those primes and their exponents.

With this knowledge I created a script which makes connections and simply waits
for the right number. After making a correct guess, server gives the flag:
```
actf{middle_square_method_more_like_middle_fail_method}
```
