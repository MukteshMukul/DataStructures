#pragma once

#include <iostream>

struct Node
{
	int data;
	struct Node* next;
};


class LinkedList
{
private:
	Node* m_head;
	int m_size;

public:
	LinkedList();
	~LinkedList();

	void insertAtBeg(int data);
	void printElems();
	int delFromEnd();
	void insertAtEnd(int data);
};