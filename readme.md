# 🧩 Feladat: Egyedi betűk gyűjtése

Írj egy `egyedi_betuk(szoveg)` nevű függvényt, amely egy tetszőleges szöveget kap paraméterként,  
és visszaadja a szövegben található **betűket (a–z, A–Z)** egyszer, **ábécé sorrendben**, **kisbetűs formában**.

A nem betű karaktereket (szám, írásjel, szóköz stb.) figyelmen kívül kell hagyni.

---

## 🔍 Elvárások

- A függvény **while ciklus** és **elágazások** segítségével oldd meg. 
- A függvény ne írjon ki semmit, hanem **visszatérési értékként** adja vissza a listát.  
- Minden betű **csak egyszer** szerepeljen az eredményben.  
- Az eredmény **ábécé sorrendben** legyen rendezve. A rendezéshez használhatod a sort függvényt.  

---

## ✳️ Példák

```python
>>> egyedi_betuk("Hello, Világ!")
['a', 'e', 'g', 'h', 'i', 'l', 'o', 'v']

>>> egyedi_betuk("Python 3.12")
['h', 'n', 'o', 'p', 't', 'y']

>>> egyedi_betuk("Árvíztűrő tükörfúrógép")
['a', 'e', 'f', 'g', 'k', 'o', 'p', 'r', 't', 'u', 'v', 'z']
