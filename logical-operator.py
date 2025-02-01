password = "Password123$"
confirmPassword = "Password123"



# create validation for checking password is same with confirmPassword
# operator and
checkingPassword = password == "Password123$" and password == confirmPassword


isWork = False
isPressure = True

goodUser = isWork or isPressure

print(goodUser)