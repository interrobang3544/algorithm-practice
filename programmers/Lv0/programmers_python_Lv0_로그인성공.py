def solution(id_pw, db):
    if id_pw in db:
        return "login"
    for data in db:
        if data[0] == id_pw[0]:
            return "wrong pw"
    return "fail"