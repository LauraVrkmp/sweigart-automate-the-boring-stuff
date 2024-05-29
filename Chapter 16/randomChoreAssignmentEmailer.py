import random, sys, smtplib
from copy import deepcopy

people = ['ashley@example.com', 'bob@example.com', 'charlie@example.com', 
          'david@example.com']
people_names = ['Ashley', 'Bob', 'Charlie', 'David']
chores_done = [[] for i in range(len(people))]

for i in range(10):
    chores = ['dishes', 'bathroom', 'vacuum', 'walk dog', 'fold clothes', 'washer']
    for j in range(len(people)):
        chores_not_seen = deepcopy(chores)
        for k in range(len(chores)):
            randomChore = random.choice(chores_not_seen)
            if chores_done[j] != []:
                if randomChore == chores_done[j][-1]:
                    chores_not_seen.remove(randomChore)
                    k -= 1
                    continue
                if chores_not_seen == []:
                    print('No more chores available!')
                    sys.exit()
                chores_done[j].append(randomChore)
                chores.remove(randomChore)
                break
            else:
                chores_done[j].append(randomChore)
                chores.remove(randomChore)
                break

smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('laura.veerkamp@hotmail.com', sys.argv[1])

for i in range(len(people)):
    body = "Subject: %s, your chore for this week.\n\nDear %s,\n\n\
    \b\b\bYour chore for this week is %s. Please be dutifull." % (people_names[i], 
                                                            people_names[i], 
                                                            chores_done[i][-1])
    print(body)
    print('Sending email to %s...' % people[i])
    sendmailStatus = smtpObj.sendmail('laura.veerkamp@hotmail.com', people[i], body)

    if sendmailStatus != {}:
        print('There was a problem sending email to %s: %s' % (people_names[i],
                                                               sendmailStatus))
smtpObj.quit()

# j = 0
# for i in range(len(chores_done[j])):
#     group_test = []
#     for j in range(len(chores_done)):
#         if chores_done[j][i] in group_test:
#             print('Group test failed')
#             break
#         group_test.append(chores_done[j][i])
#     print(group_test)
#     print('Group test passed')

# for i in range(len(chores_done)):
#     for j in range(len(chores_done[i]) - 1):
#         if chores_done[i][j] == chores_done[i][j + 1]:
#             print('Sequence test failed')
#             break
#     print(chores_done[i])
#     print('Sequence test passed')