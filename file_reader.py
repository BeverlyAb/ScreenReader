def read_token(id_name):
    token_dict = {}
    lines = []
    with open("token.txt") as f:
        lines = f.readlines()


    for i in range(len(lines)):
        id, val = lines[i].split()
        token_dict[id.strip()] = val.strip()
    return token_dict[id_name]
