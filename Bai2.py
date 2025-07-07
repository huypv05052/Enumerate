#Nhập vào một xâu s. In ra từng ký tự trong xâu kèm với chỉ số của nó theo dạng:
# Ký tự tại vị trí 0: h  
# Ký tự tại vị trí 1: e  
# Ký tự tại vị trí 2: l  
# ...



while True:
    s=input('Nhập xâu s: ')
    if len(s)>0:
        break
    else:
        print('Chưa nhập kí tự cho xâu.')
    
for i,val in enumerate(s):
    print(f'Ký tự tại vị trí {i+1}: {val}')
