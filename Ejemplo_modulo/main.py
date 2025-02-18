# import edad as ed

# print (ed.calcula_edad("18/02/2000", "18/02/2025"))

from edad import calcula_edad as function_calcula_edad

print(range.__doc__)

if __name__  == "__main__":
    print(function_calcula_edad("18/02/2000", "18/02/2025"))
    print(function_calcula_edad.__doc__)

