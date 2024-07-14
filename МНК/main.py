import numpy as np
import matplotlib.pyplot as plt

N = 100 #Число эксперементов
sigma = 3 #стандартное отклонение данных выборки
k = .5 #теоретическое значение параметра k
b = 2 #теоретическое знач. параметра b

x=np.array(range(N)) # Одномерный массив значения x

# Формируем теоретическую кривую(через функицю генератор)
func = np.array([k*z+b for z in range(N)])

# Сформируем данные выборки(эксперементальные)
y = func + np.random.normal(0, sigma, N) # рандомные точки распределенные по Гауссевскому закону

#Вычисление кавчества отклонений по методу МНК
mx = x.sum()/N
my = y.sum()/N
alpha2=np.dot(x.T, x)/N #Воторой начальный момент альфа2
a11=np.dot(x.T, y)/N

kk=(a11 - mx*my)/(alpha2 - mx**2) #вычисление оценки для k
bb=my-kk**mx #вычисление оценки для b

ff=np.array([kk*z+bb for z in range(N)])

# Отображение графика
plt.plot(func)
plt.plot(ff, c='yellow')
plt.scatter(x, y, s=2, c='red')
plt.grid(True)
plt.show()
