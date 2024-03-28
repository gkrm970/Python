## 1) how to use fixture in pytest?
## 2) how to run a specific method before each test method in a class using fixture?
## 3) how to run a specific method before all test methods in a class using fixture?
## 4) How to run a specific method before all the classes using fixture?
## 4. How to execute a fixture automatically on running any file?
## 5) how to use dependency in pytest?
    using pytest dependency in pytest framework
    INSTALL PYTEST-dependency
    if dependent test fail then followed method will get skipped .
def test_method1():
    print("this is test method 1")

@pytest.mark.dependency(method=["test_method1"])
def test_method2():
    print("this is test method 2")

@pytest.mark.dependency(method=["test_method2"])
def test_method3():
    print("this is test method 3")

## 6) what is a finalizer and how to use it inside a fixture?
      @pytest.fixture(scope="class", autouse=True)
      @pytest.fixture(scope="session", autouse=True)
      @pytest.fixture(scope="function", autouse=True)
      
      def setup(request):
          print("this is setup method")

          def teardown():
              print("this is teardown method")

          request.addfinalizer(teardown)  

        or 

      @pytest.fixture()
      def setup():
          print("this is setup method")
          yield
          print("this is teardown method")

## 8) how to call fixture from a test method?

## 9) How to use fixture inside another fixture?
## 10) How to use fixture inside a class?
## 11) How to run the same test method for a multiple set of data or how to do parameterization in a pytest framework?
     @pytest.mark.parametrize("arg1, arg2", [("a", "b"), ("c", "d")])
    def test_method1(arg1, arg2):
        print(arg1, arg2)
    
