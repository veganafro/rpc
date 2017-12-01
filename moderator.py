import sys

import grpc
import debate_pb2
import debate_pb2_grpc

def run():
    direction = sys.argv[1]
    if direction == "answer":
        print(answer(" ".join(sys.argv[2:])))
    elif direction == "elaborate":
        topic = get_topic(sys.argv[2:])
        blah_run = list(map(
            int,
            filter(
                lambda x: x.isdigit(),
                sys.argv
            )
        ))
        print(elaborate(topic, blah_run))


def answer(question):
    channel = grpc.insecure_channel("localhost:50050")
    stub = debate_pb2_grpc.CandidateStub(channel)
    reply = stub.Answer(
        debate_pb2.AnswerRequest(question=question)
    )
    return reply.answer


def elaborate(topic, blah_run):
    channel = grpc.insecure_channel("localhost:50050")
    stub = debate_pb2_grpc.CandidateStub(channel)
    reply = stub.Elaborate(
        debate_pb2.ElaborateRequest(topic=topic, blah_run=blah_run)
    )
    return reply.answer


def get_topic(args):
    ending_index = 0
    while ending_index < len(args):
        if args[ending_index].isdigit():
            return " ".join(args[:ending_index])
        ending_index += 1
    return " ".join(args[:ending_index])


if __name__ == "__main__":
    run()
