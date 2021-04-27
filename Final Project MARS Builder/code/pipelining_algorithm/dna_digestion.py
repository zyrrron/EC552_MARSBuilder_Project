from pipelining_algorithm import pipelining_algorithm

pa = pipelining_algorithm()
pa.add_edge("input0", "mix1", "METER")
pa.add_edge("input1", "mix1", "METER")
pa.add_edge("input2", "mix1", "METER")

pa.add_edge("mix1", "incubator")

pa.add_edge("incubator", "out_a")

pa.draw_graph("dna_digestion", True)