from typing import Callable, Any


def Autowire(dependency: Callable[..., Any]) -> Any:
    to_call: Callable[..., Any] = None

    if not callable(dependency):
        TypeError(f"Supply Callable. Got {type(dependency)}")

    if isinstance(dependency, type):
        to_call = autowire_class_type(dependency=dependency)
    else:
        to_call = dependency

    return to_call()


def autowire_class_type(cls_dependency: type) -> type:
    """Takes in a class definition and determines which type needs to be called to 
    later instantiate an object. 
    Use Case primary for abstract class definitions whose concrete implemention will be
    looked up in the `__subclasses_` call.

    Args:
        cls_dependency (type): type definition (class definition to examine)

    Raises:
        Exception: On multiple subclasses of an abstract base class the concrete object is ambiguous

    Returns:
        type: The type definition which should be used
    """    
    cls_to_call: Callable[..., Any] = None

    if not is_abstract(cls_dependency):
        cls_to_call = cls_dependency
    else:
        subclasses = cls_dependency.__subclasses__()

        if len(subclasses) != 1:
            raise Exception(
                f"Ambiguous Wiring: Subclasses for {type(cls_dependency)}: {subclasses}"
            )
        else:
            cls_to_call = subclasses[0]

    return cls_to_call


def is_abstract(cls: type) -> bool:
    return bool(getattr(cls, "__abstractmethods__", False))
