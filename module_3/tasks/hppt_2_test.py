from module_3.tasks.http_2 import parse_hosts

test = "<a href=\"http://stepic.org/courses\"> " \
       "<a href='https://stepic.org'>" \
       "<a href='http://neerc.ifmo.ru:1345'>" \
       "<a href=\"ftp://mail.ru/distib\" >" \
       "<a href=\"ya.ru\">" \
       "<a href=\"www.ya.ru\">" \
       "<a href=\"../skip_relative_links\">"

test1 = "<a href=\"http://stepic.org/courses\"> " \
       "<a href='https://stepic.org1'>"

hosts = parse_hosts(test)
print("\n".join(sorted(hosts)))