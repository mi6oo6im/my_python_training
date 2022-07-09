from collections import defaultdict

legendary_dict = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
junk_value = defaultdict(list)
obtained = False
while not obtained:
    key_value_list = input().split()
    for i in range(0, len(key_value_list), 2):
        value = int(key_value_list[i])
        junk = key_value_list[i + 1].lower()
        junk_value[junk].append(value)
        for k, v in junk_value.items():
            if sum(v) >= 250 and k in legendary_dict:
                print(f'{legendary_dict.get(k)} obtained!')
                junk_value[k].append(-250)
                print(f"""shards: {sum(junk_value['shards'])}
fragments: {sum(junk_value['fragments'])}
motes: {sum(junk_value['motes'])}""")
                print('\n'.join([f'{key}: {sum(val)}' for key, val in junk_value.items() if key not in legendary_dict]))
                obtained = True
                break
        if obtained:
            break
