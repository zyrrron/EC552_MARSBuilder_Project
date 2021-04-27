from pipelining_algorithm import pipelining_algorithm

pa = pipelining_algorithm()
pa.add_edge("input0", "mix1", "METER")
pa.add_edge("input1", "mix1", "METER")

pa.add_edge("mix1", "central_well")

pa.add_edge("input2", "central_well")

pa.draw_graph("fluorescence", True)