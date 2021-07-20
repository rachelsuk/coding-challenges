"""Count employees in an org chart.

Our organization has the following org chart::

                    Jane
          Jessica          Janet
       Al  Bob  Jen     Nick  Nora
                                Henri

Let's make this chart::

    >>> henri = Node("Henri")
    >>> nora = Node("Nora", [henri])
    >>> nick = Node("Nick")
    >>> janet = Node("Janet", [nick, nora])
    >>> al = Node("Al")
    >>> bob = Node("Bob")
    >>> jen = Node("Jen")
    >>> jessica = Node("Jessica", [al, bob, jen])
    >>> jane = Node("Jane", [jessica, janet])

And test our counting function::

    >>> henri.count_employees()
    0

    >>> nora.count_employees()
    1

    >>> jane.count_employees()
    8


"""


class Node(object):
    """Node in a tree."""

    def __init__(self, name, children=None):
        self.name = name
        self.children = children or []

    def __str__(self):
        return f'{self.name}'

    def count_employees(self):
        """Return a count of how many employees this person manages.

        Return a count of how many people that manager manages. This should
        include *everyone* under them, not just people who directly report to
        them.
        """
        to_visit = []
        to_visit.extend(self.children)
        emp_count = len(self.children)
        #to_visit = [al, Bob, Jen]
        #emp_count = 8
        while to_visit:
            current = to_visit.pop()
            #current = jessica
            to_visit.extend(current.children)
            emp_count += len(current.children)

        return emp_count


henri = Node("Henri")
nora = Node("Nora", [henri])
nick = Node("Nick")
janet = Node("Janet", [nick, nora])
al = Node("Al")
bob = Node("Bob")
jen = Node("Jen")
jessica = Node("Jessica", [al, bob, jen])
jane = Node("Jane", [jessica, janet])
print(henri.count_employees())
print(nora.count_employees())
print(jane.count_employees())


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU ARE A TREE GENIUS!\n")
