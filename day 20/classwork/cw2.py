# 1) პატარა ასოებით სტრინგი - Uppercase

small_text = "chat"
upper_text = small_text.upper()
print("Uppercase:", upper_text)

# 2) დიდი ასოებით სტრინგი - Lowercase

big = "CHAT"
lower = big.lower()
print("Lowercase:", lower)

# 3) პატარა ასოებით სტრინგი - პირველი ასო დიდად

sml = "chat"
capitalized= sml.capitalize()
print("Capitalized:", capitalized)

# 4) სტრინგიდან ასოების ინდექსები

text = "კაიპურისჭამა"
con = text.index("ჭ")
pro = text.index("პ")
print("ასო 'ჭ' ინდექსი:", con)
print("ასო 'პ' ინდექსი:", pro)