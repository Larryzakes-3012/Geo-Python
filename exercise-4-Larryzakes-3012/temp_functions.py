def fahr_to_celsius(temp_fahrenheit):
    converted_temp = round(((temp_fahrenheit - 32)/1.8),2)
    return converted_temp
# i defined a fucntion that converts temperature from farenheit to celsius degree. 
# the defined function takes a parameter of fahrenheit value


def temp_classifier(temp_celsius):
    if temp_celsius <-2:
        temp_celsius = 0
        return temp_celsius
    if temp_celsius >= -2 and temp_celsius < 2:
        temp_celsius = 1
        return temp_celsius
    if temp_celsius >=2 and temp_celsius < 15:
        temp_celsius = 2
        return temp_celsius
    if temp_celsius > 15:
        temp_celsius = 3
        return temp_celsius