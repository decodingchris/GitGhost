# GitVault

A simple way to keep your private files safe while sharing your code with the world.

---

## Overview

GitVault helps you **manage sensitive files and folders** that you don’t want in your public Git repo. It lets you back up and version those private files in a separate, secure repo — so you get the best of both worlds.

---

## What it does

- Use a `.gitvaultinclude` file to list private stuff you want to track (which should also be in `.gitignore`)
- `gitvault init` sets up GitVault in your project, creating the private repo and config files
- `gitvault status` shows what’s changed in your private files since your last save
- `gitvault save` commits and pushes those private changes to your private repo
- `gitvault discard` lets you throw away private changes you don’t want to keep
- Keeps secrets out of your public repo, no surprises
- Manual control — **you decide when to save, discard, or check**

---

## How to use it

1. **Initialize GitVault**

Run this once in your repo to set things up:

```bash
gitvault init
```

2. **List your private files**

Create a `.gitvaultinclude` file with paths to your private files or folders (make sure they’re also in `.gitignore`):

```
secrets.env
private_notes/
config/dev.yaml
```

3. **See what’s changed**

```bash
gitvault status
```

4. **Save your private changes**

```bash
gitvault save
```

5. **Discard private changes you don’t want**

```bash
gitvault discard
```

That’s it — your sensitive stuff is safely versioned, but never exposed.

---

## Installation

_Coming soon on PyPI!_  
For now, just clone this repo and install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Contributing

Ideas, bugs, or want to help out?  
Pull requests are welcome! Or just open an issue and let’s chat.

---

## License

MIT License
