














from puppycompanyblog.models import db,User

sam = User.query.all()
#for am in sam:

print('')
print ("{:<12} {:<27} {:<15} {:<70} ".format('id','email','username','pass_confirm'))
print('----------------------------------------------------------------------------------------------------------------------')
print('')
for am in sam:

    print ("{:<12} {:<27} {:<15} {:<70}".format(am.id,am.email,am.username,am.password_hash))
    print('')





    #print(am.email)
    #print(am.username)
    #print(am.password_hash)
    #print('')
