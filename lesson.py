a = "test"
b = a
c = b
print(c)

num = 1
name = '1'

is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

# あとから上書きすると型も動的に変わる
name = num
print(name, type(name))  # str -> int

# printの書き方
print('Hi', 'John')  # 半スペが適用される
print('Hi', 'John', sep=',')  # カンマで区切る（半スペが適用されない）
print('Hi', 'John', sep=',', end='.\n')  # 末に挿入

# バックスラッシュと改行を組み合わせると改行で表示可能
print('#########')
print("""\
hello
hello
hello
hello
hello\
""")
print('#########')

# スライス
word = 'Python'
print(word[0:3])  # Pyt
print(word[:3])  # Pyt
print(word[0:])  # Python
print(word[:])  # Python
print(len(word))  # 6

greetWord = 'My name is Mike. Hello, Mike.'
print(greetWord.startswith('My'))  # True
print(greetWord.startswith('Mike.'))  # False
print(greetWord.find('Mike'))  # 11
print(greetWord.rfind('Mike'))  # 24

print('My name is {myName}. Hi {friendName}'.format(myName='Yamada', friendName='Satou'))

# python3.6からfにアップデートされた
myName = 'Yamada'
friendName = 'Satou'
print(f'My name is {myName}. Hi {friendName}')

# リスト型
list = [1, 2, 3, 4, 5, 6]
# 3つとばし
print(list[::3])  # [1, 4]