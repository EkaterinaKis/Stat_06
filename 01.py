from scipy import stats
import numpy as np

# # 1. Известно, что генеральная совокупность распределена нормально со средним
# # квадратическим отклонением, равным 16.Найти доверительный интервал для
# # оценки математического ожидания a с надежностью 0.95, если выборочная
# # средняя M = 80, а объем выборки n = 256.

# M = 80
# n = 256
# sigma = 16

# t = stats.t.ppf(0.975,255)

# result = [M-t*(sigma/(n**0.5)), M+t*(sigma/(n**0.5))]
# print("Доверительный интервал:",result)


# # 2. В результате 10 независимых измерений некоторой величины X,
# # выполненных с одинаковой точностью, получены опытные данные:
# # 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1
# # Предполагая, что результаты измерений подчинены нормальному закону
# # распределения вероятностей, оценить истинное значение величины X при помощи
# # доверительного интервала, покрывающего это значение
# # с доверительной вероятностью 0,95.


# array = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
# n = len(array)

# mean = np.mean(array)

# newarray = []

# for i in range(len(array)):
#     newarray.append((array[i]-mean)**2)

# sum = 0
# for i in range(len(newarray)):
#     sum = sum + newarray[i]
# D = sum/n

# S = ((n/(n-1))*D)**0.5
# t = stats.t.ppf(0.975,9)

# result = [mean-(t*S)/(n**0.5), mean+(t*S)/(n**0.5)]
# print("С 95% вероятностью истинное значение находится в интервале:",result)

# # 3. Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170
# # Рост матерей  178, 165, 165, 173, 168, 155, 160, 164, 178, 175
# # Используя эти данные построить 95% доверительный интервал
# # для разности среднего роста родителей и детей.

# daughters = [175, 167, 154, 174, 178, 148, 160, 167, 169, 170]

# mean1 = np.mean(daughters)

# n = len(daughters)

# newdaughters = []

# for i in range(len(daughters)):
#     newdaughters.append((daughters[i]-mean1)**2)

# sum = 0
# for i in range(len(newdaughters)):
#     sum = sum + newdaughters[i]
# D1 = sum/n

# S1 = ((n/(n-1))*D1)**0.5

# mothers = [178, 165, 165, 173, 168, 155, 160, 164, 178, 175]

# mean2 = np.mean(mothers)

# m = len(mothers)

# newmothers = []

# for i in range(len(mothers)):
#     newmothers.append((mothers[i]-mean2)**2)

# sum = 0
# for i in range(len(newmothers)):
#     sum = sum + newmothers[i]
# D2 = sum/m

# S2 = ((m/(m-1))*D2)**0.5


# delta = mean2-mean1

# t = stats.t.ppf(0.975,18)

# D = (S1**2+S2**2)/2

# S = (D*(1/n+1/m))**0.5

# result = [delta-t*S, delta+t*S]
# print("95% доверительный интервал для разности среднего роста родителей и детей:",result)