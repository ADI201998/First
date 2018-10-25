#include <iostream>
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

using namespace std;

#define SERVER_PORT htons(50007)

int main() {

        char buffer[1000];
        int n;
        //char hello[10000] = 'Hello from server';
        int serverSock=socket(AF_INET, SOCK_STREAM, 0);

        sockaddr_in serverAddr;
        serverAddr.sin_family = AF_INET;
        serverAddr.sin_port = SERVER_PORT;
        serverAddr.sin_addr.s_addr = INADDR_ANY;

        /* bind (this socket, local address, address length)
           bind server socket (serverSock) to server address (serverAddr).  
           Necessary so that server can use a specific port */ 
        bind(serverSock, (struct sockaddr*)&serverAddr, sizeof(struct sockaddr));

        // wait for a client
        /* listen (this socket, request queue length) */
        listen(serverSock,1);

        while (1) {
                bzero(buffer, 1000);

                sockaddr_in clientAddr;
                socklen_t sin_size=sizeof(struct sockaddr_in);
                int clientSock=accept(serverSock,(struct sockaddr*)&clientAddr, &sin_size);

                //receive a message from a client
                while(10)
                {
                    n = read(clientSock, buffer, 500);
                    cout << "Confirmation code  " << n << endl;
                    cout << "Server received:  " << buffer << endl;

                    strcpy(buffer, "123456");
                    //write(clientSock, buffer, strlen(buffer));
                    send(clientSock , buffer , strlen(buffer) , 0 ); 
                    cout << "\nSent some value to client.\n" <<endl;
                }
                
                close(clientSock);
                sleep(1);
        }
        return 0;
}