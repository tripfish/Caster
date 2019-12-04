from dragonfly import MappingRule

from castervoice.lib.actions import Text
from castervoice.ccr.standard import SymbolSpecs
from castervoice.ccr.vhdl.vhdl_strings import for_generate_string, if_generate_string, process_string, case_string, \
    component_declaration_string, component_string, architecture_string, entity_string
from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.state.short import R


class VHDLnon(MappingRule):
    mapping = {
        "entity":
            R(entity_string),
        "Architecture":
            R(architecture_string),
        "component":
            R(component_string),
        "component declaration":
            R(component_declaration_string),
        SymbolSpecs.SWITCH:
            R(case_string),
        SymbolSpecs.CASE:
            R(Text("case TOKEN is")),
        "process":
            R(process_string),
        "generate components":
            R(for_generate_string),
        "conditional component":
            R(if_generate_string),
    }


def get_rule():
    return VHDLnon, RuleDetails(name="vhdl companion")
