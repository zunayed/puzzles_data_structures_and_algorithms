#include <cstdlib>
#include <iostream>

using namespace std;


class List{
private:
    struct node{
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


void List::DeleteNode(int del_data){
    temp = head;
    current = head;
    node* pointer_to_delete = NULL;

    while(current != NULL && current->data != del_data){
        temp = current;
        current = current->next_node;
    }

    if(current == NULL){
        cout << "element not  found";
        delete pointer_to_delete;
    }
    else {
        //found the data to delete
        pointer_to_delete = current;
        current = current->next_node;
        temp->next_node = current;

        if(pointer_to_delete == head){
            head = head->next_node;
            temp = NULL;
        }

        delete pointer_to_delete;
        cout << del_data << " was deleted\n";
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
    Test.AddNode(1);

    Test.PrintList();

    Test.DeleteNode(5);
    Test.PrintList();

}