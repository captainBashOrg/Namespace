# Пространство имен

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
        #print('__main__')

    inner_function()


print ("Пространство имен\n\n")


test_function()