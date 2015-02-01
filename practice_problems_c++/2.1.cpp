#include "data_structures/linked_list.h"


int main(){
    List Test;

    Test.AddNode(9);
    Test.AddNode(5);
    Test.AddNode(2);
    Test.AddNode(1);

    Test.PrintList();

    Test.DeleteNode(5);
    Test.PrintList();   
}
