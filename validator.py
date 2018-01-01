from rule import RuleFactory


def validate(docs, rule_definitions):
    print(rule_definitions)
    factory = RuleFactory()
    rules = [factory.for_definition(rule_definitions[key]) for key in rule_definitions]
    for doc in docs:
        for rule in rules:
            rule.check(doc)