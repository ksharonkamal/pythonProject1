class int_roman:
    def int_roman(self,num):
        integer_num=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        roman_num=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        result=""
        i=0
        while(num!=0):
            if(integer_num[i]<=num):
                result+=roman_num[i]
                num-=integer_num[i]
            else:
                i=i+1
        print(result)


obj1=int_roman()
num=int(input("Enter a number:"))
obj1.int_roman(num)