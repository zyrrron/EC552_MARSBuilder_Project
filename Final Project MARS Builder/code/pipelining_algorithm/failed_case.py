from pipelining_algorithm import pipelining_algorithm

pa = pipelining_algorithm()
pa.add_edge("input0", "mix1", "METER")
pa.add_edge("input1", "mix1", "METER")

pa.add_edge("mix1", "mix3")

pa.add_edge("input2", "mix2", "METER")
pa.add_edge("input3", "mix2", "METER")

pa.add_edge("mix2", "mix3")

pa.add_edge("mix3", "out_a")

pa.draw_graph("failed_case", True)