#include <stdio.h>
#include <stdlib.h>

typedef enum {WHITE, GRAY, BLACK} Color;

typedef struct Node {
    int vertex;
    Color color;
    struct Node* next;
} Node;

void addEdge(Node** adjList, int u, int v)
{
    // u -> v
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = v;
    newNode->color = WHITE;
    newNode->next = NULL;

    if (!adjList[u] || adjList[u]->vertex > v) {
        newNode->next = adjList[u];
        adjList[u] = newNode;
    } else {
        Node* current = adjList[u];
        while (current->next && current->next->vertex < v) {
            current = current->next;
        }
        newNode->next = current->next;
        current->next = newNode;
    }

    // v -> u
    newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = u;
    newNode->color = WHITE;
    newNode->next = NULL;

    if (!adjList[v] || adjList[v]->vertex > u) {
        newNode->next = adjList[v];
        adjList[v] = newNode;
    } else {
        Node* current = adjList[v];
        while (current->next && current->next->vertex < u) {
            current = current->next;
        }
        newNode->next = current->next;
        current->next = newNode;
    }
}

void dfs(Node** adjList, int vertex) {
    Node* current = adjList[vertex];
    printf("%d ", vertex);

    current->color = GRAY;
    while (current) {
        int nextVertex = current->vertex;
        if (adjList[nextVertex] && adjList[nextVertex]->color == WHITE) {
            adjList[nextVertex]->color = GRAY;
            dfs(adjList, nextVertex);
        }
        current = current->next;
    }
    adjList[vertex]->color = BLACK;
}

void bfs(Node** adjList, int N, int startVertex) {
    int* queue = (int*)malloc(sizeof(int) * (N + 1)); // Queue initialize
    int front = 0, rear = 0;
    int i;

    for (i = 1; i <= N; i++) {
        if (adjList[i]) {
            adjList[i]->color = WHITE;
        }
    }

    // Enqueue and paint to GRAY
    queue[rear++] = startVertex;
    adjList[startVertex]->color = GRAY;

    while (front < rear) {  // Queue is not empty
        int currentVertex = queue[front++];     // Dequeue
        printf("%d ", currentVertex);

        Node* current = adjList[currentVertex];
        while (current) {
            int nextVertex = current->vertex;
            if (adjList[nextVertex] && adjList[nextVertex]->color == WHITE) {
                queue[rear++] = nextVertex; // Enqueue
                adjList[nextVertex]->color = GRAY;
            }
            current = current->next;
        }
        adjList[currentVertex]->color = BLACK;
    }

    free(queue);
}

int main(void) {
    int N, M, V;
    scanf("%d %d %d", &N, &M, &V);

    Node** adjList = (Node**)malloc(sizeof(Node*) * (N + 1));
    for (int i = 1; i <= N; i++) {
        adjList[i] = NULL;
    }

    int a, b;
    // Construct adjacency list
    for (int i=0; i<M; i++) {
        scanf("%d %d", &a, &b);
        addEdge(adjList, a, b);
    }

    dfs(adjList, V);
    printf("\n");
    bfs(adjList, N, V);
    printf("\n");

    for (int i = 1; i <= N; i++) {
        Node* current = adjList[i];
        while (current) {
            Node* temp = current;
            current = current->next;
            free(temp);
        }
    }
}