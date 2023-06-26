from dataclasses import dataclass

class MetaSingleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]


@dataclass
class Settings(metaclass=MetaSingleton):
    db: str = "MySQL"
    port: int = 3306


if __name__ == '__main__':

    connect = Settings()
    

    connect_other = Settings()

    print(id(connect) == id(connect_other))


    print(connect_other.port)
    connect.port = 5634
    print(connect_other.port)
