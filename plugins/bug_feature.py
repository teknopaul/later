"""
This plugin provides a _bug _command to create high priority issues,
and a _feat_ command for low priority 
"""

_HOOKS=None

def cmd_bug(args):
	"""Create a bug issue."""
	if not args:
		error("need message")
	if not args[0]:
		return
	issue = _HOOKS.be_new_issue()
	issue.msg = args.pop(0)
	issue.properties["priority"] = 9
	issue.properties["type"] = "bug"
	_HOOKS.be_store_issue(issue)
	print "issue stored as", issue.guid


def cmd_feature(args):
	"""Create a feature issue."""
	if not args:
		error("need message")
	if not args[0]:
		return
	issue = _HOOKS.be_new_issue()
	issue.msg = args.pop(0)
	issue.properties["priority"] = 1
	issue.properties["type"] = "feature"
	_HOOKS.be_store_issue(issue)
	print "issue stored as", issue.guid

def plugin_init(hooks):
	global _HOOKS
	hooks["cmd_bug"] = cmd_bug
	hooks["cmd_feat"] = cmd_feature
	hooks["cmd_feature"] = cmd_feature
	_HOOKS = hooks

