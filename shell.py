import basic

while(True):
    text = input('basic >> ')
    result, error =  basic.run(fn='shell.py',text=text)    
    if(error): print(error.as_string())
    else: print(result)