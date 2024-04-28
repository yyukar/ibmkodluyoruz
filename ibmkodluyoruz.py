import math

def euclideanDistance(point1, point2):
    # İki nokta arasındaki Öklid mesafesini hesaplar.
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Güncellenmiş noktalar
points = [(2, 1), (2, 4), (1, 1)]

# Her nokta çifti arasındaki Öklid mesafesini hesaplayıp bu mesafeleri bir listede saklar.
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

# Hesaplanan mesafelerden en küçüğünü bulur ve yazdırır.
min_distance = min(distances)
print("Minimum Öklid mesafesi:", min_distance)