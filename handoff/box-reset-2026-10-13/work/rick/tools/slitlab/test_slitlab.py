import slitlab as S
def test_1(): r=S.i1_double_slit(); assert r['V_coherent']>0.99 and r['V_whichpath']<0.01
def test_2(): assert S.i2_phase_knob()['dot_rel_err_mean']<0.02
def test_3(): t=S.i3_grover()['table'][-1]; assert t['p_success']>0.99 and t['grover_queries']<t['N']/50
def test_4(): r=S.i4_mzi_gates(); assert r['NOT'] and r['XOR'] and r['AND'] and r['OR'] and r['phase_tolerance_rad']>0.3
def test_5(): r=S.i5_nosignal(); assert r['max_dev']<1e-12 and r['MI_bits_sampled']<1e-3
def test_6(): assert all(abs(x['peak_to_N2']-1)<1e-3 for x in S.i6_grating()['table'])
def test_7(): r=S.i7_optimizer()['hit_rate_by_evals']['100']; assert abs(r['optical_hit']-r['random_hit'])<0.1
def test_8(): t=S.i8_crystal()['table']; assert t[1]['bits_per_voxel']==4 and t[1]['symbol_err']<0.01
def test_9(): n=S.i9_tessera_memory()['noise']['sig4deg_0.04']; assert n['ber_hamming74']<n['ber_raw']/50 and n['blocks_2KB_recovered']>0.99
def test_10(): r=S.i10_palace_grover(); assert r['grover_p']>0.99 and r['grover_queries']*10<r['classical_expected']
if __name__=='__main__':
    import sys; fs=[v for k,v in dict(globals()).items() if k.startswith('test_')]; f=0
    for t in fs:
        try: t(); print('PASS',t.__name__)
        except AssertionError: f+=1; print('FAIL',t.__name__)
    sys.exit(f)
