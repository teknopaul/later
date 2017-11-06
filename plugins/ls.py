"""
This plugin provides ls pretty printed and ordered
"""

_HOOKS=None

def issue_compare(x, y):
	if x.properties.has_key("priority") and y.properties.has_key("priority"):
		return int(x.properties["priority"]) - int(y.properties["priority"])
	elif x.properties.has_key("priority"):
		return 1
	elif y.properties.has_key("priority"):
		return -1
	else:
		return 1

def shortString(self):
	"""One line representation"""
	i = self.msg.find("\n")
	if i < 0:
		i = None
	string = self.msg[:i]
	status = self.properties.get("status", "?")
	return " %s  %-50s %s"%(self.guid[:8], string, status) 

def cmd_ls(args):
	"""By default lists all issues, which are not closed."""
	

	issues = (_HOOKS.be_load_issue(guid) for guid in _HOOKS.be_all_guids())

	# Filtering for bugs
	if args.count('bug'):
		issues = (iss for iss in issues if iss.properties.has_key("type") and iss.properties["type"] == "bug")
		args.remove('bug')

	if args.count('feat'):
		issues = (iss for iss in issues if iss.properties.has_key("type") and iss.properties["type"] == "feat")
		args.remove('feat')

	issues = (iss for iss in issues if iss.properties["status"] != "closed")

	issues = sorted(issues, cmp=issue_compare, reverse=True )

	for issue in issues:
		if issue.properties.has_key("priority") and int(issue.properties["priority"]) > 8:
			print("\033[31m" + issue.shortString() + "\033[0m")
		elif issue.properties.has_key("priority") and int(issue.properties["priority"]) >= 2:
			print("\033[93m" + issue.shortString() + "\033[0m")
		elif issue.properties.has_key("priority") and int(issue.properties["priority"]) >= 1:
			print("\033[32m" + issue.shortString() + "\033[0m")
		else:
			print("\033[02m" + issue.shortString() + "\033[0m")



def plugin_init(hooks):
	global _HOOKS
	hooks["cmd_ls"] = cmd_ls
	_HOOKS = hooks

