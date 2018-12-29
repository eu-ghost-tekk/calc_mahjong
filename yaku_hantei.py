#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig
from mahjong.meld import Meld
import generate_melds as gm

def calc(manz, pinz, souz, honorz, finish_tile, meldz):
    
    calculator = HandCalculator()

    # we had to use all 14 tiles in that array
    tiles = TilesConverter.string_to_136_array(sou=souz, pin=pinz, man=manz, honors=honorz)

    if finish_tile[0] == 'man':
        win_tile = TilesConverter.string_to_136_array(man=finish_tile[1])[0]    
    elif finish_tile[0] == 'pin':
        win_tile = TilesConverter.string_to_136_array(pin=finish_tile[1])[0]    
    elif finish_tile[0] == 'sou':
        win_tile = TilesConverter.string_to_136_array(sou=finish_tile[1])[0]    
    else:
        win_tile = TilesConverter.string_to_136_array(honors=finish_tile[1])[0]
        
    melds = gm.mkmelds(meldz)

    result = calculator.estimate_hand_value(tiles, win_tile, melds = melds, config = HandConfig())

    print(result.han, result.fu)
    print(result.cost['main'])
    print(result.yaku)
    for fu_item in result.fu_details:
        print(fu_item)
        
##########################################
#('manz', 'pinz', 'souz', 'honors', ['上がり牌の種類', '上がり牌のインデックス'])
#honors:1-東, 2-南, 3-西, 4-北, 5-白, 6-發, 7-中
##########################################
        
calc('123', '456', '789', '11122',['honors', '2'], [['man', '123']])