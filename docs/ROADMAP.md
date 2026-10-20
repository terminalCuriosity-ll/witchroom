# Witchroom roadmap

The plan from "knowing nothing" to a desktop where every part is an object in her room.
Each step teaches one idea and ends with something you can see. Nothing here is final:
change the order, the names or the look whenever you like.

## How we work
- **You run, I write.** I prepare files in this repo and check them; you copy, paste and
  tell me what you see.
- **Nothing is lost.** NixOS keeps every previous version of your system (called a
  *generation*). If a change breaks something, you pick the older one from the boot menu.
- **Your current setup stays until the new one is ready.** We build the witchroom next to
  it and only switch over when it boots and works.

## Words you will meet
| Word | What it means |
|---|---|
| **Linux** | The core of the operating system: it talks to the hardware. |
| **NixOS** | A Linux system described entirely by text files. Change the file, rebuild, and the computer matches it. |
| **Configuration** | Those text files. Ours will live in this repo. |
| **Flake** | A file (`flake.nix`) that pins exact versions of everything, so the same config always builds the same system. |
| **home-manager** | The part of the config for *your* user: apps, terminal, theme. |
| **Rebuild** | `sudo nixos-rebuild switch`: turns the files into the running system. |
| **Window manager / compositor** | The program that draws and arranges windows. The "walls and furniture layout" of the room. |
| **Shell (desktop shell)** | The bar, clock, launcher, notifications: everything around the windows. We will write ours. |
| **Terminal** | A text window where you type commands. |
| **Git / repo** | A history of every change to our files. This repo is the witchroom's spellbook. |

## The room (a first draft, yours to rewrite)
Every interface part becomes an object in the flat. These are suggestions to react to.

| Interface part | Object in the room (idea) |
|---|---|
| Clock | In the window, moon rises + sets in hour-segments according to time (at 00:00 it's at its highest, at 12:00 it's below the horizon, at 18:00 it's halfway to returning to its highest spot, etc.) and it shows the current moon phase on it |
| Bar | No bar |
| Weather | The window itself: if it's dry outside it's foggy in the city, if it's raining/snowing it rains. if it's hot it lightens to glow dawn shades, then bright blue glowing skies at very high hot temperatures. if it's cold it darkens to glow dusk shades, then pitch black skies at very low cold temperatures |
| App launcher | Drawing a tarot card from the deck: each card you draw opens one new app window |
| Session menu (sleep, lock, logout, reboot, shut down) | Snuffing candles: each a different ending ritual: sleep, lock, logout, reboot, shutdown. Each candle is its own colour, darkening with how final it is: sleep is lavender, and the others grow deeper in shade up to shutdown. They stand behind the bed (the bed has no headboard). Night light is the blinds on the window or another candle? |
| Workspaces | Each workspace is its own tarot reading: one card per open app window in that workspace, as many cards as you have windows open there. The reading of the workspace you're on floats beside the deck on a little hologram at the very top of the screen, and switching workspace swaps the spread |
| Window manager | Tiling but also movable overlays over the whole scene like holographic displays, they overlay: bookshelves (roughly left third of screen), floor (roughly bottom third of screen) right_wall (roughly right fifth of screen), and the window as default tiles. Each tile stops at the edge of its own area, and no two tiles overlap |
| Terminal | Neon (scratch-n-sniff paper almost) on black spell-book you write into |
| Notifications | The familiar is the notification feed: speech bubbles from the familiar with a cute noise. It also pops up now and then with a positive message or affirmation from a self-love / affirmation widget. The familiar sleeps curled up on the end of the bed, and her messages appear in the bottom-right corner of the screen without covering her |
| Browser (Zen) | Neon glowing & flickering digital apparition/portals summoned from the summoning circle (designed in a later step) |
| Control center | No single panel any more: it is spread across the room (the next four rows) |
| Volume | The ritual circle, drawn on the bed: simple, with a light cyber touch. It grows bigger and more runically complex as the volume goes up. Scroll on it to raise or lower the volume |
| Battery | The ritual circle glows brighter or dimmer with the battery level |
| Brightness | The literal electric light(s) in the room that light the scene. Scroll on a light to raise or lower brightness |
| Wi-fi and bluetooth | One round, porthole-like holographic display on the left wall, between the bookshelves and the window, split into two halves like video calls, with no border between them: wi-fi on top, bluetooth below. Connected: friends on the screen and a glowing frame. Idle (nothing connected): a soft teal glow in level bands, like the round window in the room pictures. Scroll on one to switch between wi-fi networks or bluetooth devices |
| Pomodoro timer | An hourglass, standing among the books on one of the bookshelves |
| File manager | The books on the bookshelves (the potted herbs on the shelves are just for looks) |

**The room's layout.** The walls, ceiling and floor follow the lofi-vibes-4k picture: one-point
perspective, with the vanishing point at the far right edge at eye level, so the left wall shows wide
and the right wall hardly at all. Bookshelves run along the left wall, with the round wi-fi and
bluetooth porthole on the wall between them and the window. The window fills most of the far wall,
from the ceiling (only the rolled blinds sit between them) down to a low seat near the floor, which
stays clear. The ledge and a small goth altar at its left end are one built-in piece, with the same
dark wood, pointed arches and lace; the altar sits under the porthole, and the spellbook lies open on
a book stand on top of it. Out in the city, hover trains cross between lit towers, and two
megastructures rise behind the nearer rows. The hourglass and a lava lamp stand among the books. The bed is in the far right corner, head to
the back wall, a little longer than before, with the ritual circle drawn on it, the candles on a shelf
behind it and the familiar curled up on its end. The light is a moon lamp on a plain cord, hanging in
the top right. Five plants, each a different kind and each on its own, are just for looks: a monstera
on the floor by the altar, an English ivy trailing off the altar, a string of pearls on a shelf, a
pothos hanging by the window and a fern hanging lower than the light. The deck and the current reading float on a slim hologram
above the window, over the blinds but never over the glass. There is no bar, desk, chair, big screen
or desk nook.

## Steps

### 0. Ground (no commands yet)
- Read the word list above; ask about anything.
- Gather the vibe: a few images, songs, games or films that feel like her room. We turn
  them into a mood board and a written design language (palette, type, shapes, motion).

### 1. Lay the foundation  <- RESUME HERE
Goal: a tiny, plain witchroom config that boots your laptop.
1. Get this repo onto your computer (`git clone`).
2. Let NixOS describe your hardware for us (`nixos-generate-config --show-hardware-config`),
   since disks, encryption and the NVIDIA graphics are unique to your machine.
3. Write a minimal `flake.nix`, `configuration.nix` and `home.nix`: boot, your user,
   network, sound, and nothing else.
4. Rebuild and reboot into it. Learn the boot menu and how to roll back.

### 2. Choose the walls (window manager)
Compare a couple of compositors (my default pick is **Hyprland**: Wayland, smooth
animations, huge community; **niri** is the main alternative) and install one.

### 3. The theme file
One file holds every colour, font and size. Everything later reads from it, so changing
the whole look is one edit.

### 4. The terminal and spellbook
Style the terminal and command prompt first: the easiest place to learn how config files
turn into visible changes.

### 5. Build our own desktop shell
Written with **Quickshell** (a toolkit for drawing desktop widgets in a language called
QML). Smallest first, so each one teaches a new skill:
1. Clock (show text that changes over time)
2. Bar (a panel that holds things)
3. Workspaces (talk to the window manager)
4. Weather (fetch data from the internet)
5. App launcher (search and start programs)
6. Session menu (run system actions safely)
7. Notifications feed
8. Control center (audio, brightness, power, network, bluetooth, screen time)

### 6. The rest of the room
Zen browser theming, file manager, lock screen, wallpaper and ambient touches.

### 7. Ritual interactions
Tarot draws, spells and gestures as ways to *use* the system, once the basics work.

## Done
(nothing yet)
