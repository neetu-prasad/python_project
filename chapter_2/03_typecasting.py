# type() function and typecasting
#type function is used to find the datatype of the given variable in python

# a=31
# type(a) ---> class <int>

# b="31"
# type(b) ---> class <str>
a="3534"
a=int(a)
print (type(a)) # here its converting string to integer, it will nly accept if the given value is valid 
print(a+5) # it will add +5 to a and give 3539 as o/p
#type casting is a way to convert one data type to another ex: char to int, int to foat etc etc

#a="34cdf56"
#a=int(a) #it will definitely throw an error as we cannot change that string to integer
#print(a+5) # here we get error as - ValueError: invalid literal for int() with base 10: '34cdf56'
#  number can be converted to string an vice versa

#str(32) => "31"
#  #integer to string conversion
# int("32") => 32 --> string to integer conversion
# float(32) => 32.0 integer to float conversion.... and so on
# here 31 is a string literal and 31 a numeric literal
