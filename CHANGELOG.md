# Changelog


### 13-8-21
- Added Fumo mode as a joke
- Added `$changelog`
- Cleaned up the messy embeds and other code
- Updated `.gitignore`

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
  - Implemented anilist.co search
  - Implemented [mywaifulist.moe](https://mywaifulist.moe) search
  - Implemented nhentai.net search