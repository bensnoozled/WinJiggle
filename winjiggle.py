import win32gui
import win32api
import random
import time

IGNORE = ['', 'Backup and Sync', 'Program Manager'] # Windows we don't care about
DEVICE = "\\\\.\\DISPLAY" # Standard string for device names
PIXELS = 7 # number of pixels to shift edges
PADDING = 7 # I had to manually pad some of my monitor dimensions to get things to line up correctly
FREQUENCY = .5 # number of minutes between runs

target_monitors_id = [2, 1] # Monitors to shift

target_monitors_id = [DEVICE + str(m) for m in target_monitors_id]

# Get target monitors from IDs specified above
def get_target_monitors(target_monitors):
    monitor_handles = win32api.EnumDisplayMonitors()
    targets = []
    for monitor in monitor_handles:
        monitor_info = win32api.GetMonitorInfo(monitor[0])
        if monitor_info.get('Device') in target_monitors:
            targets.append(monitor)
    return targets

# Function used as a callback when iterating through monitors
def move_window(window, target_monitors):
    # If it's hidden or in our lits, we don't need to move it
    if win32gui.IsWindowVisible(window) and win32gui.GetWindowText(window) not in IGNORE:
        mon = next((monitor for monitor in target_monitors if monitor[0] == win32api.MonitorFromWindow(window)), None)
        if mon:
            # Coordinates of the window in question and the dimensions of the monitor
            window_cords = win32gui.GetWindowRect(window)
            monitor_dims = mon[2]

            # Randomly compute some number of pixels to move the window
            top_x = random.randint(window_cords[0] - PIXELS, window_cords[0] + PIXELS)
            top_y = random.randint(window_cords[1] - PIXELS, window_cords[1] + PIXELS)
            bot_x = random.randint(window_cords[2] - PIXELS, window_cords[2] + PIXELS)
            bot_y = random.randint(window_cords[3] - PIXELS, window_cords[3] + PIXELS)

            # If you stick a window near the edge, ensures it will mostly stay there
            if top_x < monitor_dims[0]:
                top_x = monitor_dims[0] - PADDING
            if top_y < monitor_dims[1]:
                top_y = monitor_dims[1] - PADDING
            if bot_x > monitor_dims[2]:
                bot_x = monitor_dims[2] + PADDING
            if bot_y > monitor_dims[3]:
                bot_y = monitor_dims[3] + PADDING

            # Set window to new coordinates
            win32gui.SetWindowPos(window, None, top_x, top_y, bot_x - top_x, bot_y - top_y, 0)

def main():
    while True:
        # Get target monitors
        target_monitors = get_target_monitors(target_monitors_id)
        # Process open windows
        win32gui.EnumWindows(move_window, target_monitors)
        time.sleep(30 * FREQUENCY)

if __name__ == "__main__":
    main()
