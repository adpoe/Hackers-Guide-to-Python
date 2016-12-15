# decorator is a fn that takes another function as an argument,
# and replaces it with a new, modified fn.

# simplest
def identity(f):
    return f

# in use (though useless); just returns same fn
@identity
def foo()
    return 'bar'

# registering a decorator
_functions = {}
def register(f):
    global _functions
    _functions[f.__name__] = f
    return f

@register
def foo():
    return 'bar'

# common use case:
# --> factor common code that needs to be called before, or after multiple functions

# example
class Store(object):
    def get_food(self, username, food):
        if username != ’admin’:
            raise Exception(”This user is not allowed to get food”)
        return self.storage.get(food)

def put_food(self, username, food):
    if username != ’admin’:
        raise Exception(”This user is not allowed to put food”)
    self.storage.put(food)

# first step
# refactor the if username != 'admin' part, so no need to repeat it
def check_is_admin(username):
        if username != 'admin':
            raise Exception(”This user is not allowed to get food”)

class Store(object):
    def get_food(self, username, food):
        check_is_admin(username)
        return self.storage.get(food)

    def put_food(self, username, food):
        check_is_admin(username)
        self.storage.put(food)

# better (using decorators)
def check_is_admin(f):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != admin
            raise Exception("This user is not allowed to get food")
        return f(*args, **kwargs)
    return wrapper

class Store(object):
    @check_is_admin
    def get_food(self, username, food):
        return self.storage.get(food)

    @check_is_admin
    def put_food(self, username, food):
        self.storage.put(food)

# however, this naive approach to using decorators has drawbacks
# --> decorator REPLACES original fn with a new one, on the fly
# but new fn lacks many of the attributes of original fn, such as docstring and argument
# --> SO: functools module solves this problem. with update_wrapper fucntion
# AND we can use the @functools.wraps(f) decorator ON decorators to automate this
import functools
    def check_is_admin(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            if kwargs.get(’username’) != ’admin’:
                raise Exception(”This user is not allowed to get food”)
            return f(*args, **kwargs)
        return wrapper

class Store(object):
    @check_is_admin
    def get_food(self, username, food):
        return self.storage.get(food)

# use the inspect module to retrieve a fn's signature and operate on it
import functools
import inspect

    def check_is_admin(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            # inspect use on next line
            func_args = inspect.getcallargs(f, *args, **kwargs)
            if func_args.get(’username’) != ’admin’:
                raise Exception(”This user is not allowed to get food”)
            return f(*args, **kwargs)
        return wrapper

@check_is_admin
def get_food(username, type=’chocolate’):
    return type + ” nom nom nom!”

# inspect.getcallargs returns a dictionary containing the names and values of the arguments
# as key-value pairs. (I.e. - {’username’:’admin’, ’type’:’chocolate’})
# means: NO MORE CHECKING FOR POSITIONAL VALUE OF AN ARG!!!! so much yes.

# can use @staticmethod to create methods that belong to a class,
# but don't operate on specific instances
class Pizza(object):
    @staticmethod
    def mix_ingredients(x, y):
        return x + y

    def cook(self):
        return self.mix_ingredients(self.cheese, self.vegetables)

# most importantly, we know static methods don't depend on state of an instantiated object
# common across languages, but good to know for python-specifically
# AND we can override the static method in subclasses without worry


# use @classmethod to bind a method to a class only. useful for factory methods
# that instantiate objects in a specific fashion
class Pizza(object):
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def from_fridge(cls, fridge):
        return cls(fridge.get_cheese() + fridge.get_vegetables())
    # think --> returns a brand new pizza using ingredients from what's currently avilable in my fridge

# abstract methods are defined in a base that does not necessarily provide an implementation
class Pizza(object):
    @staticmethod
    def get_radius():
        raise NotImplementedError
        # any class inheriting from pizza should implement this

# use the abc module to enforce this an get an early warning, avoid runtime error
import abc
class BasePizza(object):
    __metaclass__  = abc.ABCMeta

    @abc.abstractmethod
    def get_radius(self):
        ”””Method that should do something.”””

# mixing these: can extend the abstract prototype as we see fit
class Calzone(BasePizza):
    def get_ingredients(self, with_egg=False):
        egg = Egg() if with_egg else None
        return self.ingredients + [egg]

# can define Calzone's methods any way we like, sas long as they support interface designed in the BasePizza class
import abc
class BasePizza(object):
    __metaclass__  = abc.ABCMeta

    @abc.abstractmethod
    def get_ingredients(self):
     ”””Returns the ingredient list.”””

class DietPizza(BasePizza):
    @staticmethod
    def get_ingredients():
        return None # ha.

# Unlike Java --> can also put code in abstract methods themselves
# and call this user super()
# here: all Pizza subclasses need to override the get_ingredients method
#   BUT - they have access to the default mechanism for getting ingrendients
#   in the superclass, using super()
import abc
class BasePizza(object):
    __metaclass__  = abc.ABCMeta

    default_ingredients = [’cheese’]

    @classmethod
    @abc.abstractmethod
    def get_ingredients(cls):
        ”””Returns the default ingredient list.”””
        return cls.default_ingredients

class DietPizza(BasePizza):
    def get_ingredients(self):
        return [Egg()] + super(DietPizza, self).get_ingredients()

# notes on super() --> is actually a constructor, instantiated each time we call it
