import sys

import grpc
import debate_pb2
import debate_pb2_grpc

def run():
    direction = sys.argv[1]
    if direction is "answer":
        print(answer(sys.argv[2]))

def answer(question):
    channel = grpc.insecure_channel("localhost:50050")
    stub = debate_pb2_grpc.
