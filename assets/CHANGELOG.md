# Changelog

### 19-8-21
- Moved profile picture and changelog to `assets/`
- Added comment to `fumo_mode.py` explaning what happened.
- Changed NSFW error message to an embed
  - Added Sagiri picture just because I thought it would be funny

### 17-8-21
- Add "/100" to the end of Anilist rating.
  - Idea by [@islem2006](https://github.com/islem2006)
- Updated profile picture to not look like a fursona.

### 14-8-21
- Removed fumo mode. Short joke, right?
- Implemented ***basic*** logging. I may expand upon this later.
  - By basic, I mean `import logging` and setting the default level.
- Split `$help` command into non-NSFW and NSFW
  - Doing this reverts a change from 12-8-21

### 13-8-21
- Added Fumo mode as a joke
- Added `$changelog`
- Cleaned up the messy embeds and other code
- Updated `.gitignore`
- Implemented [nekos.life](https://nekos.life) API

### 12-8-21
- Added NSFW checking via environment variables
  - If NSFW commands are disabled, they will be hidden in `$help`
  - Bot will not respond via error message in chat
- Added channel checking for NSFW content
  - If a channel is NSFW, `$sauce` and `$randsauce` will work.
  - If not, bot will respond by saying those only work in NSFW channels.

### 10-8-21
- Created proper `README.md`
- Created `pylint.yml`

### 5-8-21
- Initial release
  - added `requirements.txt`
  - Implemented [anilist.co](https://anilist.co/) search
    - Uses [AnilistPython](https://github.com/ReZeroE/AnilistPython)
  - Implemented [mywaifulist.moe](https://mywaifulist.moe/) search
  - Implemented [nhentai.net](https://nhentai.net/) search
    - Uses [hentai](https://github.com/hentai-chan/hentai)