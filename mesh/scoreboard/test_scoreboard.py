import rank,velocity
def test_only_measured_gains():
    r=rank.rank(); assert r and all(velocity.gain(m)>0 and m["pr"] for m in r)
def test_speed_outranks_equal_accuracy():
    assert rank.W["tokens"]>rank.W["speed"]>rank.W["accuracy"]>max(v for k,v in rank.W.items() if k not in("tokens","speed","accuracy"))
def test_sorted():
    r=rank.rank(); assert all(a["impact"]>=b["impact"] for a,b in zip(r,r[1:]))
def test_velocity_keys():
    s=velocity.stats({"kept":19,"tried":32}); assert s["tokens_per_merged_improvement_est"]>0 and 0<s["gate_pass_rate"]<=1
import collab_check as c
def test_handoff():
    assert c.check_handoff("HANDOFF Q-007 PASS https://github.com/vitalitychems-dot/TESSERA/pull/262 forged_cookie_ok=1->0 by=cursor")
    assert not c.check_handoff("HANDOFF Q-007 PASS https://x/pull/1 by=cursor")
    assert c.check_prop('{"id":"P1","by":"rick","goal":"speed","idea":"x"}') and not c.check_prop('{"id":1}')
