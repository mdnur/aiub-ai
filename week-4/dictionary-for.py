users = {'hans':'active','eleonore':'inactive','mdnur':'active'}


for user,status in users().copy().items():
    if status =='inactive':
        print("print")