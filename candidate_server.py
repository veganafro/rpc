import grpc
import debate_pb2
import debate_pb2_grpc

import consultation_pb2
import consultation_pb2_grpc

from random import randint

interrogatives = set(["why", "what", "how", "who", "when"])

class Candidate(debate_pb2_grpc.CandidateServicer):
    def Answer(self, request, context):
        question = list(map(
            lambda x: x.lower(),
            request.question.split(" ")
        ))
        
        if question[0] not in interrogatives:
            replies = ["your 3 cent titanium tax goes too far",
                "your 3 cent titanium tax doesn't go too far enough"
            ]
            return debate_pb2.AnswerReply(answer=replies[randint(0, 1)])
        for idx, word in question:
            if word is "you":
                question[idx] = "I"
            elif word is "your":
                question[idx] = "my"
        channel = grpc.insecure_channel("localhost:50051")
        stub = consultation_pb2_grpc.CampaignManagerStub(channel)
        retort = stub.Retort(
            consultation_pb2.RetortRequest(original_question=" ".join(question))
        )
        return debate_pb2.AnswerReply(
            answer="You asked me " + " ".join(question) + " but I want to say that" + retort.retort
        )
