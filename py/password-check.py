# -*- coding: utf8 -*-
import itertools
import time
import datetime
from progress.bar import Bar, ChargingBar


# посчтитать сколько вариантов подбора есть
	
progress_bar = ChargingBar('Processing', max=1000000)
	
var_count = 0
target = raw_input("Введите слово для подбора: ")
start_time = time.time()
for p in itertools.permutations(target):
	var_count += 1
	progress_bar.next()
progress_bar.finish()
finish_time = time.time() - start_time
print("Количество вариантов: %s" % (var_count))
print("Это значит что чтобы подобрать ваш пароль - нужно перебрать %s вариантов пароля." % (var_count))
print("Это заняло {} {}.".format(finish_time, "секунд"))
