def div(a,b):
    # if a < b:
    #     a,b = b,a 
    return a / b 

def smart_div(func):
    def logic(a,b):
        if a < b:
            a,b = b,a 
        return func(a,b)
    return logic

div = smart_div(div)

result = div(5,10)
print(result)