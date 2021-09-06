from __future__ import print_function

import grpc
import hello_pb2_grpc
import hello_pb2

import logging


def run():
    with grpc.insecure_channel("localhost:30100") as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_pb2.HelloRequest(name='Emanuel'))
        print('Server responded with: ', response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()
