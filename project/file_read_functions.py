def read_input(input_path, score_path):
    if type(input_path) != str or type(score_path) != str:
        raise TypeError('input paths should have type str')
    path_pairs = []
    with open(input_path, 'r', encoding='utf-8') as file:
        line = file.readline()
        while line:
            path_pairs.append(line.rstrip().split())
            line = file.readline()
    return path_pairs, score_path


def read_code(path):
    if type(path) != str:
        raise TypeError('input path should have type str')
    with open(path, 'r', encoding='utf-8') as file:
        code = file.read()
    return code

