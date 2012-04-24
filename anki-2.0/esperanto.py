# -*- coding: utf-8 -*-
#
# esperanto.py ---  Esperanto Support for Anki 2.0
#
# Copyright (C) 2010-2012 Peter Carroll <peter at peterjcarroll dot com>
#
# Anki 2.0 version created: 2012-04-24
#
# Anki 1.2 version created: 2010-08-04 
# Juan Miguel Cejuela's German Support plugin was used as a model
# for this plugin
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

from aqt import mw
import re
from anki.hooks import addHook
import anki.stdmodels

   
def addEsperantoModel(col):
    mm = col.models
    m = mm.new(_("Esperanto"))
    fm = mm.newField(_("Fronto"))
    mm.addField(m, fm)
    fm = mm.newField(_("Dorso"))
    mm.addField(m, fm)
    t = mm.newTemplate(_(u"Antaŭen"))
    t['qfmt'] = "{{Fronto}}"
    t['afmt'] = t['qfmt'] + "\n\n<hr id=answer>\n\n{{Dorso}}"
    mm.addTemplate(m, t)
    mm.add(m)
    return m

def replaceWithHats(value):
    tmp = re.sub("cx", u"ĉ", value)
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
    return tmp

def onFocusLost(flag, n, fidx):
    if "esperanto" not in n.model()['name'].lower():
        return flag
    for (name, value) in n.items():
        updatedValue = replaceWithHats(value)
        if value != updatedValue:
            n[name] = updatedValue
            flag = True
    n.flush()
    return flag

anki.stdmodels.models.append((_("Esperanto"), addEsperantoModel))
        
addHook('editFocusLost', onFocusLost)
