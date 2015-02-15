#include "data_structures/linked_list.h"


List::Node* partition (List::Node* head, int x) {
    // Create two lists. One greater and one smaller then x and then merge
    List::Node* current = head; 
    List smaller;
    List bigger;

    while (current != NULL){
        if (current->data < x) {
            smaller.AddNode(current->data);
        } else {
            bigger.AddNode(current->data);            
        }
        current = current->next_node;
    }
    // get end of smaller lists
    List::Node* small_node = smaller.head;

    while (small_node->next_node != NULL){
        small_node = small_node->next_node;
    }

    small_node->next_node = bigger.head;
    return smaller.head;
}

int main() {
    List Test;

    cout << "----Before partition function----" << endl;
    Test.AddNode(9);
    Test.AddNode(1);
    Test.AddNode(4);
    Test.AddNode(3);
    Test.AddNode(9);
    Test.AddNode(3);
    Test.AddNode(7);
    Test.PrintList();
    List::Node* new_head = partition(Test.head, 9);
    List new_list;
    new_list.head = new_head;
    cout << "----New list after partition function----" << endl;
    new_list.PrintList();

}
