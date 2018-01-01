from unittest import TestCase
import yaml
from validator import validate
from rule import ValidationException


class ValidatorTest(TestCase):

    def test_validator_fails_at_missingfield(self):
        with open('test_validation_rules.yml') as f:
            config = yaml.load(f)
            docs = [
                {"first_name": "Luke"}
            ]
            print(config)
            try:
                validate(docs=docs, rule_definitions=config)
                self.fail("Should fail on missing age field")
            except ValidationException as e:
                pass

    def test_validator_fails_at_field_none(self):
        with open('test_validation_rules.yml') as f:
            config = yaml.load(f)
            docs = [
                {"first_name": None, "age": 10}
            ]
            print(config)
            try:
                validate(docs=docs, rule_definitions=config)
                self.fail("Should fail on none first_name")
            except ValidationException as e:
                print(e)
                pass