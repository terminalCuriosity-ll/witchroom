# Witchroom

A NixOS desktop built from scratch: a cyberpunk / retrofuturist / neon-goth witch's
one-room flat, where ritual, tarot and spells are how she talks to her technology.
The roadmap is `docs/ROADMAP.md`; the step marked **RESUME HERE** is where we are.

## Who this is for
- The owner is a Linux beginner and near-beginner programmer. Define every new word,
  explain every file, and teach as we go.
- Claude cannot touch her computer. Everything she runs must be copy-paste or
  step-by-step, and safety-reviewed first.

## Rules
- This repo is a fresh start. Do not copy config or design from her older `nix` repo
  unless she asks for a specific piece.
- Install user programs through home-manager (`home.packages`). Use
  `environment.systemPackages` only for system-wide needs (drivers, services).
- Never build or install imperatively (`nix-env`, `nix profile install`). Everything goes
  through the config files so the system stays reproducible.
- The only rebuild command is `sudo nixos-rebuild switch` (with `--flake` once the flake
  exists). Claude never runs it; she does, when asked.
- Every themed value (colours, fonts, sizes, motion) comes from one theme file, so the
  look stays changeable.
