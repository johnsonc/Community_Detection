import sys, os
def main():
	run("higgs-social_network.txt:higgs:0.01:4")

def run(me=""):
	textFile, dataSet, convergence, thread = me.split(':');
	
	inputDirectory = "/home/armysummer/tangelo_html/community_detection/input/"+dataSet+"/"
	output_path = "/home/armysummer/tangelo_html/community_detection/output/"+dataSet+"/"
	os.system('rm -rf ' + inputDirectory + '*')
	os.system('rm -rf ' + output_path)

	

	delitePath = "./published/OptiGraph/bin/delite CommunityDetectionCompiler /home/armysummer/tangelo_html/community_detection/datasets/"+textFile+ " /home/armysummer/tangelo_html/community_detection/input/" + dataSet + "/"+dataSet+" "+convergence+ " -t"+thread
	os.chdir('/home/armysummer/hyperdsl')
	
	if os.path.isdir(inputDirectory) == False:
		os.chmod("/home/armysummer/tangelo_html/community_detection/input/", 0777)
		makeFolder = 'mkdir '+inputDirectory
		os.system(makeFolder)
		os.chmod(inputDirectory, 0777)
	

	os.system(delitePath)

	#print delitePath
	return me


if __name__ == "__main__":
    main()