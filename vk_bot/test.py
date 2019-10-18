import mods
modules = []
for test in mods.modules:
    modules.append(test(4))
t = modules[0]
t = t.main()
print(t)
