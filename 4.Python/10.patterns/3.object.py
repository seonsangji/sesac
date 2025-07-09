class User:
    pass
class Store:
    pass
class Item:
    pass

class DisplayData:
    def __init__(self, data):
        self.handlers = {
            User: self.display_str,
            Store: self.display_list,
            Item: self.display_dict,
        }
        handler = self.handlers.get(type(data), self.unsupported_type)
        handler(data)


    def display_str(self, data):
        print(f"문자열: {data}")

    def display_list(self, data):
        print(f"리스트: {data}")

    def display_dict(self, data):
        print(f"딕셔너리: {data}")

    def unsupported_type(self, data):
        print("지원하지 않는 타입입니다.")

DisplayData(User())
DisplayData(Store())
DisplayData(Item())
DisplayData(123)