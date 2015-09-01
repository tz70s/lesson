#!/usr/bin/env python3

fh = None

class FunckedError(EnvironmentError):pass

try:
    fh = open("hello.txt",encoding = "utf8")
    # programmer can check the error message in the Traceback
    # by using assert
    assert fh , "No such file ass hole"
    #not neccessary of raise using , just demostration

except (IOError, OSError) as err:
    print (err)
    raise FunckedError()
else:
    pass
finally:
    if fh is not None:
        fh.close()
print ("End of file opening")

'''
additional using of exception
especially we want to break out in many loops

raise exception
raise exception from original exception
raise

'''
