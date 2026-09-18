employee_departaments=
[("Иванов": "Продажи",
"Петров": "Маркетинг",
"Сидоров": "Продажи",
"Алексеева": "Разработка",
"Кузнецов": "Маркетинг")]

performance_scores = 
[("Иванов", 85),
("Петров", 92),
("Алексеева", 95),
("Сидоров", 60),
("Кузнецов", 82),]

statistic=dict()

for name, score in performance_scores:
    dep=employee_departaments[name]
    if dep in statistic:
    statistic[dep].append(score)
    else:
    statistic[dep]=[score]
    print(statistic)

    for i in statistic:
        statistic[i]=sum(statistic[i])/len(statistic[i])
        print(statistic)