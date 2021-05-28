class reverse_string:
    # def __init__(self,str):
    #     self.str=str
    def reverse(self,str):
        self.str = str
        res = str.split()
        res.reverse()
        result = " ".join(res)
        print(result)

str1=reverse_string()
str1.reverse("hi how are")



