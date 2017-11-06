![](later_bug.png)
# Later


A simple command-line issue tracker for Linux, forked from (https://github.com/qznc/later)

Keeps bugs in text files called _./.later/\<guid\>.issue_

Why? [discussion](https://news.ycombinator.com/item?id=1620168)  because the venerable _sd_ has stopped working with latest Ubuntu releases.

# Install

Clone the github repository https://github.com/teknopaul/later.git

Install with

	sudo ./install

Set you _EDITOR_ variable.

## Usage

	later cmd [args]

_cd_ to your project directory.

	later init
	later bug "description here..."

## Commands

- **init** - create .later dir in current directory
- **bug** "msg" - new bug
- **feat** "msg" - new feature
- **add** "msg" - new issue
- **ls** \<bug|feat\> - show unclosed issues ordered by priority
- **edit** \<guid\> - edit issue with the given guid
- **show|cat** \<guid\> - show issue \<guid\> completely
- **close** \<guid\> - set status to closed
- **confirm** \<guid\> - set status to confirmed
- **assign** \<guid\> \<developer\> - set responsible to developer
- **list** - show all issues in short form
- **help** \<cmd\> - shows documentation for \<cmd\>
- **schedule** - calculates/show deadlines
- **htmlreport** - generate html report
- **delete|del|rm** \<guid\> - delete issue \<guid\>
- **delete-closed** - delete all closed issues
- **list-subdirs** - show issue list of subdirs
- **revision** - manage revisions