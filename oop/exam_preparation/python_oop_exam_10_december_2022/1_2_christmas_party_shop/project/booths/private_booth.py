from project.booths.booth import Booth


class PrivateBooth(Booth):
    @property
    def price_per_person(self):
        return 3.50
