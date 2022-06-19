pokemons_list = list(map(int, input().split()))
total_pokemon_score = 0
while len(pokemons_list) > 0:
    pokemon_index = int(input())
    if pokemon_index < 0:
        captured_pokemon = pokemons_list[0]
        pokemons_list.pop(0)
        pokemons_list.insert(0, pokemons_list[-1])
    elif pokemon_index >= len(pokemons_list):
        captured_pokemon = pokemons_list[-1]
        pokemons_list.insert(-1, pokemons_list[0])
        pokemons_list.pop(-1)
    else:
        captured_pokemon = pokemons_list.pop(pokemon_index)
    total_pokemon_score += captured_pokemon
    new_pokemons_list = [x + captured_pokemon if x <= captured_pokemon else x - captured_pokemon for x in pokemons_list]
    pokemons_list = new_pokemons_list
print(total_pokemon_score)
