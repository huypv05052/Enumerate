#Nhập vào một xâu s. Hãy in ra:
#- Vị trí các chữ số trong xâu.
#- Tổng số chữ số có trong xâu.
#VD: Nhập s = "abc123x4y"
# → Vị trí chữ số: [3, 4, 5, 7]
# → Số lượng chữ số: 4



while True:
    s=input('Nhập xâu s: ')
    if len(s)>0:
        break
    else:
        print('Chưa nhập kí tự cho xâu s.')
print(f'Xâu đã nhập: {s}')
    
vi_tri_so=[]
count=0
tong=0
for i,val in enumerate(s):
    if val.isdigit():
        vi_tri_so.append(i)
        count+=1
        tong+=int(val)
print(f'Vị trí số trong xâu: {vi_tri_so}')
print(f'Có {count} số trong xâu s.')
print(f'Tổng các số trong xâu: {tong}')
