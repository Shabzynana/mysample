from puppycompanyblog.models import db,User

sam = User.query.all()
for am in sam:

    print(am.email)
    print(am.username)
    print(am.password_hash)
    print('')
