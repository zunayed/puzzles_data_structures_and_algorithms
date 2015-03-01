#ifndef LINKED_LIST_H
#define LINKED_LIST_H 

#include <cstdlib>
#include <iostream>
#include <stdexcept>


class List{
public: 
    struct Node{
        int data;
        Node* next_node;   
    };

    Node* head;

    List();
    void PrintList() const; 
    void AddNode(int add_data);
    void DeleteNode(int del_data);
};


List::List(){
    head = NULL;
}


void List::AddNode(int data){
    Node* n = new Node;
    Node* current;

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
    Node* temp = head;
    Node* current = head;
    Node* pointer_to_delete = NULL;

    while(current != NULL && current->data != del_data){
        temp = current;
        current = current->next_node;
    }

    if(current == NULL){
        std::cout << "element not  found";
        throw std::invalid_argument( "element not  found" );
    }
    else{
        //found the data to delete
        pointer_to_delete = current;
        current = current->next_node;
        temp->next_node = current;

        if(pointer_to_delete == head){
            head = head->next_node;
            temp = NULL;
        }

        delete pointer_to_delete;
        std::cout << del_data << " was deleted\n";
    }
}

void List::PrintList() const{
    Node* current = head;
    while(current != NULL){
        std::cout << current->data << std::endl;
        current = current->next_node;
    }
}

#endif
