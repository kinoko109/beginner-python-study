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

chose_from_two = ('A', 'B', 'C')

answer =[]
answer.append('A')
answer.append('B')

print(answer)

# 辞書型
d = {
  'x': 10,
  'y': 20,
}
print(d)

d['x'] = 'xxxx'
print(d)

print(dict(a=10, b=123))

print(dict([('a', 'aaa'), ('b', 'bbbb')]))

# 集合
s = {1, 2, 3, 4, 5}

s.add(6)
print(s)

s.remove(3)
print(s)

s.clear()
print(s)
print(type(s))

a = {}
print(type(a))

my_frineds = { 'a', 'b', 'c' }
other_frineds = { 'c' }

print(my_frineds & other_frineds)

f = ['apple', 'banana', 'apple']
kind = set(f)
print(kind)

# if
x = [1, 3]
y = 1

if y in x:
  print('in')

if "d" not in x:
  print('not in')

is_ok = True
if not is_ok:
  print('not is_ok')
else:
  print('is_ok')

# 基本的にisはNoneを判定するときに使う
is_empty = None
if is_empty is None:
  print('none')

# while
count = 0
while count <= 5:
  print(count)
  count += 1

print('##########')

count2 = 0
while count2 < 5:
  if count2 >= 5:
    print(count2)
    break

  if count2 == 3:
    count2 += 1
    continue

  print(count2)
  count2 += 1
