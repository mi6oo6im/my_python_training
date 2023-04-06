from typing import List
from project.jockey import Jockey
from project.horse_race import HorseRace
from project.horse_specification.horse import Horse
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class HorseRaceApp:

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    @property
    def valid_horse_types(self):
        return {
            "Appaloosa": Appaloosa,
            "Thoroughbred": Thoroughbred,
        }

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in ["Appaloosa", "Thoroughbred"]:
            return
        same_name_horses = [h for h in self.horses if h.name == horse_name]
        if same_name_horses:
            raise Exception(f"Horse {horse_name} has been already added!")

        try:
            horse = self.valid_horse_types[horse_type]
            new_horse = horse(horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."
        except KeyError:
            return

    def add_jockey(self, jockey_name: str, age: int):
        same_name_jockey = [j for j in self.jockeys if j.name == jockey_name]
        if same_name_jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        same_type_races = [r for r in self.horse_races if r.race_type == race_type]
        if same_type_races:
            raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        available_horses_of_horse_type = [h for h in self.horses if h.__class__.__name__ == horse_type and not h.is_taken]
        try:
            horse = available_horses_of_horse_type.pop()
        except IndexError:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        try:
            race = next(filter(lambda r: r.race_type, self.horse_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        try:
            race = next(filter(lambda r: r.race_type, self.horse_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        wining_speed = max(j.horse.speed for j in race.jockeys)
        winner = next(filter(lambda j: j.horse.speed == wining_speed, race.jockeys))

        return f"The winner of the {race_type} race, with a speed of {wining_speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."
