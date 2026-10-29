input_str = "teeterjacdacdaaaaz"

for char in input_str:
    print("get data was ",input_str.count(char))
    if input_str.count(char) == 1:
        print("Char is: ", char)
        break