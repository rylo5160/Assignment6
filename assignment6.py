import getopt, sys

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "m:g:j:p:")
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        sys.exit(2)
    for o, a in opts:
		if o in ("-p"):
			print "flag", o
			print "args", a
			print a[0]
			print float(a[1:])
			#setting the prior here works if the Bayes net is already built
			#setPrior(a[0], float(a[1:])
		elif o in ("-m"):
			print "flag", o
			print "args", a
			print type(a)
			#calcMarginal(a)
		elif o in ("-g"):
			print "flag", o
			print "args", a
			print type(a)
			'''you may want to parse a here and pass the left of |
			and right of | as arguments to calcConditional
			'''
			p = a.find("|")
			print a[:p]
			print a[p+1:]
			#calcConditional(a[:p], a[p+1:])
		elif o in ("-j"):
			print "flag", o
			print "args", a
		else:
			assert False, "unhandled option"
		
    # ...

if __name__ == "__main__":
    main()

def disease_Net():
	
	# Begin the bayes network
	smoker = 1
	cancer = 2
	xray = 3
	dyspnoea = 4
	number_of_nodes = 5
	
	pollution_Node = bayesNode(0, 2, name = "pollution")
	smoker_Node = bayesNode(1, 2, name = "smoker")
	cancer_Node = bayesNode(2, 2, name = "cancer")
	xray_Node = bayesNode(3, 2, name = "xray")
	dysponea_Node = bayesNode(4, 2, name = "dyspnoea")
	
	# Set parents and children
	pollution_Node.add_child(cancer_Node)
	smoker_Node.add_child(cancer_Node)
	
	cancer_Node.add_parent(pollution_Node)
	cancer_Node.add_parent(smoker_Node)
	
	xray_Node.add_parent(cancer_Node)
	dysponea_Node.add_parent(cancer_Node)
	
	cancer_Node.add_child(xray_Node)
	cancer_Node.add_child(dysponea_Node)
	
	nodes = [pollution_Node, smoker_Node, cancer_Node, xray_Node, dysponea_Node]
	
	# Set probabilities given by assignment
	# 1 = high pollution, 0 = low pollution, 1 = postitive, 0 = negative
	prob = zeros([pollution_Node.size(), smoker_Node.size(), cancer_Node.size()]),
	prob[0, 1, ] = [0.050, 0.950]
	prob[0, 0, ] = [0.020, 0.980]
	prob[1, 1, ] = [0.030, 0.970]
	prob[1, 0, ] = [0.001, 0.999]
	
	prob = zeros([cancer_Node.size(), xray_Node.size()]),
	prob[1, ] = [0.9, 0.1]
	prob[0, ] = [0.2, 0.8]
	
	prob = zeros([cancer_Node.size(), dysponea_Node.size()])
	prob[1, ] = [0.65, 0.35]
	prob[0, ] = [0.30, 0.70]

	prob = zeros([pollution_Node.size()]),
	prob[1] = [0.1]
	prob[0] = [0.9]
	
	prob = zeros([smoker_Node.size()]),
	prob[1] = [0.3]
	prob[0] = [0.7]

# Create the actual network
def create_Network():
	for node in disease_Net(nodes):
		if node.id == 0:
			pollution = node
		if node.id == 1:
			smoker = node
		if node.id == 2:
			cancer = node
		if node.id == 3:
			xray = node
		if node.id == 4:
			dysponea = node

