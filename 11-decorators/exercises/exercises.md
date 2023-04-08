# Decorator Exercises

1. Create a decorator that logs the arguments and return value of a function. The decorator should print the arguments passed to the function, the return value of the function, and the time it took for the function to execute.

2. Create a decorator that validates the arguments passed to a function. The decorator should check that the arguments are of the correct type and within the correct range. If the arguments are invalid, the decorator should raise an exception with a custom error message.

3. Create a decorator that caches the results of a function. The decorator should check if the function has been called with the same arguments before. If it has, the decorator should return the cached result. If not, the decorator should call the function and cache the result for future calls.

4. Create a decorator that limits the rate at which a function can be called. The decorator should take a rate limit as an argument and ensure that the function is not called more than the specified number of times per second. If the function is called more than the limit, the decorator should raise an exception with a custom error message.
