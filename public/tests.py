from django.db.models.aggregates import Count
from django.test import TestCase

from public.models import Tree, ASD1, ASD2


class TestBlah(TestCase):
    def test_get_descendents(self):
        objs = Tree.objects.bulk_create([Tree() for _ in range(3)])
        for i, x in enumerate(objs):
            more = [ASD1.objects.create(parent=x) for _ in range(i)]
            for blah in more:
                ASD2.objects.create(parent=blah)
        queried = Tree.objects\
            .annotate(asd=Count("asd1") + Count("asd1__asd2"))\
            .order_by("id")
        print([x.asd for x in queried])
