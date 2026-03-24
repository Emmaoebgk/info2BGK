def adding(num1,num2):
    return num1 + num2

def solve_equalison(a,b):
    if a == 0:
        return None
    return -b / a

def solve_quadratic(a,b,c):
    if a == 0:
        return None, None
    d= b**2-4*a*c
    d_square = None

    if d == 0:
        d_square = 0

    elif d <0:
        d_square = None

    else:
        d_square = d**0.5

    if d_square is None:
        return None, None


    if d_square == 0:
        print("d = 0")
        return -b/(2*a),None
    else:
        print("d != 0")
        x1= (-b + d_square)/(2*a)
        x2 = (-b-d_square)/(2*a)
        return (x1,x2)




if __name__ == "__main__":
     c=adding(1,2)
     print(c)

