import matplotlib.pyplot as plt
import numpy as np

def fonksiyon_cizdir():
    # Kullanıcıdan alınacak fonksiyon inputu
    fonksiyon = input("Çizmek istediğiniz fonksiyonu girin (örn. 'x**2', 'np.sin(x)'): ")

    # x değerlerinin aralığı ve hassasiyeti
    x = np.linspace(-10, 10, 400)
    
    y = eval(fonksiyon)

    # Fonksiyonun grafiğini çizme
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'f(x) = {fonksiyon}')
    plt.title("Matematiksel Fonksiyon Grafiği")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    fonksiyon_cizdir()
