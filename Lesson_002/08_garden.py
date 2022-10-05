#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
garden_set = set(garden)
meadow_set = set(meadow)
flowers_set = garden_set.union(meadow_set)

# выведите на консоль все виды цветов

print(flowers_set)

# выведите на консоль те, которые растут и там и там

flowers_both = garden_set.intersection(meadow_set)
print(flowers_both)

# выведите на консоль те, которые растут в саду, но не растут на лугу

flowers_garden = garden_set.difference(meadow_set)
print(flowers_garden)

# выведите на консоль те, которые растут на лугу, но не растут в саду

flowers_meadow = meadow_set.difference(garden_set)
print(flowers_meadow)


