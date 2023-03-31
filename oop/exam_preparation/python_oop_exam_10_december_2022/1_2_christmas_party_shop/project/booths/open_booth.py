from project.booths.booth import Booth


class OpenBooth(Booth):
    @property
    def price_per_person(self):
        return 2.50
