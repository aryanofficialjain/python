def debug(func):
    def wrapper(*agrs, **kwargs):
        return func(*agrs, **kwargs)
    
    return wrapper




def greet(greet, name):
    return (f"{greet} + {name}")


print(greet(greet="hola", name="Aryan"))

