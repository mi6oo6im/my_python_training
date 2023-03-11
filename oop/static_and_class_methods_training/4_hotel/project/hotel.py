from typing import List
from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests: int = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> [str, None]:
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        response = room.take_room(people)
        if response:
            return response
        self.guests += people

    def free_room(self, room_number: int):
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        people = room.guests
        response = room.free_room()
        if response:
            return response
        self.guests -= people

    def status(self):
        free_rooms = ', '.join(str(r.number) for r in self.rooms if not r.is_taken)
        taken_rooms = ', '.join(str(r.number) for r in self.rooms if r.is_taken)
        return f"""Hotel {self.name} has {self.guests} total guests
Free rooms: {free_rooms}
Taken rooms: {taken_rooms}"""

