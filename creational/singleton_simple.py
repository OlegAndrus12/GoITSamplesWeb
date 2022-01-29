class DatabaseConnector:
    __instance = None

    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance


if __name__ == "__main__":
    # The client code.

    s1 = DatabaseConnector()
    s2 = DatabaseConnector()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
    