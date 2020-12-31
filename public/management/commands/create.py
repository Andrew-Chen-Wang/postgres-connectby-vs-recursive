from timeit import default_timer
import os
import random
import time

from django.db import connection
from django.core.management.base import BaseCommand

from public.models import Tree


class Command(BaseCommand):
    help = (
        "Generates test data of a tree hierarchy"
    )
    requires_migrations_checks = True

    def handle(self, *args, **options):
        if Tree.objects.count() > 0:
            Tree.objects.all().delete()
        random.seed("I wish I could just add something like 1984 to this"
                    " seed but I can't because I'm an absolute moron."
                    " But let the story continue on and on again", version=2)
        # We're just gonna test a single parent node
        initial = Tree.objects.create()
        objs = [Tree.objects.first()]
        start = default_timer()
        t_end = time.time() + 60 * 2  # 2 minutes
        while objs or time.time() < t_end:
            # Decide if this has children
            if bool(random.getrandbits(1)) or objs[0].parent is None:
                # Now figure out how many
                for _ in range(random.randint(0, 5)):
                    objs.append(Tree.objects.create(parent=objs[0]))
            objs.pop(0)
        end = default_timer()
        print(f"It took {end - start} seconds to create the objects.")
        num_trees = Tree.objects.filter(parent__isnull=False).count()
        print("Number of children:", num_trees)
        # Create random trees to make sure the numbers are correct
        Tree.objects.create()
        _a = Tree.objects.create()
        _b = Tree.objects.create(parent=_a)
        Tree.objects.create(parent=_b)
        Tree.objects.create(parent=_a)

        print("Beginning test with connectby")
        start = default_timer()
        # Should be the correct number 732951 as of my stoppage point
        # from data generation
        # with connection.cursor() as c:
        #     c.execute("""
        #     """)
        #     count = c.fetchone()[0]
        # assert count == num_trees
        end = default_timer()
        print(f"It took {end - start} seconds.")

        print("Beginning test with WITH RECURSIVE")
        start = default_timer()
        with connection.cursor() as c:
            c.execute("""
            WITH RECURSIVE cte AS (
               SELECT id, parent_id
               FROM   public_tree
               WHERE  id = %s
            
               UNION ALL
               SELECT t.id, c.id
               FROM public_tree t, cte c
               WHERE t.parent_id = c.id
            )
            SELECT COUNT(*) - 1
            FROM cte
            """, (initial.id,))
            count = c.fetchone()[0]
        assert count == num_trees
        end = default_timer()
        print(f"It took {end - start} seconds.")




"""
SELECT COUNT(*) FROM 
    connectby('public_tree', 'id', 'parent_id', '0', 95128, '~')
    AS t(id numeric, parent_id numeric, level int, branch text);
"""
