#Nhập danh sách n tên học sinh từ bàn phím, tìm và in ra tên có nhiều kí tự nhất và vị trí của tên đó trong danh sách.

while True:
    try:
        n=int(input('n='))
        if n>0:
            break
        else:
            print('Nhập n nguyên dương.')
    except ValueError:
        print('Nhập n nguyên dương.')

dsten=[]
for i in range(n):
    while True:
        ten=input(f'Nhập tên học sinh thứ {i+1}: ')
        if ten=='':
            print('Vui lòng nhập tên.')
        elif ten[0]==' ':
            print('Ký tự đầu không được cách.')
        elif any(k.isdigit() for k in ten):
            print('Tên không chứa số.')
        else:
            dsten.append(ten)
            break
# print(dsten)



#Tìm độ dài lớn nhất
max_len=max(len(ten) for ten in dsten)

#Tìm các tên có độ dài max và vị trí của nó:
ten_dai_nhat=[ten for ten in dsten if len(ten)==max_len]
vi_tri=[i for i,ten in enumerate(dsten) if len(ten)==max_len]

print(f'Tên có độ dài lớn nhất là: {ten_dai_nhat}')
print(f'Vị trí ở: {vi_tri}')
