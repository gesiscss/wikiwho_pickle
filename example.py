from wikiwho import open_pickle

obj = open_pickle(6187, lang='en')

# local query
all_content = obj.get_all_content(['o_rev_id', 'editor', 'token_id', 'in', 'out', 0])