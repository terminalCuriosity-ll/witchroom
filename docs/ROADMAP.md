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
| Clock | A candle burning down, or a moon phase in the window |
| Bar | The shelf along the wall, holding the other objects |
| Weather | The window itself: rain, fog, neon glow outside |
| App launcher | Drawing a tarot card from the deck |
| Session menu (sleep, lock, logout, reboot, shut down) | Snuffing candles: each a different ending ritual |
| Workspaces | Altars or corners of the room |
| Window manager | The room's layout: where things are placed |
| Terminal | A scrying mirror or spellbook you write into |
| Notifications | Familiar's messages, or letters slipped under the door |
| Browser (Zen) | A portal or crystal ball onto the outside world |
| Control center | The ritual circle: dials for sound, light, power, signal |
| Screen time | An hourglass |
| File manager | A chest of drawers, an apothecary cabinet |

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
