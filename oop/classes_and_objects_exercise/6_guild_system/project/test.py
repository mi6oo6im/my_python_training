from project.guild import Guild
from project.player import Player

guild = Guild("GGXrd")
player = Player("Pesho", 90, 90)
print(guild.assign_player(player))
print(guild.assign_player(player))

print(guild.kick_player('Pesho'))
print(guild.kick_player('Pesho'))