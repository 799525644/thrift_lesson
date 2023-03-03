from match_client.match import Match
from match_client.match.ttypes import User

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

# 用于接收终端信息
from sys import stdin

def operate(op, user_id, username, score):
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = Match.Client(protocol)

    # Connect!
    transport.open()

    user = User(user_id, username, score)
    if op == "add":
        client.add_user(user, "")
    elif op == "remove":
        client.remove_user(user, "")
    # Close!
    transport.close()

# 定义main函数从
def main():
    for line in stdin:
        op, user_id, username, score = line.split(' ')
        operate(op, int(user_id), username, int(score))

# __name__获取执行对象，当直接调用时执行该语句，不直接调用时不执行
if __name__ == "__main__":
    main()
