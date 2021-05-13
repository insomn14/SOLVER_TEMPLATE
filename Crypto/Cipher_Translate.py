import string


firstString  = 'qwertyuiopasdfghjklzxcvbnm'
secondString = 'abcdefghijklmnopqrstuvwxyz'



string = 'zpezy{ktr_gkqfut_hxkhst_tyukokkgotyt_hoftqhhst_ykxoz_qxilrtxiyf}'

print("Original string:", string)

translation = string.maketrans(firstString, secondString)

# translate string
print("Translate string:", string.translate(translation))
