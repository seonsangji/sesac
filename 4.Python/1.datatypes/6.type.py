x=5
y="hello"
z=[1,2,3]

print(type(x))

print(isinstance(x, (int,float)))
# x는 int나 float로 만들어진거야?

class A:
    pass

class B (A):
    pass
    # B extends A : B는 A를 상속받앗다

b = B()
# b라는 변수를 B라는 클래스로 찍어냇다

print(isinstance(b,B)) 
# true..