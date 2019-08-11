import java.awt.*;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.List;

public class WeightedGraph {

    // Node class
    class WeightedNode {
        int mIndex;
        private List<WeightedEdge> mNeighbors = new ArrayList<WeightedEdge>();

        WeightedNode(int index) {
            mIndex = index;
        }
    }

    // Edge class
    private class WeightedEdge implements Comparable {

        private WeightedNode mFirst, mSecond;
        private double mWeight;

        WeightedEdge(WeightedNode first, WeightedNode second, double weight) {
            mFirst = first;
            mSecond = second;
            mWeight = weight;
        }

        @Override
        public int compareTo(Object o) {
            WeightedEdge e = (WeightedEdge) o;
            return Double.compare(mWeight, e.mWeight);
        }
    }

    // Weighted Graph
    // List of vertices
    private List<WeightedNode> mVertices = new ArrayList<WeightedNode>();

    // Constructor
    public WeightedGraph(int numberOfVertices) {
        for (int i = 0; i < numberOfVertices; i++) {
            mVertices.add(new WeightedNode(i));
        }
    }

    // Add edge
    public void addEdge(int firstVertex, int secondVertex, double weight) {
        WeightedNode first = mVertices.get(firstVertex);
        WeightedNode second = mVertices.get(secondVertex);

        WeightedEdge edge = new WeightedEdge(first, second, weight);
        first.mNeighbors.add(edge);
        second.mNeighbors.add(edge);
    }

    /**
     * Prints the graph to the console. Each vertex is printed on its own line,
     * starting with the vertex's number (its index in the mVertices list), then
     * a colon, then a sequence of pairs for each edge incident to the vertex.
     * For each edge, print the number of the vertex at the opposite end of the
     * edge, as well as the edge's weight.
     *
     * Example: in a graph with three vertices (0, 1, and 2), with edges from 0
     * to 1 of weight 10, and from 0 to 2 of weight 20, printGraph() should print
     *
     * Vertex 0: (1, 10), (2, 20) Vertex 1: (0, 10) Vertex 2: (0, 20)
     */
    public void printGraph() {
        HashSet<Integer> checked = new HashSet<>();
        for (WeightedNode node : mVertices) {
            System.out.print("Vertex " + node.mIndex + ": ");
            checked.add(node.mIndex);

            for (WeightedEdge edge : node.mNeighbors) {
                if (checked.contains(edge.mSecond.mIndex))
                    System.out.print("(" + edge.mFirst.mIndex + ", " + edge.mWeight + ")\t");
                else
                    System.out.print("(" + edge.mSecond.mIndex + ", " + edge.mWeight + ")\t");
            }
            System.out.println();
        }
    }

    /**
     * Applies Prim's algorithm to build and return a minimum spanning tree for
     * the graph. Start by constructing a new WeightedGraph with the same number
     * of vertices as this graph. Then apply Prim's algorithm. Each time an edge
     * is selected by Prim's, add an equivalent edge to the other graph. When
     * complete, return the new graph, which is the minimum spanning tree.
     *
     * @return an UnweightedGraph representing this graph's minimum spanning
     * tree.
     */
    public WeightedGraph getMinimumSpanningTree() {
        // TODO: build and return the MST.
        WeightedGraph mst = new WeightedGraph(mVertices.size());
        HashSet<Integer> markedVertices = new HashSet<>();
        PriorityQueue<WeightedEdge> edges = new PriorityQueue<>();

        // Choose random node
        WeightedNode u = mVertices.get(0);
        // Add to marked vertices
        markedVertices.add(u.mIndex);
        // Add all edges to PQ
        edges.addAll(u.mNeighbors);

        while(!edges.isEmpty()) {
            // Get minimum edge
            WeightedEdge minEdge = edges.poll();

            // If the first node isn't in the hashset
            if (!markedVertices.contains(minEdge.mFirst.mIndex)) {
                // Add new vertex to checked
                markedVertices.add(minEdge.mFirst.mIndex);
                // Add its edges
                edges.addAll(minEdge.mFirst.mNeighbors);
                // Build tree
                mst.addEdge(minEdge.mFirst.mIndex, minEdge.mSecond.mIndex, minEdge.mWeight);
            }
            else if (!markedVertices.contains(minEdge.mSecond.mIndex)) {
                // Add new vertex to checked
                markedVertices.add(minEdge.mSecond.mIndex);
                // Add its edges
                edges.addAll(minEdge.mSecond.mNeighbors);
                mst.addEdge(minEdge.mFirst.mIndex, minEdge.mSecond.mIndex, minEdge.mWeight);

            }
        }

        return mst;
    }

    /**
     * Applies Dijkstra's algorithm to compute the shortest paths from a source
     * vertex to all other vertices in the graph. Returns an array of path
     * lengths; each value in the array gives the length of the shortest path
     * from the source vertex to the corresponding vertex in the array.
     */
    public double[] getShortestPathsFrom(int source) {
        // TODO: apply Dijkstra's algorithm and return the distances array.

        // This queue is used to select the vertex with the smallest "d" value
        // so far.
        // Each time a "d" value is changed by the algorithm, the corresponding
        // DijkstraDistance object needs to be removed and then re-added to
        // the queue so its position updates.
        PriorityQueue<DijkstraDistance> vertexQueue =
                new PriorityQueue<DijkstraDistance>();

        // Initialization: set the distance of the source node to 0, and all
        // others to infinity. Add all distances to the vertex queue.
        DijkstraDistance[] distances = new DijkstraDistance[mVertices.size()];
        distances[source] = new DijkstraDistance(source, 0);
        for (int i = 0; i < distances.length; i++) {
            if (i != source)
                distances[i] = new DijkstraDistance(i, Integer.MAX_VALUE);

            vertexQueue.add(distances[i]);
        }

        while (vertexQueue.size() > 0) {
            DijkstraDistance vertex = vertexQueue.poll();
            for( WeightedEdge e : mVertices.get(vertex.mVertex).mNeighbors){
                int child;
                if (vertex.mVertex == e.mFirst.mIndex)
                    child = e.mSecond.mIndex;
                else
                    child = e.mFirst.mIndex;

                double len = distances[vertex.mVertex].mCurrentDistance + e.mWeight;
                if (len < distances[child].mCurrentDistance){
                    distances[child] = new DijkstraDistance(child, len);
                    vertexQueue.add(new DijkstraDistance(child, len));
                }
            }
        }

        double[] results = new double[mVertices.size()];
        for (int i = 0; i < distances.length; i++) {
            results[i] = distances[i].mCurrentDistance;
        }

        return results;
    }

    class DijkstraDistance implements Comparable {

        int mVertex;
        double mCurrentDistance;

        DijkstraDistance(int vertex, double distance) {
            mVertex = vertex;
            mCurrentDistance = distance;
        }

        @Override
        public int compareTo(Object other) {
            DijkstraDistance d = (DijkstraDistance) other;
            return Double.compare(mCurrentDistance, d.mCurrentDistance);
        }
    }

   public static void main(String[] args) {
      // Use this main to test your code by hand before implementing the program.
//      WeightedGraph g = new WeightedGraph(6);
//      g.addEdge(0, 1, 1);
//      g.addEdge(0, 2, 3);
//      g.addEdge(1, 2, 1);
//      g.addEdge(1, 3, 1);
//      g.addEdge(1, 4, 4);
//      g.addEdge(2, 3, 1);
//      g.addEdge(2, 5, 2);
//      g.addEdge(3, 4, 1);
//      g.addEdge(3, 5, 3);
//      g.addEdge(4, 5, 2);
//      g.printGraph();
//
//
//
//      double[] distances = g.getShortestPathsFrom(0);
//      for (int i = 0; i < distances.length; i++) {
//         System.out.println("Distance from 0 to " + i + ": " +
//          distances[i]);
//
//      }
//
//      WeightedGraph mst = g.getMinimumSpanningTree();
//      System.out.println("Minimum spanning tree:");
//      mst.printGraph();

       Scanner input = new Scanner(System.in);
       System.out.println("Enter file name: ");
       String file_name = input.nextLine();
       WeightedGraph g = null;

       try(BufferedReader reader = new BufferedReader(new FileReader(file_name))) {
           int numNodes = Integer.parseInt(reader.readLine());
           g = new WeightedGraph(numNodes);
           String line;

           int vertex = 0;
           while((line = reader.readLine()) != null) {
               Scanner charReader = new Scanner(line);
               while (charReader.hasNext()) {
                   int nextVertex = Integer.parseInt(charReader.next());
                   int weight = Integer.parseInt(charReader.next());
                   g.addEdge(vertex, nextVertex, weight);
               }
               vertex++;
           }

       }catch (IOException e) {
           System.out.println(e.getMessage());
       }

       while (true) {
           System.out.println("1) Print Graph\n2) Minimum Spanning Tree\n3) Shortest Path\n4) Quit");
           int menu_option = Integer.parseInt(input.nextLine());

           if (menu_option == 1) {
               g.printGraph();
           }
           else if (menu_option == 2) {
               WeightedGraph mst = g.getMinimumSpanningTree();
               mst.printGraph();
           }else if (menu_option == 3) {
               System.out.println("Enter source index: ");
               int source_vertex = Integer.parseInt(input.nextLine());
               double[] distances = g.getShortestPathsFrom(source_vertex);
               for (int i = 0; i < distances.length; i++) {
                   System.out.println("Distance from " + source_vertex + " to " + i + ": " +
                           distances[i]);
               }

           }else if (menu_option == 4)
               break;
       }
   }

}

