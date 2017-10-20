#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   Takahiro Oshima <tarotora51@gmail.com>
# License:  MIT License
# Created:  2017-10-20
#
import requests
import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash=1, proof=100)

    def new_block(self):
        # 新しいブロックを作りチェーンに加える
        pass

    def new_transaction(self):
        """
        次に採掘されるブロックに加える新しいトランザクションを作る
        :param sender: <str> 送信者のアドレス
        :param recipient: <str> 受信者のアドレス
        :param amount: <int> 量
        :return: <int> このトランザクションを含むブロックのアドレス
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        pass

    @property
    def last_block(self):
        pass

    


if __name__ == "__main__":
