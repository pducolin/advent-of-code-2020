import re

DEBUG = False


def dbg_print(s):
    if DEBUG:
        print(s)


def parse_letters(option, index):
    chars = ''
    while index < len(option) and option[index] != '"':
        chars += option[index]
        index += 1
    return chars, index


def parse_number(option, index):
    number = ''
    while index < len(option) and option[index].isdigit():
        number += option[index]
        index += 1
    return int(number), index


def parse_lexemes_in_rule(rule):
    rule_lexemes = []
    i = 0
    while i < len(rule):
        ch = rule[i]
        if ch == '"':
            alpha, i = parse_letters(rule, i + 1)
            rule_lexemes.append(alpha)
            continue
        if ch.isdigit():
            number, i = parse_number(rule, i)
            rule_lexemes.append(number)
            continue
        if ch == '|':
            rule_lexemes.append('|')
        i += 1
    return rule_lexemes


# Started from 20, obtained same result with 5
MAX_RECURSION_COUNT = 5


def solve_rule(rules_dict, regex_dict, index):
    dbg_print(f'Solving rule {index}')
    # return if already solved
    if index in regex_dict:
        return regex_dict[index]
    rule = rules_dict[index]

    if index == 8:
        # change rule 8: 42 to 8: 42+
        group_42 = solve_rule(rules_dict, regex_dict, 42)
        regex = f'({group_42})+'
        regex_dict[index] = regex
        dbg_print(f'Solved rule {index}')
        return regex_dict[index]

    if index == 11:
        # change rule 11: 42 31 to 42 31 | 42 11 31 recursively
        group_42 = solve_rule(rules_dict, regex_dict, 42)
        group_31 = solve_rule(rules_dict, regex_dict, 31)
        rules_11 = []
        for i in range(1, MAX_RECURSION_COUNT):
            rules_11.append(f'({group_42}){{{i}}}({group_31}){{{i}}}')
        regex = '({})'.format('|'.join(rules_11))
        regex_dict[index] = regex
        dbg_print(f'Solved rule {index}')
        return regex_dict[index]

    regex = ''
    for lexeme in rule:
        if type(lexeme) is not int:
            regex += lexeme
            continue
        sub_index = int(lexeme)
        sub_rule = solve_rule(rules_dict, regex_dict, sub_index)
        regex += f'({sub_rule})'

    regex_dict[index] = regex
    dbg_print(f'Solved rule {index}')
    return regex_dict[index]


def parse_rules_dict(rules):
    rules_dict = {}
    for r in rules:
        index, rule = [x.strip() for x in r.split(':')]
        rules_dict[int(index)] = parse_lexemes_in_rule(rule)
    dbg_print(f'Rules dict: {rules_dict}')
    return rules_dict


def solution(data):
    rules, messages = [x.splitlines() for x in data.split('\n\n')]
    rules_dict = parse_rules_dict(rules)
    regex_dict = {}
    pattern_at_0 = solve_rule(rules_dict, regex_dict, 0)
    counter = 0
    for message in messages:
        if re.fullmatch(pattern_at_0, message):
            counter += 1
    return counter
