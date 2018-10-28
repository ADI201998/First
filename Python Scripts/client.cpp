// Client side C/C++ program to demonstrate Socket programming 
#include <iostream>
#include <sstream>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <unistd.h>
#include <string>
#include <arpa/inet.h>
#include <string.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h> 

using namespace std;

#define PORT 50007

int main() 
{ 
	struct sockaddr_in address; 
	int valread; 
	struct sockaddr_in serv_addr; 
	char hello[1000] ; 
	char buffer[1024] = {0}; 
    int n = 0;
	int sock = socket(AF_INET, SOCK_STREAM, 0);

	memset(&serv_addr, '0', sizeof(serv_addr)); 

	serv_addr.sin_family = AF_INET; 
	serv_addr.sin_port = htons(PORT); 
	
	// Convert IPv4 and IPv6 addresses from text to binary form 
	inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr);

	connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr));
    while(1)
    {
        stringstream strs;
        strs << n;
        string temp_str = strs.str();
        const char *cstr = temp_str.c_str();
        strcpy(hello, cstr);
        send(sock , hello , strlen(hello) , 0 ); 
	    cout<<"Sent seomething\n"; 
	    valread = read( sock , buffer, 1024); 
	    cout<<"recieved:"<<buffer<<endl;
        n = n+10;
    }
	 
	return 0; 
} 
