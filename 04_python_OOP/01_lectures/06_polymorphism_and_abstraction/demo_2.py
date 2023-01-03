class Rule:
    def check_rule(self):
        pass


class HeaderRule(Rule):
    def check_headers(self):
        return True

    def check_rule(self):
        return self.check_headers()


class IntegerRule(Rule):
    def check_age_column(self):
        return True

    def check_kg(self):
        return True

    def check_rule(self):
        return self.check_age_column() and self.check_kg()


class NameRule(Rule):
    def check_rule(self):
        return True


class AgeRule(Rule):
    def check_rule(self):
        return True


rules = (NameRule(), IntegerRule(), HeaderRule())


class RuleEngine():
    def apply(self):
        for rule in rules:
            if not rule.check_rule():
                raise ValueError("Please send report for invalid file")


if __name__ == "__main__":
    engine = RuleEngine
