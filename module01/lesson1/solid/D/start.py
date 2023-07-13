'''
the FrontEnd class depends on the BackEnd class and its concrete implementation. 
You can say that both classes are tightly coupled. This coupling can lead to
scalability issues. For example, say that your app is growing fast, and you want 
the app to be able to read data from a REST API
'''
class FrontEnd:
    def __init__(self, back_end):
        self.back_end = back_end

    def display_data(self):
        data = self.back_end.get_data_from_database()
        print("Display data:", data)

class BackEnd:
    def get_data_from_database(self):
        return "Data from the database"