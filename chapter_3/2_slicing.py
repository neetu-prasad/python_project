greeting = "good eveng"
name = "neetu"
c = greeting + name
print(c)
# also--> print(greeting + Name) will give directly without adding c = gr+name 
#concatenating two strings




#slicing example
name = "harry"
print(name[4])
# name [3] = 'd' -----> it wil not work
#it will print y as string adress strt with , 0,1,2,3..... or from backwards i.e,  .....-3,-2,-1


#String slicing
print(name[1:4])   
#it will print from 1,2,and 3 (arr) from harry it will not display 4th letter, 
#print(name[2:5])--> it will print 2,3,4th (rry) from harry letters
# first includes and secnd excludes --> in [] ,this is called as slicing.
# print(name[:4])--> is equal to name[0:4]
'''
syntax --->  syntax = name[ind_start : ind_end]  #ind--->index
ex: sl[0:3] returns "har" --> characters from 0 to 3
     sl[1:3] returns "ar" --> characters from 1 to 3.
    '''
c= name[-4:-1] 
print(c)
'''negative indices  : if we dnt know the lenght of string and need last index, we will give -1 as from last it indicates as ......-4,-3,-2,-1  
        print(c) gives ---> same as [1:4 ] in case of harry
    ''' 


  #  slicing with skip value#  
d = name[1:4:2] 
print(d)  #it prints ar from harry -- from 1 to 4 it wil skip every single letter





