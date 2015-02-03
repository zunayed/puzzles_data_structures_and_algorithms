#include <typeinfo>
#include "data_structures/linked_list.h"

void remove_dupes(List::Node* head){
    if (head->next_node == NULL)
        return;

    List::Node* current = head;
    while (current != NULL){
        List::Node* checker = current;
        while (checker->next_node != NULL){
            if (checker->next_node->data == current->data){
                checker->next_node = checker->next_node->next_node;
            } else {
                checker = checker->next_node;
            }
        }
        current = current->next_node;
    }
}

int main(){
    List Test;

    cout << "----Before remove function----" << endl;
    Test.AddNode(9);
    Test.AddNode(1);
    Test.AddNode(4);
    Test.AddNode(3);
    Test.AddNode(9);
    Test.AddNode(3);
    Test.PrintList();
    remove_dupes(Test.head);
    cout << "----after remove function----" << endl;
    Test.PrintList();

}
