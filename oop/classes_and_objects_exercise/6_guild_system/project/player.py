from typing import Dict


class Player:
    NOT_PART_OF_GUILD_WORD = 'Unaffiliated'

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str: int] = {}
        self.guild = Player.NOT_PART_OF_GUILD_WORD

    def add_skill(self, skill_name: str, mana_cost: int) -> str:
        if skill_name in self.skills:
            return "Skill already added"

        self.skills[skill_name] = mana_cost

        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self) -> str:
        skills = '\n'.join([f'==={k} - {v}' for k, v in self.skills.items()])
        return f'Name: {self.name}\n' \
               f'Guild: {self.guild}\n' \
               f'HP: {self.hp}\n' \
               f'MP: {self.mp}\n' + skills


# john = Player('John', 30, 39)
# john.add_skill('jump', 32)
# john.add_skill('crawl', 4)
# print(john.player_info())
