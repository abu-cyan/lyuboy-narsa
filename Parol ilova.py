import time
import subprocess
import turtle

n=input("Parolni kiriting:")

m=[114, 97, 115, 115, 121, 111, 48, 55, 48, 53]
c=[114, 97, 115, 115, 48, 49, 49]

if n=="".join(chr(i) for i in c):
    print("Ochilmoqda...")

    subprocess.Popen([
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"--user-data-dir=C:\Users\Siz\Documents\GizliChrome",
    ])
    
elif n=="".join(chr(i) for i in m):
    print("Ochilmoqda...")

    subprocess.Popen([
    r"C:\Users\user\AppData\Roaming\.minecraft\TLauncher.exe"
    ])
    
else:
    print("PAROL NOTO'G'RI")

    p = ["Parol noto'g'ri","pArol noto'g'ri","paRol noto'g'ri","parOl noto'g'ri","paroL noto'g'ri","parol Noto'g'ri","parol nOto'g'ri","parol noTo'g'ri","parol notO'g'ri","parol noto'G'ri","parol noto'g'Ri","parol noto'g'rI"]
    yr=["white", "red", "green", "blue", "yellow", "orange", "purple", "gray", "pink", "brown", "black", "cyan"]
    fr=["black", "cyan", "magenta", "yellow", "blue", "dodgerblue", "black", "lightgreen", "darkgreen", "turquoise", "white", "red"]

    s=turtle.Screen()
    s.tracer(0)

    t=turtle.Turtle()
    t.hideturtle()
    t.speed(1)
    t.pensize(5)
    t.color("red")
    while True:
        for i in range(12):
            t.clear()
            t.color(yr[i])
            s.bgcolor(fr[i])
            t.write(p[i], align="center", font=("Arial", 40, "bold"))
            s.update()
            time.sleep(0.2)
