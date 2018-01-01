from unittest import TestCase
from rule import NotNullRule, MissingFieldRule
from rule import ValidationException, RuleFactory


class NotRuleTest(TestCase):

    def test_not_null_rule_is_ok_when_field_is_ok(self):
        rule = NotNullRule({
            "fields": ['important']}
        )
        doc = {
            'important': None
        }
        try:
            rule.check(doc)
            self.fail("Should raise ValidationException as field is None")
        except ValidationException as e:
            pass


class MissingFieldTest(TestCase):

    def test_missing_field_rule_should_raise_ValidationException_when_doc_is_missing_the_field(self):
        rule = MissingFieldRule({
            "fields": ['importante']
        })
        doc = {
            'other_field': '1'
        }
        try:
            rule.check(doc)
            self.fail("Should raise ValidationException as field is missing")
        except ValidationException as e:
            pass


class RuleFactoryTest(TestCase):

    def test_factory_for_wrong_type_throws_Exception(self):
        factory = RuleFactory()
        try:
            factory.for_definition({})
            self.fail("Shoul throw an exception for empty or unknown definition")
        except Exception as e:
            self.assertIsInstance(e, NotImplementedError)

    def test_factory_should_resolve_all_rule_types(self):
        factory = RuleFactory()
        not_null = factory.for_definition({'not_null': {"fields": []}})
        self.assertIsInstance(not_null, NotNullRule)
        not_null = factory.for_definition({'missing': {"fields": []}})
        self.assertIsInstance(not_null, MissingFieldRule)
