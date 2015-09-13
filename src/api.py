def get_token(token_id):
    return {
        'token_id': token_id,
        'title': "Thing %d" % token_id,
        'yes_effect': 6,
        'no_effect': -5,
    }

def get_question(question_id):
    return {
        'question_id': question_id,
        'text': 'what about thing %s?' % question_id,
        'tokens': map(get_token, [3,6,7]),
        'unset_tokens': map(get_token, [4,5]),
        'has_unset_tokens': True
    }

def get_game():
    return {
        'questions': map(get_question, [3,4,5]),
        'all_tokens': map(get_token, [3,4,5,6,7])
    }