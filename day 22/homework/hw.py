# n1

word = input("enter a word: ")

print("lower case: ", word.lower())
print("upper case: ", word.upper())
print("capitalize the first letter: ", word.capitalize())

# n2

sentence = input("enter a sentence: ")
sent = input("enter a 2nd sentence: ")
sntnc = input("enter a 3rd sentence: ")
print("lowercase", sentence)
print("uppercase", sent)
print("capitalize", sntnc)

# n3

my_name = "mari"
name = input("enter your name: ")
if my_name.lower == name.lower():
    print("Our names are similiar!: ")
else:
    print("we have different names: ")

# n4

wordless = "nothing"
print(wordless.capitalize())

# n5

# .upper() ყველა ასო დიდია
# word.upper() -> WORD

# .lower() ყველა ასო პატარაა
# kvercxi.lower() -> kvercxi

# .capitalize() მარტო პირველი ასოა დიდი, დანარჩენი პატარა
# soul.capitalize() -> Soul

# .replace() ანაცვლებს სტრინგს ახალით
# noob.replace() -> buns

# .find() აბრუნებს ფრჩხილებში გადაცემული სიმბოლოს ინდექსს
# dumb.find("m") -> 3

# .swapcase უცვლის სტრინგს და მის სიმბოლოებს case-ს ანუ lower->upper/upper->lower
# salami.swapcase()-> SALAMI

# .isupper() შედგება თუ არა სტრინგი მხოლოდ დიდი ასოებისგან
# HELLO.isupper -> True

# .islower() შედგება თუ არა სტრინგი მხოლოდ პატარა ასოებისგან
# WASSUP.islower() -> False

# .isdigit() შედგება თუ არა სტრინგი მხოლოდ ციფრებისგან
# 230211.isdigit() -> True

# .isalpha() შედგება თუ არა სტრინგი მხოლოდ ასოებისგან
# kvat1.isalpha() -> False

# .isalnum() შედგება თუ არა სტრინგი მხოლოდ ციფრებისა და ასოებისგან
# 2ad2megobari2jujavart.isalnum() -> True