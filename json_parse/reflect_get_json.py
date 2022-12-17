''' 
使用反射解析嵌套json 
参考链接：https://www.cnblogs.com/rexcheny/p/10973543.html
'''
import sys
import json
import importlib

class Play:
    def __init__(self) -> None:
        self._sport = []
        self._game = []
    
    def __str__(self) -> str:
        return self.__class__.__name__

    
    @property
    def Sport(self):
        return self._sport
    
    @Sport.setter
    def Sport(self,sport):
        self._sport = sport
    
    @property
    def Game(self):
        return self.Game
    
    @Game.setter
    def Game(self,game):
        self._game = game

class Person:
    def __init__(self) -> None:
        self._name = "1"
        self._sex =""
        self._blood_type = "0"
        self._hobbies = []
        self._date_of_birth = "1900/1/1"
        self._play = Play()
    
    def __str__(self) -> str:
        # print("this is __str__")
        return self.__class__.__name__ 
    
    @property
    def Name(self):
        return self._name
    
    @Name.setter
    def Name(self,name):
        self._name = name
    
    @property
    def Sex(self):
        return self._sex
    
    @Sex.setter
    def Sex(self,sex):
        return self._sex
    
    @property
    def BloodType(self):
        return self._blood_type
    
    @BloodType.setter
    def BloodType(self,blood_type):
        self._blood_type = blood_type
    
    @property
    def Hobbies(self):
        return self._hobbies
    
    @Hobbies.setter
    def Hobbies(self,hobbies):
        self._hobbies = hobbies
    
    @property
    def date_of_brith(self):
        return self._date_of_birth
    
    @date_of_brith.setter
    def date_of_brith(self,date_of_brith):
        self._date_of_birth = date_of_brith

    @property
    def Play(self):
        return self._play
    
    @Play.setter
    def Play(self,play):
        self._play = play


def get_instance(str_stream,class_full_path=None):

    try:
        json_obj = json.loads(str_stream)
    except Exception as err:
        print("err",err)
        return None
    
    # if class_full_path is None:
    #     return json_obj
    
    obj = Person()

    for key in json_obj.keys():
        obj.__setattr__(key,json_obj[key])
    # print("--->")
    # print(obj)
    return obj


def main():
    str1 = '{"Name": "Alex", "Sex": "Male", "BloodType": "A", "Hobbies": ["篮球", "足球"], "Play":{"Sport": ["篮球","足球","羽毛球"],"Game": ["英雄联盟","王者荣耀"]}}'
    person1 = get_instance(str1)
    print(person1)
    # 查看类型
    print("查看类型",type(person1))
    # 查看属性
    print("查看属性",person1.__dict__)
    # 查看指定属性
    print("查看指定属性名",person1.Play)

if __name__ == "__main__":
    main()

        
