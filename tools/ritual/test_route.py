import unittest, route
# synthetic fixture (no real truth committed): agent "good" is accurate on cat X, "bad" is not
cats = ["X", "X", "X", "Y", "Y"]; truth = [10, 20, 30, 5, 7]
ans = {"good": [10, 20, 30, 9, 9], "bad": [15, 30, 45, 5, 7], "mid": [11, 22, 33, 6, 8]}
conf = {"good": [0.9, 0.9, 0.2, 0.9, 0.9], "bad": [0.9] * 5, "mid": [0.9] * 5}
class T(unittest.TestCase):
    def test_routes_to_best_by_category_one_ask(self):
        out, asks = route.route(cats, ans, conf, truth)
        self.assertEqual(out, [10, 20, 30, 5, 7]); self.assertEqual(asks, 5)
    def test_escalates_on_low_conf(self):
        out, asks = route.route(cats, ans, conf, truth, conf_min=0.5)
        self.assertEqual(asks, 4 + 3); self.assertEqual(out[2], 33)
    def test_poll_all_cost(self):
        self.assertEqual(route.poll_all(ans)[1], 15)
    def test_categorical(self):
        out, _ = route.route(["c", "c"], {"a": ["A", "B"], "b": ["B", "A"]}, {"a": [1, 1], "b": [1, 1]}, ["A", "B"])
        self.assertEqual(out, ["A", "B"])
if __name__ == "__main__": unittest.main()
