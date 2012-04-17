# -*- coding: utf-8 -*-
#
# esperanto.py ---  Esperanto Support for Anki
#
# Copyright (C) 2010 Peter Carroll <peter at peterjcarroll dot com>
#
# Juan Miguel Cejuela's German Support plugin was used as a model
# for this plugin
#
# created: 2010-08-04
#
#
################################################################################
# Description:
################################################################################
#
# Features:
#       -When using the Esperanto model for your cards, the Esperanto
#           special characters will appear when you follow the letter
#           with an 'x'. Examples: 'cx' becomes 'ĉ', 'Gx' becomes 'Ĝ', 
#           'ux' becomes 'ŭ', etc.
#
################################################################################
# Use:
################################################################################
#
# Add your cards with the Esperanto Model.
#

from ankiqt import mw
import re, subprocess
from anki.utils import findTag
from anki.hooks import addHook
from anki.models import Model, CardModel, FieldModel
import anki.stdmodels


def EsperantoModel():
    m = Model(_("Esperanto"))

    #Model
    m.addFieldModel(FieldModel(u'Demando', True, True))
    m.addFieldModel(FieldModel(u'Respondo', False, False))

    #Cards
    m.addCardModel(CardModel(u"Avanulo",
                             u"%(Demando)s",
                             u"%(Respondo)s"))
    m.addCardModel(CardModel(u"Dorsflanko",
                             u"%(Respondo)s",
                             u"%(Demando)s",
                             active=False))
    m.tags = u"Esperanto"
    return m

def onFocusLost(fact, field):
    modelTag = "Esperanto"

    if not findTag(modelTag, fact.model.tags):
        return

    tmp = re.sub("cx", u"ĉ", field.value)
    tmp = re.sub("gx", u"ĝ", tmp)
    tmp = re.sub("hx", u"ĥ", tmp)
    tmp = re.sub("jx", u"ĵ", tmp)
    tmp = re.sub("sx", u"ŝ", tmp)
    tmp = re.sub("ux", u"ŭ", tmp)
    tmp = re.sub("Cx", u"Ĉ", tmp)
    tmp = re.sub("Gx", u"Ĝ", tmp)
    tmp = re.sub("Hx", u"Ĥ", tmp)
    tmp = re.sub("Jx", u"Ĵ", tmp)
    tmp = re.sub("Sx", u"Ŝ", tmp)
    tmp = re.sub("Ux", u"Ŭ", tmp)
    
    field.value = tmp
    fact[field.name] = tmp 
    
        

anki.stdmodels.models['Esperanto'] = EsperantoModel
        
addHook('fact.focusLost', onFocusLost)

mw.registerPlugin("Esperanto Support", 10)
