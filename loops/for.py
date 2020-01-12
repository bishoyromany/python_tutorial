x = ['text' , 1 , 2 , 3]

for i in x:
    print(i)
    if isinstance(i , str):
        for y in i:
            print(y)
        print('End Text Loop')
print('FInished First Loop')

# loop with range(start , end , num between)
for f in range(0 , 100 , 1):
    if f % 2 == 0:
        # continue ignore this one only
        continue
    # break means stop
    if f % 49 == 0:
        break

    # pass means no code ignore it
    if f % 3 != 0:
        pass
    elif(f % 3 == 0):
        print('Wooha Pass Worked With '+str(f))
    print(f)