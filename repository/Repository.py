from domain.Graph import Graph
import networkx as netx
class Repository:
    def __init__(self,filename,label='label'):
        self.__filename=filename
        self.__label = label
        self.__graph=Graph(self.__readData())


    def __readData(self):
        graph=netx.read_gml(self.__filename,self.__label)
        return graph

    def writeData(self,lines):
        withoutExt=self.__filename.split(".")[0]
        f=open(withoutExt+"_solution.txt","w")
        f.write('\n')
        for line in lines:
            f.write(line+'\n')
    def getGraph(self):
        return self.__graph


