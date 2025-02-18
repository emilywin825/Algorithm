# n=int(input())

# note=[]
# for _ in range(n):
#     note.append(input())


# for _ in range(n-1):
#     poem= input()
#     if poem in note:
#         note.remove(poem)

# print(note.pop())
# # ------------------------------------

n=int(input())

note=dict()
for _ in range(n):
    word=input()
    note[word]=1

for _ in range(n-1):
    poem= input()
    note[poem]=0

for key,val in note.items():
    if val==1:
        print(key)
        break