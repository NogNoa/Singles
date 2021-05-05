max_gen = 10


class noble:
    def __init__(self, father, gen, land=0, king=False):
        self.father = father
        self.land = land
        self.gen = gen
        self.king = king
        self.senior, self.junior = None, None
        if self.father.king:
            self.king = True

    def beget(self):
        self.senior = noble(self, self.gen + 1)
        self.junior = noble(self, self.gen + 1)

    def leave(self):
        if self.king:
            self.senior.land = self.land / 2
            self.junior.land = self.land / 2
        else:
            self.senior.land = self.land / 3
            self.junior.land = self.land / 3

    def third_inheritence(self, inh):
        if self.father.junior is self:
            self.father.senior.land += inh
        else:
            self.father.third_inheritence(inh)


# todo: we want a callable (not init-time) for making another generation and callculating it's land.
