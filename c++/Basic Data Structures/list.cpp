#include <cstdlib>
#include <iostream>

using namespace std;


class List{
private:
    typedef struct node{
        int data;
        node* next_node;   
    }* nodePtr;

    nodePtr head;
    nodePtr current;
    nodePtr temp;

public:
    List();
    void PrintList(); 
    void AddNode(int add_data);
    // void DeleteNode(int del_data);
};


List::List(){
    head = NULL;
    current = NULL;
    temp = NULL;
}

void List::AddNode(int data){
    node* n = new node;
    n->next_node = NULL;
    n->data = data;

    if(head != NULL){
        current = head;
        while(current->next_node != NULL){
            current = current->next_node;
        }
        current->next_node = n;

    }
    else{
        head = n;
    }
}

void List::PrintList(){
    current = head;
    while(current != NULL){
        cout << current->data << endl;
        current = current->next_node;
    }
}

int main(int argc, char** argv){
    List Test;

    Test.AddNode(9);
    Test.AddNode(5);
    Test.AddNode(2);

    Test.PrintList();
}