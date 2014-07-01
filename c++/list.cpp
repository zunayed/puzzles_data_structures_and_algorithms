#include <iostream>

using namespace std;

class List{
private:
    struct node
    {
        int data;
        node* next_node;   
    };

    node* head;
    node* current;
    node* temp;
public:
    List();
    void PrintList(); 
    void AddNode(int add_data);
    void DeleteNode(int del_data);
};

List(){
    head = NULL;
    current = NULL;
    temp = NULL;
}

void AddNode(int data){
    node* n = new node;
    n->next = NULL;
    m->data = data;

    if(head != NULL){
        current = head;
        while(current->next != NULL){
            current = current->next;
        }
        current->next = n;

    }
    else{
        head = n;
    }
}

void PrintList(){
    current = head;
    while(current != NULL){
        count << current->data << endl;
        current = current->next;
    }
}

int main(int argc, char** argv){
    List Test;

    Test.AddNode(9);
    Test.AddNode(5);
    Test.AddNode(2);

    Test.PrintList();
}