#include "linkedList.h"

using namespace std;

LinkedList::LinkedList()
{
	m_head = new Node();
	m_head->next = NULL;
	m_size = 0;
}

LinkedList::~LinkedList()
{
	cout << "Do we need this" << endl;
}

void LinkedList::insertAtBeg(int data)
{
	Node* tmp = new Node();
	tmp->data = data;
	tmp->next = m_head;
	m_head = tmp;
	m_size += 1;
}

void LinkedList::printElems()
{
	Node* tmp = m_head;
	while (tmp->next != NULL)
	{
		cout << tmp->data << " -> ";
		tmp = tmp->next;
	}
	cout << "NULL" <<endl;
}

int LinkedList::delFromEnd()
{
	int data = 0;
	Node* tmp = m_head;

	while (tmp->next->next != NULL)
		tmp = tmp->next;

	data = tmp->data;
	tmp->next = NULL;
	delete tmp->next;

	return data;
}

void LinkedList::insertAtEnd(int data)
{
	Node* end = new Node();
	if (m_size == 0)
	{
		end->data = data;
		end->next = m_head;
		m_head = end;
		m_size += 1;
		return;
	}

	end = m_head;
	while (end->next->next != NULL)
	{
		end = end->next;
	}

	Node* tmp = new Node();
	tmp->data = data;
	tmp->next = NULL;

	end->next = tmp;
}
