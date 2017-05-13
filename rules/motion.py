from dragonfly import Choice, MappingRule, Key, IntegerRef, RuleRef
from .quick_search import QuickSearchRule
from ..choices.motion import motionChoice
from ..choices.uncountableMotion import uncountableMotionChoice
from ..lib.execute_factory import executeFactory, multipleExecuteFactory

class MotionRule(MappingRule):
    exported = True
    mapping = {
        "[<n>] <motion>": Key("%(n)d, %(motion)s"),
        "<quick_search>": executeFactory('quick_search'),
        "go <uncountableMotion>": Key("%(uncountableMotion)s"),
    }
    extras = [
        IntegerRef("n", 1, 10),
        motionChoice("motion"),
        uncountableMotionChoice("uncountableMotion"),
        RuleRef(rule = QuickSearchRule(name = "motion_qsearch"), name = "quick_search"),
    ]
    defaults = {
        "n": 1,
    }