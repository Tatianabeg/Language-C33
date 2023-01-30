#1. Случайная непрерывная величина A имеет равномерное распределение на промежутке  (200, 800].
#Найдите ее среднее значение и дисперсию.

def mean_and_variance(a,b):
    return f'На промежутке ({a};{b}]\nСреднее значение: М(А) = {(a+b)/2: .2f}\nДисперсия: D(A) = {((b-a)**2)/12: .2f}'
print(mean_and_variance(200,800))

#2. О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2. 
# Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5? 
#Если да, найдите ее.

b=0.5+2.4**(1/2)
print(f'Левая граница распределения величины В - b = {b: .3f}\n'
      f'Среднее значение В на промежутке (0.5; {b: .3f}) M(B) = {(b+0.5)/2: .3f}'     
     )




 
