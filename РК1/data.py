from pack import comp
from pack.comp import comp
from pack.orch import orch
from pack.comp_orch import comp_orch

comps = [
    comp(1,'Лебединая песня', 5.40, 1),
    comp(2, 'Шербурские зонтики', 3.20, 2),
    comp(3, 'Соната №14 "Лунная"', 7.15, 2),
    comp(4, 'Жизнь', 6.28, 1),
    comp(5, 'Тико-Тико', 2.49, 3),
    comp(6, 'Not so far away', 5.28, 4),
    comp(7, 'Ave Maria', 4.43, 3),
    comp(8, 'Токката', 6.06, 1),
    comp(9, 'Тебе одной', 3.56, 5)
]

orchs = [
    orch(1, "Большой симфонический оркестр"),
    orch(2, "Лондонский оркестр"),
    orch(3, "Персимфанс"),
    orch(4, "Филармония"),
    orch(5, "Симфонический оркестр Би-би-си")
]

comps_orchs = [ 
    comp_orch(1,1),
    comp_orch(1,2),
    comp_orch(2,2),
    comp_orch(1,3),
    comp_orch(3,3),
    comp_orch(4,3),
    comp_orch(7,4),
    comp_orch(8,5),
    comp_orch(1,5),
    comp_orch(6,1),
    comp_orch(7,2),
    comp_orch(8,2),
    comp_orch(5,3),
    comp_orch(8,3),
    comp_orch(9,3),
    comp_orch(1,4),
    comp_orch(7,5),
    comp_orch(3,5)
]