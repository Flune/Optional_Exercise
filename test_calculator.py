import calculator as c
import math
import pytest
@pytest.mark.parametrize(
    "arg,expected_output",[[(1,2),3],[(-1,-1),-2],[(1,1),2],[(1,0),1],[(1,-1),0],[(0.1,0.2),0.3],[("Hello ","World"),"Hello World"]]
)
def test_add(arg,expected_output):
    tol=10**-16
    if not(isinstance(arg[0], str) or isinstance(arg[1], str)):
        assert abs(c.add(arg[0],arg[1])-expected_output)<tol
    else:
        assert c.add(arg[0],arg[1])==expected_output
    with pytest.raises(TypeError):
        c.add("Hello",1)
@pytest.mark.parametrize(
    "nr",[i for i in range(100)]
)
def test_factorial(nr):
    assert c.factorial(nr)==math.factorial(nr)
@pytest.mark.parametrize(
    "nr",[i for i in range(-10,10)]
)
def test_sin(nr):
    tol=10**-12
    assert abs(c.sin(nr,100)-math.sin(nr))<tol
@pytest.mark.parametrize(
    "arg,expected_output",[[(1,2),0.5],[(1,4),0.25],[(6,2),3],[(5,1),5],[(-1,-2),0.5],[(-1,2),-0.5],[(1,-2),-0.5]]#add decimal division?
)
def test_divide(arg,expected_output):
    assert c.divide(arg[0],arg[1])==expected_output
    with pytest.raises(ZeroDivisionError):
        c.divide(1,0)
@pytest.mark.parametrize(
    "nr",[i for i in range(100)]
)
def test_root(nr):
    tol=10**-12
    assert c.root(nr)==math.sqrt(nr)
    assert abs(c.root(nr**3,3)-nr)<tol
    assert abs(c.root(nr**4,4)-nr)<tol
    assert abs(c.root(nr**5,5)-nr)<tol
@pytest.mark.parametrize(
    "nr",[i for i in range(-100,100)]
)
def test_absolute(nr):
    assert c.absolute(nr)==abs(nr)