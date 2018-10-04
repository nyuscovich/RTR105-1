#!/usr/bin/python
# -*- coding: utf-8 -*-

a = input("Cien. liet., lūdzu, ievadi skaitli: ")
# 3. python'ā visi input rezultāti ir ar str datu tipu
# tapēc ievadītā lieluma datu tips vēlāk ir jāparveido
a = int(a)

print("Liet., Tu esi iavadījis skaitli: %d"%(a))
aa = a * a
print("Tavs skaitlis kvadrātā ir: %d"%(aa))
