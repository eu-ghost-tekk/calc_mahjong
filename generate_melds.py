#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mahjong.meld import Meld
from mahjong.tile import TilesConverter

def mkmelds(meldz):

    #meldz = [['man', '123'], ['honors', '111'], ['honors', '5555']]
    melds = []
    
    for i in range(len(meldz)):
        if list(meldz[i][1])[0] != list(meldz[i][1])[1]:#chi
            if meldz[i][0] == 'man':
                melds.append(Meld(meld_type=Meld.CHI, tiles=TilesConverter.string_to_136_array(man=meldz[i][1])))
            if meldz[i][0] == 'pin':
                melds.append(Meld(meld_type=Meld.CHI, tiles=TilesConverter.string_to_136_array(pin=meldz[i][1])))
            if meldz[i][0] == 'sou':
                melds.append(Meld(meld_type=Meld.CHI, tiles=TilesConverter.string_to_136_array(sou=meldz[i][1])))
        elif len(list(meldz[i][1])) == 3:#pon
            if meldz[i][0] == 'man':
                melds.append(Meld(meld_type=Meld.PON, tiles=TilesConverter.string_to_136_array(man=meldz[i][1])))
            if meldz[i][0] == 'pin':
                melds.append(Meld(meld_type=Meld.PON, tiles=TilesConverter.string_to_136_array(pin=meldz[i][1])))
            if meldz[i][0] == 'sou':
                melds.append(Meld(meld_type=Meld.PON, tiles=TilesConverter.string_to_136_array(sou=meldz[i][1])))
            if meldz[i][0] == 'honors':
                melds.append(Meld(meld_type=Meld.PON, tiles=TilesConverter.string_to_136_array(honors=meldz[i][1])))
        else:#kan
            if meldz[i][0] == 'man':
                melds.append(Meld(meld_type=Meld.KAN, tiles=TilesConverter.string_to_136_array(man=meldz[i][1])))
            if meldz[i][0] == 'pin':
                melds.append(Meld(meld_type=Meld.KAN, tiles=TilesConverter.string_to_136_array(man=meldz[i][1])))
            if meldz[i][0] == 'sou':
                melds.append(Meld(meld_type=Meld.KAN, tiles=TilesConverter.string_to_136_array(man=meldz[i][1])))
            if meldz[i][0] == 'honors':
                melds.append(Meld(meld_type=Meld.KAN, tiles=TilesConverter.string_to_136_array(man=meldz[i][1])))
                
    return melds