import json

def load_candidates_from_json():
    '''
    :return: возвращает список всех кандидатов
    '''
    with open("candidates.json", 'r', encoding='utf-8') as file:
        return json.load(file)


def get_candidate(candidate_id):
    '''
    :param candidate_id:
    :return: возвращает одного кандидата по его id
    '''
    for candidate in load_candidates_from_json():
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    '''
    :param candidate_name:
    :return: возвращает кандидатов по имени
    '''
    result = []
    for candidate in load_candidates_from_json():
        if candidate["name"] == candidate_name:
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name):
    '''
    :param skill_name:
    :return: возвращает кандидатов по навыку
    '''
    result = []
    for candidate in load_candidates_from_json():
        if skill_name in candidate["skills"].lower().split(', '):
            result.append(candidate)
    return result

