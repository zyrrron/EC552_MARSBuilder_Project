from pipelining_algorithm import pipelining_algorithm

pa = pipelining_algorithm()
pa.add_edge("input0", "mix1", "METER")
pa.add_edge("input1", "mix1", "METER")

pa.add_edge("mix1", "out_d")

pa.draw_graph("transformation", True)