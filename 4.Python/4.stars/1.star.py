print("*")
print("**")
print("***")
print("****")
print("*****")

def draw_ltri(lines):
    for i in range(1,lines+1):
        print("*"*i)
    

def draw_rtri(lines):
    for i in range(1,lines+1):
        print(" "*(lines-i) + "*"*i)

draw_rtri(5)

# def draw_irtri(lines):

# def draw_iltri(lines):


print("-"*10)

def draw_iltri(lines):
    for i in range(lines):
        print("*"*(lines-i))


draw_iltri(5)

def draw_irtri(lines):
    for i in range(lines):
        print(" "*i + "*"*(lines-i))

draw_irtri(5)


def draw_iltri2(lines):
    for i in range(lines,0,-1):
        print("*"*i)

draw_iltri2(7)