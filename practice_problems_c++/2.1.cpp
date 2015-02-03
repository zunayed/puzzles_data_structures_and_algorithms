#include "data_structures/linked_list.h"

void remove_dupes(List ll){
    if (ll.head->next_node == NULL)
        return;

    List::node* current = ll.head;
    while (current->next_node != NULL){
        List::node* checker = current;
        while (checker->next_node != NULL){
            if (checker->next_node->data == current->data){
                cout << "Found Duplicate\n";
                cout << checker->next_node->next_node;
                checker->next_node = checker->next_node->next_node;
            } else {
                checker = checker->next_node;
            }
        }
        current = current->next_node;
    }

    ll.PrintList();
}

int main(){
    List Test;

    Test.AddNode(9);
    Test.AddNode(1);
    Test.AddNode(4);
    Test.AddNode(3);
    Test.AddNode(3);
    Test.PrintList();
    cout << "----Before remove function----" << endl;
    remove_dupes(Test);
    //cout << "----after remove function----" << endl;
    //Test.PrintList();


}
