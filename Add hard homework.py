grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
order_students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

st = sorted(order_students) #сортировка студентов в алфавитном порядке

grade1 = grades[0] # вытаскиваем оценки 1-го студента
gr1 = sum(grade1) / len(grade1) # средний балл 1-го ученика

grade2 = grades[1] # вытаскиваем оценки 2-го студента
gr2 = sum(grade2) / len(grade2) # средний балл 2-го ученика

grade3 = grades[2] # вытаскиваем оценки 3-го студента
gr3 = sum(grade3) / len(grade3) # средний балл 3-го ученика

grade4 = grades[3] # вытаскиваем оценки 4-го студента
gr4 = sum(grade4) / len(grade4) # средний балл 4-го ученика

grade5 = grades[4] # вытаскиваем оценки 5-го студента
gr5 = sum(grade5) / len(grade5) # средний балл 5-го ученика

order_grades = (gr1, gr2, gr3, gr4, gr5)

direction = {
    st[0] : gr1,
             st[1] : gr2,
                      st[2]: gr3,
                               st[3]: gr4,
                                        st[4]: gr5
}
print(direction)
