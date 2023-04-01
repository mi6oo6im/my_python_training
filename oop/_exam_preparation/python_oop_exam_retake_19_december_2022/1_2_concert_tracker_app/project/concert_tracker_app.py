from typing import List
from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    @property
    def valid_musician_types(self):
        return {
            "Guitarist": Guitarist,
            "Drummer": Drummer,
            "Singer": Singer,
        }

    @property
    def required_skills_per_genre(self):
        return {
            "Metal": {
                "Guitarist": ["play metal"],
                "Drummer": ["play the drums with drumsticks"],
                "Singer": ["sing low pitch notes"],
            },
            "Rock": {
                "Guitarist": ["play rock"],
                "Drummer": ["play the drums with drumsticks"],
                "Singer": ["sing high pitch notes"],
            },
            "Jazz": {
                "Guitarist": ["play jazz"],
                "Drummer": ["play the drums with drum brushes"],
                "Singer": ["sing high pitch notes", "sing low pitch notes"],
            }
        }

    def create_musician(self, musician_type: str, name: str, age: int) -> str:
        try:
            musician = self.valid_musician_types[musician_type]
        except KeyError:
            raise ValueError("Invalid musician type!")

        same_name_musicians = [m for m in self.musicians if m.name == name]
        if same_name_musicians:
            raise Exception(f"{name} is already a musician!")

        self.musicians.append(musician(name, age))
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str) -> str:
        same_name_bands = [b for b in self.bands if b.name == name]
        if same_name_bands:
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str) -> str:
        same_place_concert = [c for c in self.concerts if c.place == place]
        if same_place_concert:
            raise Exception(f"{place} is already registered for {same_place_concert[0].genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str) -> str:
        try:
            musician = next(filter(lambda m: m.name == musician_name, self.musicians))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a musician!")

        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str) -> str:
        try:
            band = next(filter(lambda b: b.name == band_name, self.bands))
        except StopIteration:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = next(filter(lambda m: m.name == musician_name, band.members))
        except StopIteration:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str) -> str:
        band = next(filter(lambda b: b.name == band_name, self.bands))
        concert = next(filter(lambda c: c.place == concert_place, self.concerts))

        for musician_type in self.valid_musician_types.values():
            if any([isinstance(m, musician_type) for m in band.members]):
                continue
            # if none of the members is of the musician type -> raise exception
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        for musician in band.members:
            musician_type = musician.__class__.__name__
            skills_required = self.required_skills_per_genre[concert.genre][musician_type]
            skills = musician.skills
            if set(skills_required).issubset(set(skills)):
                continue
            # if one or more of the skills is missing -> raise exception
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."

