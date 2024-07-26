# Пространство имен

def test_function():
    def inner_function():
        def aaa():
            c = "123"
            print(c)

        #global a
        a= 3
        print("Я в области видимости функции test_function")
        #print('__main__')
        print (a)
        aaa()

    inner_function()   # вызов  inner_function()




print ("Пространство имен\n\n")

#inner_function()   # вызов  inner_function()
# а вот здесь вызов inner_function() невозможен, она в пространстве имен test_function


test_function()

