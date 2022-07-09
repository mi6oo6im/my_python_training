command_line = input()
company_dict = {}
while command_line != 'End':
    company, employee_id = command_line.split(' -> ')
    if company not in company_dict.keys():
        company_dict[company] = [employee_id]
    elif employee_id not in company_dict[company]:
        company_dict[company].append(employee_id)
    command_line = input()
res = '\n'.join([f'{k}\n'+'\n'.join([f'-- {eid}' for eid in v]) for k, v in company_dict.items()])
print(res)
