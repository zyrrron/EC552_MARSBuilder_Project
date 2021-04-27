from networkx import nx

# G = nx.Graph()

# G.add_edge("METER1", "MIXER")
# G.add_edge("METER2", "MIXER")
# draw = nx.nx_agraph.to_agraph(G).write(out_dir)



class pipelining_algorithm():
    def __init__(self, base_graph=None):
        if not base_graph:
            self.G = nx.DiGraph()
        else:
            self.G = base_graph
        
        self.carrier_count = 0
        self.meter_count = 0
        self.cw_count = 0
        self.iw_count = 0
        self.temp = nx.Graph()

    
    def add_edge(self, edge1, edge2, process=None):
        # add meter components with appropriate ports
        if process == "METER":
            carrier = f"carrier_{self.carrier_count}"
            self.carrier_count += 1
            meter = f"METER_{self.meter_count}"
            self.meter_count += 1
            cw = f"carrier_waste_{self.cw_count}"
            self.cw_count += 1
            iw = f"input_waste_{self.iw_count}"
            self.iw_count += 1

            self.G.add_edge(carrier, meter)
            self.G.add_edge(edge1, meter)
            self.G.add_edge(meter, cw)
            self.G.add_edge(meter, edge2)
            self.G.add_edge(meter, iw)


        else:
            self.G.add_edge(edge1, edge2)

    def pipeline(self):
        end_nodes = []

        for node in self.G.nodes():
            if self.G.out_degree(node) == 0:
                end_nodes.append(node)

        for node in end_nodes:
            self.find_pred(node)

    def find_pred(self, node):
        current_meter = ""
        if self.G.has_node(node):
            for pred_node in self.G.predecessors(node):
                if "METER" in pred_node:
                    if current_meter != "":
                        
                        for pred2_node in self.G.predecessors(pred_node):
                            # remove extra carrier load
                            if "carrier" in pred2_node:
                                self.G.remove_node(pred2_node)
                                print(f"removed extra carrier load {pred2_node}")
                                break
                        
                        # remove extra carrier waste
                        for suc_node in self.G.successors(pred_node):
                            if "carrier" in suc_node:
                                self.G.remove_node(suc_node)
                                print(f"removed extra carrier waste {suc_node}")
                                break
                        # pipeline carrier
                        self.G.remove_edge(current_meter, node)
                        self.G.add_edge(current_meter, pred_node)
                        print(f"rewired an edge from {current_meter} -> {node} to {current_meter} -> {pred_node}")
                        
                        break
                    current_meter = pred_node

                self.find_pred(pred_node)


    def draw_graph(self, name, option=None):
        out_dir = f"out/{name}.dot"
        if option:
            print("Using pipelining algorithm...\n")
            for i in range(self.meter_count):
                self.pipeline()
        nx.nx_agraph.to_agraph(self.G).write(out_dir)
