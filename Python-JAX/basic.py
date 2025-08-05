#!/usr/bin/python3
"""welcome to jax

j= just in time compilation, where the function is compiled directly into
byte code, which makes it run faster
a= automatic differentiation, makes it easier to get the differentiation calculations of functions(calculus)
x= (xla)accelerated linear algebra, permits us to run it on gpu"""
import jax
import jax.numpy as jnp #we can create numpy API calls with this import
import numpy as np
import time


#JAX vs Numpy



#automatic differentiation




#========================
"""Just in time (JIT) compilation"""
#========================
def myfunc(x):
    """this function returns a division by 2 if its an even number, else 3 * x + 1"""
    return jnp.where(x % 2 == 0, x / 2, 3 * x + 1) #collatz conjecture, eventually it goes back to the same place


arr = jnp.arange(10) # creates an array in the range of these numbers
start = time.perf_counter() #starting a timer
myfunc(arr).block_until_ready() #efectuates the function, it waits until ready since it performs asynchronously
end = time.perf_counter() # ends the timer
print(end - start) #output: should take somwhere between 0.19 and 0.2 seconds to effectuate

"""this shows you the power of just in time compilation
jit is good for training loops since they are fast."""

jaxpr_code = jax.make_jaxpr(myfunc)(arr) #code sent to the gpu as an object
print(jaxpr_code) #we can store to object and print it
# the otucome of this function is a lagre computation turned into bytecode



@jax.jit #decorator method for calling a just in time compile on a function
def f(x):
    if x % 2 == 0:
        return 1
    else:
        return 0

f(10)
#jit compiling this will not work on parameters set as conditionals
#this will give us a TracerBoolConversionError:

#============================
"""Automatic Differentiation"""
#============================

#FIRST EXAMPLE
def square(x):
    return x ** 2

#x = 10 <- sets value of x to ten
# f(x) = x ** 2 = 100 <- the normal function would return 100
#f'(x) = 2x = 20 <-- the derivative of the original would return 2x the value
#f''(x) = 2 = 2 <- double derivative would return a constant 2 in this instance
# f '''(x) = 0 <- a triple derivative returns 0, since the exp base of the letter variable of 2 is 0 

"""the above formula calls the derivative of the returned formula. These can
be compounded until it reaches 0. going past the point where 0 has been reached, 0 will still be hit"""
value = 10.0
print(jax.grad(square)(value))
print(jax.grad(jax.grad(square))(value))


#SECOND EXAMPLE
def f(arr): #potential for multiple, partial derivatives derivatives
    return arr[0] ** 2 + 2 * arr[1] ** 2 + 3 * arr[2] ** 2 #we can pass vectors instead of individual arguments

x, y, z = 2.0, 2.0, 2.0
# x ^ 2 + 2y ^ 2 + 3z ^ 2
#df/dx = 2x = 4
#df//dy = 4x = 8
#df/dz = 6x = 12

print(f[x, y, z]) #be sure to pass this as an array
#argnums is used as a keyword to select the function argument by index
print(jax.grad(f)([x, y, z])) #this selects the first index(x)


#============================
"""Automatic vectorization"""
#============================
key = jax.random.key(42) #this passes a random key


W = jax.random.normal(key, (150, 100)) #100 values per input per 150 neurons in next level
X = jax.random.normal(key, (10, 100)) #ten input of 100 values


"""Example # 1"""

def calculate_output(x): #this calculates the output of W per x inputs
    return jnp.dot(W, x) #this is to make it compatible with a full batch by using the next function

def batched_calculation_loop(X):
    """this function manually effectuates the contents given to
    every single input. Think of it as a way to hard code the results effectuated
    by the previous function and storing those inside a new array"""
    return jnp.stack([calculate_output(x) for x in X])


def batched_calculations_manual(X):
    """returns the transponse of the weight matrix"""
    return jnp.dot(X, W.T)


"""Example #2"""
batched_calculation_vmap = lambda X: jax.vmap(calculate_output) #this vectorizes the function to work for batches

start = time.perf_counter()
batched_calculation_loop(X)
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
batched_calculations_manual(X)
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
batched_calculation_vmap(X) #this allows you to perform fast vectorization of matrices without everything done manually
end = time.perf_counter()
print(end - start)
np.testing.assert_allclose(batched_calculation_loop(X), batched_calculations_manual(X), atol=1E-4, rtol=1E-4)
np.testing.assert_allclose(batched_calculation_loop(X), batched_calculation_vmap(X), atol=1E-4, rtol=1E-4)


#=========================
"""randomness"""
#=========================

"""Example 1"""

#we have an implicit global state that hss to be coordinated and shared. Everything depends on said global state
#with JAX, we have the capacity of this data being reproduced, parallelized and vectorized
#with numpy, it is only capable of being reproduced, we cannot parallelize and vectorize effectively

now_key = jax.random.key(42)#write once, use once, and then discard

key1, key2 = jax.random.split(now_key) #this function has the capacity to split and duplicate keys that will be discarded

#*NOTE- when keys are split, they are inmediately consumed, so in the above example, now_key is consumed
#random activity requires the cyclic process of provision and discarding of single keys

