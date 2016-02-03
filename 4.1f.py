try:
    x = 5 + 'ham'
except Exception as e:
       print(type(e))
       print(e)  
       print("\n")

try:
    x =  1/0
except Exception as e:
    print(e)
    print("\nnew line")
except ZeroDivisionError:
    print('ZeroDivisionError')
finally:
    print('finally hit')
    
    
try:
    x = 4 + test
except Exception as e:
    print(type(e))
    print(e)
    print("\n x = 4 + test")
except NameError as i:
    print('name error')
    print(i)
except:
    print('not a name error')
    
try:
    x = 4 + "string"
except Exception as e:
    print(type(e))
    print(e)
except TypeError:
    print('type error')