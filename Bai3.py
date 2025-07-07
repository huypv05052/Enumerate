#Cho một danh sách các số nguyên lst. Tính tổng các phần tử nằm ở vị trí chẵn (0, 2, 4, …).
# VD: lst = [5, 10, 15, 20, 25]
# Tổng = 5 + 15 + 25 = 45



def evenSumLst():
    while True:
        try:
            n=int(input('n='))
            if n>0: 
                break
            else:
                print('Nhập n nguyên dương.')
        except ValueError:
            print('Nhập n nguyên dương.')
    

    lst=[]
    for i in range(n):
        while True:
            try:
                num=int(input(f'Nhập giá trị thứ {i+1}: '))
                lst.append(num)
                break
            except ValueError:
                print('Nhập số nguyên.')
    print(f'Danh sách số nguyên đã nhập: {lst}')

    #Tính tổng các số ở vị trí chẵn
    evenSum=0
    oddSum=0
    for i,val in enumerate(lst):
        if i%2==0:
            evenSum+=val
        else:
            oddSum+=val
    print(f'Tổng các số ở vị trí chẵn là: {evenSum}')
    print(f'Tổng các số ở vị trí lẻ là: {oddSum}')
evenSumLst()
