#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 16:57:53 2023

@author: snipermonke01
"""

from web3 import Web3

import os
import json
import time

import telegram
from telegram import ParseMode

from numerize import numerize

base_dir = os.path.join(os.path.dirname(__file__))


def get_contract_object(web3_obj,
                        contract_address: str,
                        abi_filepath):

    abi_json = json.load(open(abi_filepath))

    return web3_obj.eth.contract(address=contract_address,
                                 abi=abi_json)


plan_ids_map = {201: {"protocol": "GMX",
                      "multisig_address": "0xB6fd0BDb1432b2c77170933120079f436F3bB4fa",
                      "proposal": "https://forum.arbitrum.foundation/t/gmx-final-stip-round-1/17426",
                      "url": "https://gmx.io/#/"},

                202: {"protocol": "Radiant",
                      "multisig_address": "0x712e3396f039243abda1858b5b85cdcdd0878976",
                      "proposal": "https://forum.arbitrum.foundation/t/radiant-final-stip-round-1/16929",
                      "url": "https://radiant.capital/"},

                203: {"protocol": "Pendle",
                      "multisig_address": "0x7877adfaded756f3248a0ebfe8ac2e2ef87b75ac",
                      "proposal": "https://forum.arbitrum.foundation/t/pendle-final-stip-round-1/17234",
                      "url": "https://www.pendle.finance/"},

                204: {"protocol": "Rysk",
                      "multisig_address": "0xc051b37c2b4f103d397074eee54573765df83a72",
                      "proposal": "https://forum.arbitrum.foundation/t/rysk-final-stip-round-1/17194",
                      "url": "https://www.rysk.finance/"},

                205: {"protocol": "Silo Finance",
                      "multisig_address": "0x865a1da42d512d8854c7b0599c962f67f5a5a9d9",
                      "proposal": "https://forum.arbitrum.foundation/t/silo-finance-final-stip-round-1/16640",
                      "url": "https://www.silo.finance/"},

                206: {"protocol": "Stella",
                      "multisig_address": "0x2e39fbb069accd1959d003297250129879eb20a1",
                      "proposal": "https://forum.arbitrum.foundation/t/stella-final-stip-round-1/17328",
                      "url": "https://stellaxyz.io/"},

                207: {"protocol": "Gamma",
                      "multisig_address": "0x8beff353fcb2e288fdffbb0b2b61b4c76dc700df",
                      "proposal": "https://forum.arbitrum.foundation/t/gamma-final-stip-round-1/16691",
                      "url": "https://www.gamma.xyz/"},

                208: {"protocol": "Angle Protocol",
                      "multisig_address": "0xaa2daccab539649d1839772c625108674154df0b",
                      "proposal": "https://forum.arbitrum.foundation/t/angle-protocol-final-stip-round-1/17104",
                      "url": "https://www.angle.money/"},

                209: {"protocol": "Vertex",
                      "multisig_address": "0x66993ca98a1ecf4f746fcdbdedfc69e95529fb0e",
                      "proposal": "https://forum.arbitrum.foundation/t/vertex-protocol-final-stip-round-1/17435",
                      "url": "https://vertexprotocol.com/"},

                210: {"protocol": "Stable Lab",
                      "multisig_address": "0x9c489e4efba90a67299c1097a8628e233c33bb7b",
                      "proposal": "https://forum.arbitrum.foundation/t/arbitrums-short-term-incentive-program-arbitrum-improvement-proposal/16131",
                      "url": "https://www.stablelab.xyz/"},

                211: {"protocol": "Perennial",
                      "multisig_address": "0xcc2a6ef429b402f7d8d72d6aecd6dfd0d787acff",
                      "proposal": "https://forum.arbitrum.foundation/t/perennial-finance-final-stip-round-1/17388",
                      "url": "https://perennial.finance/"},

                212: {"protocol": "WINR",
                      "multisig_address": "0x221b0439b50dbca3f6fc698d74636cabeaf96307",
                      "proposal": "https://forum.arbitrum.foundation/t/winr-protocol-final-stip-round-1/16755",
                      "url": "https://winr.games/"},

                213: {"protocol": "Dolomite",
                      "multisig_address": "0xa75c21c5be284122a87a37a76cc6c4dd3e55a1d4",
                      "proposal": "https://forum.arbitrum.foundation/t/dolomite-final-stip-round-1/16818",
                      "url": "https://dolomite.io/"},

                268: {"protocol": "Premia",
                      "multisig_address": "0xa079C6B032133b95Cf8b3d273D27eeb6B110a469",
                      "proposal": "https://forum.arbitrum.foundation/t/premia-final-stip-round-1/17504",
                      "url": "https://premia.blue/"},

                269: {"protocol": "Lodestar",
                      "multisig_address": "0xfA62A3A0722a0aF7739c23a361E2285F5B75ecE7",
                      "proposal": "https://forum.arbitrum.foundation/t/lodestar-finance-final-stip-round-1/16981",
                      "url": "https://www.lodestarfinance.io/"},

                270: {"protocol": "MUX",
                      "multisig_address": "0x4Fa610DD115e790B8768A482Fc366803534e9Adc",
                      "proposal": "https://forum.arbitrum.foundation/t/mux-protocol-final-stip-round-1/17540",
                      "url": "https://mux.network/#/"},

                271: {"protocol": "Balancer",
                      "multisig_address": "0xb6BfF54589f269E248f99D5956f1fDD5b014D50e",
                      "proposal": "https://forum.arbitrum.foundation/t/balancer-final-stip-round-1/16689",
                      "url": "https://balancer.fi/"},

                272: {"protocol": "Timeswap",
                      "multisig_address": "0x3B29b39b37afec28EC636f0f9e16290e28b5A377",
                      "proposal": "https://forum.arbitrum.foundation/t/timeswap-final-stip-round-1/17344",
                      "url": "https://timeswap.io/"},

                273: {"protocol": "Trade Joe",
                      "multisig_address": "0x0A56ba03cC70582EA512f44B86d19aCDd631f475",
                      "proposal": "https://forum.arbitrum.foundation/t/trader-joe-final-stip-round-1/17013",
                      "url": "https://traderjoexyz.com/arbitrum"},

                274: {"protocol": "Umami",
                      "multisig_address": "0x8E52cA5A7a9249431F03d60D79DDA5EAB4930178",
                      "proposal": "https://forum.arbitrum.foundation/t/umami-finance-final-stip-round-1/17203",
                      "url": "https://umami.finance/"},

                275: {"protocol": "Dopex",
                      "multisig_address": "0x880C3cdCA73254D466f9c716248339dE88e4a97D",
                      "proposal": "https://forum.arbitrum.foundation/t/dopex-final-stip-round-1/16645",
                      "url": "https://www.dopex.io/"},

                276: {"protocol": "Frax",
                      "multisig_address": "0xe61D9ed1e5Dc261D1e90a99304fADCef2c76FD10",
                      "proposal": "https://forum.arbitrum.foundation/t/frax-finance-final-stip-round-1/16579",
                      "url": "https://frax.finance/"},

                277: {"protocol": "Galxe",
                      "multisig_address": "0xeF80A06933Ad67F16a234e10693B2f935e4a9130",
                      "proposal": "https://forum.arbitrum.foundation/t/galxe-final-stip-round-1/17561",
                      "url": "https://galxe.com/"},

                278: {"protocol": "Tally",
                      "multisig_address": "0x50Db58E1774CB7922d1bF96a267b52e8bb41c0ce",
                      "proposal": "https://forum.arbitrum.foundation/t/tally-final-stip-round-1/17557",
                      "url": "https://www.tally.xyz/"},

                279: {"protocol": "Camelot",
                      "multisig_address": "0xEf9162fE27d319723feF7183348c87304a134c4B",
                      "proposal": "https://forum.arbitrum.foundation/t/camelot-final-stip-round-1/17200",
                      "url": "https://camelot.exchange/"},

                280: {"protocol": "Good Entry",
                      "multisig_address": "0x4827C7057B2e95aF587D738e9d49Df9886d047D2",
                      "proposal": "https://forum.arbitrum.foundation/t/good-entry-final-stip-round-1/16763",
                      "url": "https://goodentry.io/"},
                }


def _monitor(first_block=None):

    rpc = "https://arbitrum.sakurarpc.io"
    web3_obj = web3_obj = Web3(Web3.HTTPProvider(rpc))
    contract_address = "0x2CDE9919e81b20B4B33DD562a48a84b54C48F00C"
    abi_filepath = os.path.join(base_dir,
                                "contracts",
                                "token_vesting_plans.json")

    contract_obj = get_contract_object(web3_obj,
                                       contract_address,
                                       abi_filepath)

    if first_block is None:
        first_block = web3_obj.eth.block_number
        latest_block = first_block
    else:
        latest_block = web3_obj.eth.block_number
    print("Checking between blocks {} to {}".format(first_block, latest_block))
    query_output = contract_obj.events.PlanRedeemed.getLogs(fromBlock=first_block,
                                                            toBlock=latest_block)

    messages = []

    for output in query_output:

        try:
            protocol_name = plan_ids_map[output['args']['id']]["protocol"]
            multisig = 'https://arbiscan.io/address/{}'.format(
                plan_ids_map[output['args']['id']]["multisig_address"])

            amount_redeemed = int(output['args']['amountRedeemed'])/10**18
            remaining = int(output['args']['planRemainder'])/10**18
            txn = 'https://arbiscan.io/tx/{}'.format(output['transactionHash'].hex())
            block_number = output['blockNumber']
            protocol_url = "<a href='{}'>{}</a>".format(plan_ids_map[output['args']['id']]["url"],
                                                        protocol_name)
            txn_txt = "<a href='{}'>Txn</a>".format(txn)
            multi_sig_txt = "<a href='{}'>Multisig</a>".format(multisig)
            proposal = "<a href='{}'>Proposal</a>".format(
                plan_ids_map[output['args']['id']]["proposal"])

            message_header = "\U0001F7E6 New STIP Redemption! \U0001F7E6\n\n"
            message_body1 = "Protocol: {}\nAmount Redeemed: {} Arb\nRemaining to Redeem: {} Arb\n".format(
                protocol_url, numerize.numerize(amount_redeemed), numerize.numerize(remaining))
            message_body2 = "Redeemed at block: {}\n\n".format(block_number)
            message_tail = "{} | {} | {}".format(txn_txt, multi_sig_txt, proposal)

            message = "{}{}{}{}".format(message_header, message_body1, message_body2, message_tail)
            messages += [message]

        except KeyError as e:

            print("Not a STIP claim!")

    return messages, latest_block

bot_token = ""
chat_id = ""

bot = telegram.Bot(token=bot_token)

first_block = None
while True:
    try:
        messages, first_block = _monitor(first_block)
        for message in messages:
            print(message)
            bot.sendMessage(chat_id=chat_id,
                            text=message,
                            parse_mode=ParseMode.HTML,
                            disable_web_page_preview=True)
            pass
        print("Sleeping for 60s zZzZz")
        time.sleep(60)
    except Exception as e:
        print(e)
        print("Unhandled error, sleeping for 60s zZzZz")
        time.sleep(60)
