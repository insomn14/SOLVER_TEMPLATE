import angr
import claripy
import sys


def main(BIN, FIND, AVOID):
    proj = angr.Project(BIN)

    state = proj.factory.entry_state()

    simgr = proj.factory.simgr(state)

    simgr.explore(
        find=FIND,
        avoid=AVOID
    )

    print(simgr)

    if simgr.found:
        f = simgr.found[-1]
        print(f.posix.dumps(0))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(print(f'Usage {sys.argv[0]} <file_binary> <find_addr> <avoid_addr>'))
    sys.exit(main())

