import angr
import claripy

def main():
    MSGS = b'SUCCESS'
    p = angr.Project('a.out')

    flag_chars = [claripy.BVS('flag_%d'%i,8) for i in range(0x10)]
    flag = claripy.Concat(*flag_chars + [claripy.BVS(b'\n', 8)])

    st = p.factory.full_init_state(
        args=['./a.out'],
        add_options=angr.options.unicorn,
        stdin=flag,
    )

    for k in flag_chars:
        st.solver.add(k != 0)
        st.solver.add(k >= ord('!'))
        st.solver.add(k <= ord('~'))

    sm = p.factory.simulation_manager(st)
    sm.explore(find=lambda s: MSGS in s.posix.dumps(1))
    s = sm.found[0]
    result = s.posix.dumps(0)
    return result

if __name__ == '__main__':
    print(main())
