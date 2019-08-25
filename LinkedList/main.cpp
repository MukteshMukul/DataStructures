#include "linkedList.h"

using namespace std;

int main(int ac, char* av[])
{
	unique_ptr<LinkedList>firstnode = make_unique<LinkedList>();
	//LinkedList* firstnode = new LinkedList();

	int choice = 0;
	cout << "choose the operation to be performed on linked List" << endl;
	while (1)
	{
		cout << "choose the operation to be performed on linked List" << endl;
		cout << "1. insert at begining" << endl;
		cout << "2. print elements" << endl;
		cout << "3. Delete from End" << endl;
		cout << "4. insert at End" << endl;
		cout << "0. quit" << endl;
		cin >> choice;
		
		if (choice == 0)
			break;

		int tmpdata = 0;
		switch (choice)
		{
		case(1):
			cout << "Enter number to insert" << endl;
			cin >> tmpdata;
			firstnode->insertAtBeg(tmpdata);
			break;
		case(2):
			firstnode->printElems();
			break;
		case(3):
			firstnode->delFromEnd();
			break;
		case(4):
			cout << "Enter number to insert at last" << endl;
			cin >> tmpdata;
			firstnode->insertAtEnd(tmpdata);
		default:
			break;
		}
	}

	return 0;
}

