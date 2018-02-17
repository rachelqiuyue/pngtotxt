from PIL import Image
def changeGrey(r,g,b,alpha = 256):
    askii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    if alpha == 0:
        return ' ' 
    l = len(askii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0+1) / l
    return askii_char[int(gray/unit)]
    
def main():
    img = Image.open('wm.png','r')
    height = img.size[0]
    width = img.size[1]
    img = img.resize((height,width), Image.NEAREST)
    txt = ''
    for i in range(height):
        for j in range(width):
            p =img.getpixel((j,i))
            al = img.split()[-1]
            txt += changeGrey(p[0],p[1],p[2],al)
        txt += '\n'
    f = open('gray.txt','w')
    print(txt, file = f)
    f.close()
        
            
main()
    