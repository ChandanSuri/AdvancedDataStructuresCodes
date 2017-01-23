import java.util.InputMismatchException;
import java.util.Scanner;

public class AdjacencyMatrix
{
    private final int max_no_of_vertices;
    private int adjacency_matrix[][];
     
    public AdjacencyMatrix(int number_of_vertices)
    {
        max_no_of_vertices = number_of_vertices;
        adjacency_matrix = new int[max_no_of_vertices+1][max_no_of_vertices+1];
    }
     
    public void setEdge(int from_vertex,int to_vertex,int edge)
    {
        try
        {
            adjacency_matrix[from_vertex][to_vertex] = edge;
        }
        catch(ArrayIndexOutOfBoundsException indexBounce)
        {
            System.out.println("the vertex entered isnot present");
             
        }
    }
    public int getEdge(int from_vertex,int to_vertex)
    {
        try{
            return adjacency_matrix[from_vertex][to_vertex];
        }
        catch(ArrayIndexOutOfBoundsexception indexBounce)
        {
            System.out.println("The vertex entered is not present");
             
        }
        return -1;
    }
    public static void main(String args[])
    {
        int number_of_vertices,  count = 1, source = 0, destination = 0;
        Scanner d = new Scanner(System.in);
        AdjacencyMatrix adjacencyMatrix;
        try{
            System.out.println("Enter the number of vertices => ");
            number_of_vertices = d.nextInt();
            System.out.println("Enter the number of edges => ");
            int number_of_edges = d.nextInt();
             
            adjacencyMatrix = new AdjacencyMatrix(number_of_vertices);
            System.out.println("Enter the graph edges: <source> <destination>");
            while(count <= number_of_edges)
            {
                source = d.nextInt();
                destination = d.nextInt();
                adjacencyMatrix.setEdge(source,destination,1);
                count++;
            }
            System.out.println("The adjacency matrix for given graph is:");
            for(int i=1;i<=number_of_vertices;i++)
            {
                System.out.print(i);
            }
            System.out.println();
            for(int i=1;i<=number_of_vertices;i++)
            {
                System.out.print(i);
                for(int j=1;j<=number_of_vertices;j++)
                {
                    System.out.print(adjacencyMatrix.getEdge(i,j));
                }
                System.out.println();
            }
        }
        catch(InputMismatchException inputMismatch)
        {
            System.out.println("error in input format. <source index> <destination index>");
        }
        d.close();
    }
}