"""error"""

from typing import Callable
import sys


def input_error(func: Callable[..., None]) -> Callable[..., None]:
    """Decorator for handling input errors"""
    def wrapper_input_error(*args: tuple, **kwargs: dict) -> None:
        """Wrapper function for handling input errors"""
        try:
            func(*args, **kwargs)

        except TypeError as error:
            print(f"TypeError: {error}")
           

        except ValueError as error:
            print(f"ValueError: {error}")
        
        except KeyError as error:
            print(f"KeyError: {error}")
           

    return wrapper_input_error
