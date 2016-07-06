Main Window
===========

Overview
++++++++

.. image:: _images/main_window_sections.png
    :target: _images/main_window_sections.png
    :alt:    Back In Time main window
    :align:  left


Main Toolbar
++++++++++++

.. |take_snapshot|      image:: _images/document-save.svg
.. |refresh_snapshot|   image:: _images/view-refresh.svg
.. |snapshot_name|      image:: _images/gtk-edit.svg
.. |remove_snapshot|    image:: _images/edit-delete.svg
.. |view_snapshot_log|  image:: _images/text-plain.svg
.. |view_last_log|      image:: _images/document-new.svg
.. |settings|           image:: _images/gtk-preferences.svg
.. |shutdown|           image:: _images/system-shutdown.svg
.. |exit|               image:: _images/window-close.svg
.. |help|               image:: _images/help-contents.svg

|take_snapshot| Take Snapshot
    Take a new Snapshot in background. The main window can be closed during
    taking the snapshot. You can alternative take a new Snapshot with
    ``checksums`` option enabled. This will calculate checksums for every
    file to decide if the file has changed. Normal behavior is to only compare
    files size and modification time. This takes a lot more time but it will
    make sure, the destination files won't be corrupt.

|refresh_snapshot| Refresh Snapshots List
    Refresh the Snapshots in Timeline.

|snapshot_name| Snapshot Name
    Add a name for a Snapshot so you can easily identify it later.
    If ``Don't remove named snapshots`` in
    :menuselection:`Settings --> Auto Remove` is enabled this will also prevent
    the Snapshot from being removed.

    If this button is grayed out you need to select a snapshot in `Timeline`_.

|remove_snapshot| Remove Snapshot
    Remove one or more Snapshots from Timeline. ``Now`` can not be removed as
    this is no Snapshot but the live view of the local filesystem.

    If this button is grayed out you need to select a snapshot in `Timeline`_.

|view_snapshot_log| View Snapshot Log
    View the log of the selected Snapshot. This is grayed out if ``Now`` is
    selected.

    If this button is grayed out you need to select a snapshot in `Timeline`_.

|view_last_log| View Last Log
    View the log from the last snapshot attempt.

|settings| Settings
    Open :doc:`/settings`.

|shutdown| Shutdown System after Snapshot has finished
    Shutdown the computer and switch power off after a snapshot has finished.
    The main window must stay open for this. If shutdown is not supported on
    the system this button will be grayed out.

|exit| Exit
    Close the main window. Running Snapshots will remain in background.

|help| Help
    Menu with links to this help, FAQ, report bugs...

Files Toolbar
+++++++++++++

.. |up|             image:: _images/go-up.svg
.. |show_hidden|    image:: _images/show-hidden.svg
.. |restore|        image:: _images/edit-undo.svg
                        :width: 16
                        :height: 16
.. |restore_to|     image:: _images/document-revert.svg
.. |snapshots|      image:: _images/file-manager.svg

|up| Up
    Go to the parent folder.

|show_hidden| Show hidden files
    Toggle hidden files (starting with a dot) to be shown in files view.

|restore| Restore
    Restore selected files or folders. This button has a submenu (hold down
    the button). Default action is ``Restore``.

    If this button is grayed out you need to select a snapshot in `Timeline`_.

    |restore| Restore
        Restore the selected files or folders to the original destination.

    |restore_to| Restore to...
        Restore the selected files or folders to a new destination.

    |restore| Restore '/path'
        Restore the currently shown folder and all its content to the original
        destination.

    |restore_to| Restore '/path' to...
        Restore the currently shown folder and all its content to a new
        destination.

    |restore| Restore and delete new files
        Restore selected files or folders to the original destination and
        delete files/folders in which are not in the snapshot. This will also
        delete files/folders which where excluded during taking the snapshot!
        Be extremely careful!!!

    |restore| Restore '/path' and delete new files
        Restore the currently shown folder and all its content to the original
        destination and delete files/folders in which are not in the snapshot.
        This will also delete files/folders which where excluded during taking
        the snapshot! Be extremely careful!!!

|snapshots| Snapshots
    Open :doc:`/snapshotsdialog`.


Timeline
++++++++

The Timeline lists all Snapshots which where already taken. You can browse them
to see its contents in right hand `Files View`. The first item ``Now`` is not
a Snapshot. It is a live view on the local filesystem. It shows exact the same
as your normal file browser. Multi selection is possible to remove multiple
Snapshots altogether.


Files View
++++++++++

Statusbar
+++++++++
