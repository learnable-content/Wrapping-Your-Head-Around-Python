try:
    raise Exception('testing exception')
except:
    print('exception raised')
    
try:
    raise SystemError('testing exception')
except SystemError as e:
    print('system error raised')
except Exception as e:
    print('general exception raised')
    
class MyException(RuntimeError):
   def __init__(self, arg):
      self.args = arg,
      
try:
   raise MyException('custom exception')
except NameError as e:
   print('name exception raised')
except MyException as e:
   print(e.args)
except Exception as e:
    print('general exception raised')