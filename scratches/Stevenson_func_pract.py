length = 14
width = 5
pic1 = '@'
pic2 = '*'

def drawbox(length,width,pic1,pic2):
    print(length * pic1 )
    for i in range (width - 2):
        print(pic1 + (pic2 * (length - 2)) + pic1)
    print(length * pic1)

drawbox(length,width,pic1,pic2)