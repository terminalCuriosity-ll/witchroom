# Design notes

Step 0 work on how the witchroom looks. The live mood board, with the room images, Zoë's own ink
drawings, the room map and the design language draft, is a private canvas:
https://claude.ai/artifact/HticCuV7WiztxNQ5evhAqs

| File | What it is |
| --- | --- |
| `room-map.png` | The room map (draft 9): the whole screen drawn as one wall of the flat, with every desktop part numbered where it lives. The numbers match "The room" table in `../ROADMAP.md`. |
| `room_map.py` | The small Python script that draws the room map as an SVG picture. It places every object in 3D and projects it with the same one-point perspective as the lofi-vibes reference picture (vanishing point at the far right, at eye level). Run `python3 room_map.py room.svg` to redraw it. Add `LOOK=N PAL=Z NOLAB=1` in front for the Synth Noir CMYKI room, or `LOOK=C PAL=Z NOLAB=1` for neon mode. |
| `DESIGN_LANGUAGE.md` | **The design language: Synth Noir CMYKI.** Palette, colour jobs, type, shapes and rules. The theme file in Step 3 is built from it. |
| `synth-noir-cmyki.png`, `room-synth-noir.png`, `room-neon-mode.png`, `design-language.png` | Pictures of the chosen look, explained in `DESIGN_LANGUAGE.md`. |

Nothing here is installed on the computer. These are pictures and notes for planning; the real
look will come from the theme file in Step 3.
