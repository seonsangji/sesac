class DisplayData:
    def __init__(self, data):

        self.handlers = {
            str: self.display_str,
            list: self.display_list,
            dict: self.display_dict,
        }
        if isinstance(data, str) == "str":
            self.display_str(data)
        elif isinstance(data, list) == "list":
            self.display_list(data)
        elif isinstance(data, dict) == 'dict':
            self.display_dict(data)
        else : 
            raise TypeError("지원하지 않는 타입입니다.")


    def display_str(self, data):
        print(f"문자열: {data}")

    def display_list(self, data):
        print(f"리스트: {data}")

    def display_dict(self, data):
        print(f"딕셔너리: {data}")

DisplayData("hello")
DisplayData([1,2,3])
DisplayData({ })