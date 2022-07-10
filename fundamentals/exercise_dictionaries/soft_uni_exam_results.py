def add_submission_func(exams: dict, users: dict, user: str, lang: str, score: str):
    current_score = int(score)
    if lang in exams.keys():
        exams[lang] += 1
    else:
        exams[lang] = 1
    if user in users.keys():
        if users[user] < current_score:
            users[user] = current_score
    else:
        users[user] = current_score
    return exams, users


def ban_participant_func(users: dict, user: str):
    if user in users.keys():
        users.pop(user)
    return users


def get_exam_result_func(exams: dict, users: dict):
    return f'Results:\n' + '\n'.join([f'{k} | {v}' for k, v in users.items()]) + \
           '\nSubmissions:\n' + '\n'.join([f'{k} - {v}' for k, v in exams.items()])


exam_submissions = {}
user_submissions = {}

input_line = input()
while input_line != 'exam finished':
    if 'banned' in input_line:
        command = input_line.split('-')
        username = command[0]
        user_submissions = ban_participant_func(user_submissions, username)
    else:
        username, language, points = input_line.split('-')
        exam_submissions, user_submissions = add_submission_func(exam_submissions, user_submissions, username, language,
                                                                 points)
    input_line = input()
print(get_exam_result_func(exam_submissions, user_submissions))
