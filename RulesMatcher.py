# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 21:30:48 2021

@author: asus
"""

rpath = 'Rules.xlsx'
InputPromise = {'有羽毛', '会游泳', '有黑白二色', '不会飞'}
testr = {'会游泳', '有黑白二色', '不会飞'}

def Premises(RulesPath):
    import RulesReader as RR
    Ra = RR.Rules_administrator(RulesPath)
    Ra._read_rules()
    return Ra._show_premises()

def Rules_adder(RulesPath, NewRule, NewRulesPath = None, ifSave = True):
    import RulesReader as RR
    Ra = RR.Rules_administrator(RulesPath)
    Ra._read_rules()
    Ra.add_rule(NewRule, NewRulesPath, ifSave)
    
def Rules_deleter(RulesPath, OldRule, NewRulesPath = None, ifSave = True):
    import RulesReader as RR
    Ra = RR.Rules_administrator(RulesPath)
    Ra._read_rules()
    Ra.delete_rule(OldRule, NewRulesPath, ifSave)
    
def Rules_modifier(RulesPath, NewRule, OldRule, NewRulesPath = None, ifSave = True):
    import RulesReader as RR
    Ra = RR.Rules_administrator(RulesPath)
    Ra._read_rules()
    Ra.modify_rule(OldRule, NewRule, NewRulesPath, ifSave)
    
def Rules_matcher(InputPromise, RulesPath):
    """The function of matching rules by production theory~
    
    Args:
        InputPromise(set): A set of promises
        RulesPath(str): The physical loaction of the rule base
    
    Returns:
        conclusion(str): The name of an animal
    """
    import RulesReader as RR
    Ra = RR.Rules_administrator(RulesPath)
    rules = Ra._read_rules()
    rules_copy = rules.copy()
    flag = True
    conclusion = '什么都不是'
    while flag:
        i = 0
        flag = False
        for rule in rules_copy:
            existed_promise = list(rule.values())[0]
            if existed_promise.issubset(InputPromise):
                InputPromise.add(list(rule.keys())[0])
                rules_copy.pop(i)
                flag = True
                conclusion = list(rule.keys())[0]
            i += 1
    print('该动物{}'.format(conclusion))
    return '该动物{}'.format(conclusion)

if __name__ == '__main__':
    print(Premises(rpath))
    Rules_matcher(InputPromise, RulesPath = rpath)     
    Rules_matcher(testr, RulesPath = rpath)     