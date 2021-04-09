Challenge: Substitution

Description: We're given a source code with an encrypting algorithm which is running on a server. Upon connection to the server we can type a number as input and the server responds with an encryption of it.

Example of server output:
```
Enter a number and it will be returned with our super secret synthetic substitution technique
> 0
>> 125
> 1
>> 492
> 2
>> 670
> 3
>> 39
```

Solution:
We can see how the encryption behaves by looking closely at the source code and this part of it in particular:

```python
with open("flag", "r") as f:
    key = [ord(x) for x in f.read().strip()]

def substitute(value):
    return (reduce(lambda x, y: x*value+y, key))%691
```

We see it takes a flag file, reads it and converts characters to numbers.
Then it takes an input from a user and passes it to a "substitute" function, the flag being the key to the encryption.
Turns out this function does nothing more than this polynomial equation:

f(x) = a<sub>n</sub>x<sup>n-1</sup> + a<sub>n-1</sub>x<sup>n-2</sup> + ... + a<sub>2</sub>x + a<sub>1</sub> mod 691

where x is the value of an input we give  and a's are characters of the flag encoded as numbers.
So, if we knew the flag is four characters long, we could create four equations of this kind by making the algorithm encrypt for example 0,1,2,3. We'd have four unknowns and four linear equations moodulo 691 so we can solve for these unknowns. The only problem now is that we don't know the length of the flag, so we have to try many possible lengths, solve the equations for each, convert the a's back to characters and see if the results contain anything sensible.

The sol.py script does that and we find our flag:
```
actf{polynomials_20a829322766642530cf69}
```
