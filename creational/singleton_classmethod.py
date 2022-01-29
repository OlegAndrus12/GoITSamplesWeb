# What the Gang of Four’s original Singleton Pattern
# might look like in Python.

class Logger(object):
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
            # Put any initialization here.
        return cls._instance


if __name__ == "__main__":
    # The client code.

    try:
        # creating an object in traditional way
        s = Logger()
    except RuntimeError as err:
        print(err)
        
    s1 = Logger.instance()
    s2 = Logger.instance()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
