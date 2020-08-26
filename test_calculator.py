import calculator as c
import math
import pytest
@pytest.mark.parametrize(
    "arg, expected_output", [[(-1, -1), -2], [(1, 1), 2], [(1, 0), 1],[(1,-1),0],[(0,0),0],[(1,2),3],[(5,5),10]]
)
def test_add_int_exercise_1(arg,expected_output):
    assert c.add(arg[0],arg[1])==expected_output
@pytest.mark.parametrize(
    "arg, expected_output", [[(-0.1, -0.1), -0.2], [(0.1, 0.1), 0.2], [(0.1, 0), 0.1],[(0.1,-0.1),0],[(0,0),0],[(0.1,0.2),0.3],[(0.5,0.5),1]]
)
def test_add_float_exercise_2(arg,expected_output):
    tol=1e-12
    assert abs(c.add(arg[0],arg[1])-expected_output)<tol
@pytest.mark.parametrize(
    "arg", [(str(i),i) for i in range(-100,100)]
)
def test_add_error_exercise_5(arg):
    with pytest.raises(TypeError):
        c.add(arg[0],arg[1])
@pytest.mark.parametrize(
    "arg, expected_output", [[("Hello ", "World"), "Hello World"], [("", "Hi"), "Hi"], [("1", "1"), "11"],[("",""),""],[("1","Hello"),"1Hello"],[("abc","def"),"abcdef"],[("B","ooo"),"Booo"]]
)
def test_add_str_exercise_3(arg,expected_output):
    assert c.add(arg[0],arg[1])==expected_output
@pytest.mark.parametrize(
    "arg", [i for i in range(100)]
)
def test_factorial_exercise_4(arg):
    assert c.factorial(arg)==math.factorial(arg)
@pytest.mark.parametrize(
    "arg", [i for i in range(-10,10)]
)
def test_sin_exercise_4(arg):
    tol=1e-12
    assert abs(c.sin(arg,100)-math.sin(arg))<tol
@pytest.mark.parametrize(
    "arg, expected_output", [[(-1, -1), 1], [(1, 1), 1],[(1,-1),-1],[(1,2),0.5],[(-5,5),-1],[(0.1,0.2),0.5]]
)
def test_divide_exercise_4(arg,expected_output):
    assert c.divide(arg[0],arg[1])==expected_output
@pytest.mark.parametrize(
    "arg", [i for i in range(-100,100)]
)
def test_divide_error_exercise_5(arg):
    with pytest.raises(ZeroDivisionError):
        c.divide(arg,0)
@pytest.mark.parametrize(
    "arg", [i for i in range(100)]
)
def test_root_exercise_4(arg):
    assert c.root(arg)==math.sqrt(arg)
@pytest.mark.parametrize(
    "arg", [i for i in range(-100,100)]
)
def test_absolote_exercise_4(arg):
    assert c.absolute(arg)==abs(arg)
