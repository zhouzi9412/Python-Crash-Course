####收集，存储和组织大量的输入，供以后查看和显示####

#首先，创建一个待验证的用户列表#
#和一个用于存储已验证用户的列表#
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
#验证每个用户，直到没有未验证的用户为止#
#将每个经过验证的列表都移到已验证用户列表中#
while unconfirmed_users:
    current_user = unconfirmed_users.pop()                      #pop()每次循环从末尾删除未验证的用户
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)                    #append()加到列表confirmed_user中
#显示所有已验证的用户
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
