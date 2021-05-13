import angr

FILE = ''
MSGS = b''

proj = angr.Project(FILE)
state = proj.factory.entry_state()
simgr = proj.factory.simulation_manager(state)
simgr.explore(find=lambda s: MSGS in s.posix.dumps(1))
s = simgr.found[0]
#print(s.posix.dumps(1))
result = s.posix.dumps(0)
print(result)
