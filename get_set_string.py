class string:
    str=""

    def get_string(self):
        string.str=input("Enter String:")
        # print(string.str.upper())

    def print_string(self):
        str1=string.str.upper()
        print(str1)


obj=string()
obj.get_string()
obj.print_string()
