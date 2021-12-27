import unittest


class MyTestCase(unittest.TestCase):
    g_algo = GraphAlgo()
    file = "C:/Users/User/PycharmProjects/Ex3/JSON files/A3.json"

    class MyTestCase(unittest.TestCase):
        def test_get_graph(self):
            self.assertEqual(g_algo.graph, g_algo.get_graph())

        def test_load_from_json(self):
            g_algo = GraphAlgo()
            file = "C:/Users/User/PycharmProjects/Ex3/JSON files/1000Nodes.json"
            self.assertEqual(g_algo.load_from_json(file), True)




if __name__ == '__main__':
    unittest.main()
