#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig
from mahjong.meld import Meld

calculator = HandCalculator()

# we had to use all 14 tiles in that array
tiles = TilesConverter.string_to_136_array(man='11223344556677', pin='None', sou='None')
win_tile = TilesConverter.string_to_136_array(man='7')[0]

result = calculator.estimate_hand_value(tiles, win_tile)

print(result.han, result.fu)
print(result.cost['main'])
print(result.yaku)
for fu_item in result.fu_details:
    print(fu_item)