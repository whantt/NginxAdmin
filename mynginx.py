import nginx

c = nginx.loadf("modules.conf")
u=c.filter(btype="server",name="prodadmin.niubangold.com")
if len(u):
    c.remove(u[0])

# a=nginx.Upstream('act.niubangold.com',nginx.Key('server', 'aaaaaa'))
# for i in  c.filter(btype="Upstream",name="act.niubangold.com")[0].keys:
#     print i.as_list
# u=c.filter(btype="Upstream",name="act.niubangold.com")[0]
# u.add(nginx.Key('server', '999999999:8080'))

# if u[0]:
#     c.remove(u)


print u

# u2=nginx.Upstream('act.niubangold.com',nginx.Key('server', '111111111:8080'))
# c.add(u2)
# # print c.filter(btype="Upstream",name="act.niubangold.com")[0].keys
# nginx.dumpf(c, 'modules.conf')