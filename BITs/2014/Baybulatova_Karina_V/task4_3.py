#Задача 4. Вариант 3.
#Программа, которая которая выводит имя, под которым скрывается Алессандро Филипели. Выводит область интересов, место рождения, годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти). 

#Байбулатова К.В.
#14.03.2016

print("Алессандро Филипепи Боттичелли более известен, как итальянский живописец Сандро Боттичелли")
born=1445
died=1510
age=died-born
place="Италия"
interes="Живопись"
print("Место рождения: " +(place))
print("Год рождения:" +str(born))
print("Возраст:" + str(age))
print("Область интересов:" + interes)


input("\n\n Нажмите Enter для выхода")