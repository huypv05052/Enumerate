#bonus: bài tập về enumerate()
#Bài 1: Tìm chỉ số của kí tự a trong xâu s
'''s=input('Nhập xâu s: ')
vi_tri_a=[]
for i,k in enumerate(s):
    if k=='a':
        vi_tri_a.append(i)
if vi_tri_a:
    print(f'Vị trí chứa kí tự a là: {vi_tri_a}')
else:
    print('Xâu s không chứa kí tự a.')'''



# Tìm 1 kí tự k bất kì trong xâu s
'''def findIndex():
    #Nhập xâu s
    while True:
        s=input('Nhập xâu s: ')
        if len(s)>0:
            break
        else:
            print('Xâu s không được rỗng.')
    print(f'Xâu s được nhập: {s}')

    while True:
        k=input('Nhập kí tự muốn tìm: ')
        if len(k)==1:
            break
        else:
            print('Chương trình chỉ tìm được 1 kí tự.')

    #Tìm vị trí của k trong s:
    vi_tri_k=[]
    for i,value in enumerate(s):
        if value==k:
            vi_tri_k.append(i)

    if vi_tri_k:
        print(f'Vị trí của {k} trong xâu s là: {vi_tri_k}')
    else:
        print(f'Xâu s không chứa kí tự "{k}"')


findIndex()'''



#Tìm vị trí nhiều kí tự bất kì trong xâu s
def findIndex():
    while True:
        s=input('Nhập xâu s: ')
        if len(s)>0:
            break
        else:
            print('Xâu s không được rỗng.')
    #Nhập kí tự cần tìm (không trùng nhau)
    while True:
        chars=input('Nhập các ký tự muốn tìm (không trùng nhau): ')
        if len(chars)>0:
            break
        else:
            print('Vui lòng nhập ký tự muốn tìm.')
    
    for k in chars:
        vi_tri_k=[i for i,val in enumerate(s) if val==k]
        if vi_tri_k:
            print(f'Ký tự {k} xuất hiện tại vị trí {vi_tri_k}')
        else:
            print(f'Ký tự {k} không có trong xâu.')

findIndex()
