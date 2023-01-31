import abc
import pytest

from src.draw.common.autowire import is_abstract, Autowire

class IAbstract(metaclass=abc.ABCMeta):
    
    def __init__(self):
        pass

    @abc.abstractmethod
    def sample_method(self):
        pass

class Concrete(IAbstract):
    
    def sample_method(self):
        return None
    
    def __call__(self):
        return "Concrete"

def hello():
    return "Hello World!"

class OnlyAbstract(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def abstract_method(self):
        pass

@pytest.mark.parametrize("test_obj", [
(Concrete)
])
def test_is_abstract_for_concrete(test_obj):
    assert not is_abstract(test_obj)

@pytest.mark.parametrize("test_obj", [
(IAbstract)
])
def test_is_abstract_for_abstract(test_obj):
    assert is_abstract(test_obj)

@pytest.mark.parametrize("test_obj, test_type", [
    (Concrete(), str), 
    (Concrete, Concrete),
    (IAbstract, Concrete),
    (hello, str),
])
def test_autowire(test_obj, test_type):
    test_result = Autowire(test_obj)
    assert isinstance(test_result, test_type)
    assert not isinstance(test_result, type) # not a class anymore
    assert not bool(getattr(type(test_result), "__abstractmethods__", False)) # not abstract

@pytest.mark.parametrize("test_obj", [(1), ("hello"), (Concrete()())])
def test_autowire_no_callable(test_obj):
    with pytest.raises(TypeError):
        Autowire(test_obj)

@pytest.mark.parametrize("test_obj", [OnlyAbstract])
def test_autowire_no_concrete_for_abstract(test_obj):
    with pytest.raises(Exception) as exc:
        Autowire(test_obj)
    
    assert "Ambiguous Wiring: Subclasses for" in exc.value.args[0]