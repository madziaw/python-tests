def is_correct_email(string):
    elements = string.split('@')
    if len(elements) != 2:
        return False
    username, domain = elements
    if len(username) == 0:
        return False
    if '0' <= username[0] <= '9':
        return False
    if '.' not in domain:
        return False
    if len(domain) < 3:
        return False
    if domain[0] =='.' or domain[-1] =='.':
        return False
    return True
