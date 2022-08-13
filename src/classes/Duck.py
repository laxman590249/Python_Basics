

class Duck:

    def fly(self):
        print('Flying')


class NonDuck:
    pass


class Other:

    def migration(self, duck: Duck) -> None:
        duck.fly()
        print('Migration Happening')


other = Other()
duck = Duck()
non_duck = NonDuck()

other.migration(duck)
other.migration(non_duck)

