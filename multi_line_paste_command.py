import sublime
import sublime_plugin

class MultiLinePasteCommand(sublime_plugin.TextCommand):
    """Go to definition command"""
    def run(self, edit):
        self.view.run_command("paste")
        for i in sublime.get_clipboard().split("\n"):
            self.view.run_command("select_lines", { "forward": False })
        self.view.run_command("move_to", {"to": "eol"})