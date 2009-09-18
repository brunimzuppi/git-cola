from PyQt4.QtCore import SIGNAL

_signals = dict(edit = SIGNAL('edit'),
                checkout = SIGNAL('checkout'),
                delete = SIGNAL('delete'),
                diff = SIGNAL('diff'),
                diff_staged = SIGNAL('diff_staged'),
                diffstat = SIGNAL('diffstat'),
                difftool = SIGNAL('difftool'),
                mergetool = SIGNAL('mergetool'),
                redo = SIGNAL('redo'),
                reset_mode = SIGNAL('reset_mode'),
                show_untracked = SIGNAL('show_untracked'),
                stage = SIGNAL('stage'),
                stage_diffs = SIGNAL('stage_diffs'),
                undo = SIGNAL('undo'),
                undo_diffs = SIGNAL('undo_diffs'),
                unstage = SIGNAL('unstage'),
                unstage_diffs = SIGNAL('unstage_diffs'),
                staged_summary = SIGNAL('staged_summary'),
                modified_summary = SIGNAL('modified_summary'),
                unmerged_summary = SIGNAL('unmerged_summary'),
                untracked_summary = SIGNAL('untracked_summary'))

_signals_names = {}
for name, signal in _signals.iteritems():
    _signals_names[signal] = name

# Bring signals into the module namespace
globals().update(_signals)

def name(signal):
    """Return the name for a signal."""
    return _signals_names.get(signal, 'no-name')