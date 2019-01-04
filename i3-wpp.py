#!/usr/bin/env python3

import i3ipc
import sys

path2wallpappers = str(sys.argv[1])

# Create the Connection object that can be used to send commands and subscribe
# to events.
i3 = i3ipc.Connection()

# Define a callback to be called when you switch workspaces.
def on_workspace_focus(self, e):
    # The first parameter is the connection to the ipc and the second is an object
    # with the data of the event sent from i3.
    if e.current:
       i3.command('exec --no-startup-id feh --bg-fill %s/img%s' %
               (path2wallpappers, e.current.name))

# Subscribe to events
i3.on('workspace::focus', on_workspace_focus)

# Start the main loop and wait for events to come in.
i3.main()
