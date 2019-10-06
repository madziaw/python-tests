def log_in(name,surname,password):
    if name and surname and name==name.title() and surname==surname.title() and len(password)>=8:
        return True
    else:
        return False
