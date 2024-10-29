ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

i = 0
for i in range(2):
    if ft_list[i] != "Hello":
        ft_list[i] = "World!"
    ft_tuple = ("Hello", "France!")
    ft_set.discard("tutu!")
    ft_set.add("Angouleme!")
    ft_dict["Hello"] = "42Angouleme!"
    

        
    


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)