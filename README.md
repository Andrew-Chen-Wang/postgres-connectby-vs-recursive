# Base Django Test

By: Andrew Chen Wang

Edit (30 Dec 2020): I like can't figure out
how connectby works since it's an Oracle thing,
so I guess I'm sticking to my good pal recursive...

Just testing counting of children from
a single node. Need to compare speed with
`connectby` and `with recursive` on Postgres.

The creation of test data is using Python's
PRNG and a happy message of a seed (using v2
you can use a string to specify a seed value
that's actually a string).

---
Usage:

```shell
python manage.py create
```

---

### License

Licensed under the MIT License