from project.band_members.musician import Musician


class Singer(Musician):
    @property
    def available_skills(self):
        return [
            "sing high pitch notes",
            "sing low pitch notes",
            ]
