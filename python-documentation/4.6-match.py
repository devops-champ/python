

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "nothing"
        case _: #this acts as s wildcard entry. So any values other than the defined values are returned this value
            return "Something's wrong with the internet"
        
        
print(http_error(20))   


point = (0, 10)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")        