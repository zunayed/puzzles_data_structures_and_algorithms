/*
Implement an algorithm to find the kth to last element of a singly linked list
*/
#include <typeinfo>
#include "data_structures/linked_list.h"


List::Node* kth_element(List::Node* head, int k){
    if (k <= 0) { return NULL; } 
    
    List::Node* p1 = head;
    List::Node* p2 = head;

    for (int i = 0; i < k - 1; i++){
        p2 = p2->next_node;
    }

    while (p2->next_node != NULL){
        p1 = p1->next_node;
        p2 = p2->next_node;
   } 
    return p1;
}

int main(){
    List Test;

    Test.AddNode(9);
    Test.AddNode(1);
    Test.AddNode(4);
    Test.AddNode(3);
    Test.AddNode(7);
    Test.AddNode(3);
    Test.PrintList();
    List::Node* kth_elem = kth_element(Test.head, 2);
    cout << kth_elem->data;
}
