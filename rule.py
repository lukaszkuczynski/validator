from abc import abstractmethod

class ValidationException(Exception):
    def __init__(self, msg):
        super(ValidationException, self).__init__(msg)



class RuleFactory:


    def for_definition(self, dict):
        if 'not_null' in dict:
            return NotNullRule(dict['not_null'])
        elif 'missing' in dict:
            return MissingFieldRule(dict['missing'])
        else:
            raise NotImplementedError("No valid type for rule given.")


class Rule:

    @abstractmethod
    def check(self, doc):
        pass


class NotNullRule(Rule):

    def __init__(self, cfg):
        self.fields = cfg['fields']

    def check(self, doc):
        for key in doc:
            if key in self.fields:
                if doc[key] is None:
                    raise ValidationException("Field "+key+" is null")


class MissingFieldRule(Rule):

    def __init__(self, cfg):
        self.fields = cfg['fields']

    def check(self, doc):
        for field in self.fields:
            if field not in doc:
                raise ValidationException("Missing field "+field)
