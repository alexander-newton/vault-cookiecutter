# vault-cookiecutter

A [Cookiecutter](https://cookiecutter.readthedocs.io) template for spinning up a fresh Obsidian vault with a fixed plugin set, the [Minimal](https://github.com/kepano/obsidian-minimal) theme, [PARA](https://fortelabs.com/blog/para/) folders, default Templater-style note templates, and a Quarto project at the top level.

## What you get

```
<vault_name>/
├── .obsidian/                  # plugin bundles + settings (gitignored in the generated vault)
├── 01_Projects/
├── 02_Areas/
├── 03_Resources/
│   └── templates/              # daily-note, project, meeting, literature-note
├── 04_Archive/
├── _quarto.yml                 # Quarto project config
├── .gitignore                  # excludes .obsidian/, output/, .quarto/, _freeze/, TeX cruft
└── CONTRIBUTING.md             # onboarding for collaborators
```

Bundled plugins (latest releases at template build time):

- `obsidian-git`
- `obsidian-minimal-settings`
- `obsidian-latex-suite` (with a customised snippet library)
- `obsidian-kanban`
- `obsidian-zotero-desktop-connector`
- `terminal`
- `obsidian-outliner`
- `obsidian-custom-attachment-location`

Plus the **Minimal** theme.

The post-generation hook initialises a git repo on `master`, adds the remote you supplied (if any), and optionally installs three [alexander-newton](https://github.com/alexander-newton) Quarto extensions: `custom-amsthm-environments`, `custom-equation-tags`, `econ-paper-template`.

## Prerequisites

- Python 3.8+
- `cookiecutter` (`pip install cookiecutter` or `pipx install cookiecutter`)
- `git` (for the post-gen hook)
- Optional: `quarto` (only needed if you opt in to extension install at prompt time)

## Usage

```bash
cookiecutter git@github.com:alexander-newton/vault-cookiecutter.git
```

or against a local clone:

```bash
git clone git@github.com:alexander-newton/vault-cookiecutter.git
cookiecutter ./vault-cookiecutter
```

You'll be prompted for:

| Variable | Default | Notes |
|---|---|---|
| `vault_name` | `my-vault` | Used as the folder name and shown in the generated `CONTRIBUTING.md`. |
| `author_name` | `Alexander Newton` | Embedded in `_quarto.yml`, default template front matter, and `CONTRIBUTING.md`. |
| `git_remote_url` | _(empty)_ | If set, the hook runs `git remote add origin <url>`. Empty = no remote. |
| `quarto_output_dir` | `output` | Where Quarto writes rendered files. Auto-added to `.gitignore`. |
| `install_quarto_extensions` | `yes` / `no` | If `yes` and `quarto` is on PATH, the three alexander-newton extensions are installed via `quarto add`. |

### Non-interactive

```bash
cookiecutter git@github.com:alexander-newton/vault-cookiecutter.git \
  --no-input \
  vault_name=phd-notes \
  author_name="Your Name" \
  git_remote_url=git@github.com:you/phd-notes.git \
  install_quarto_extensions=no
```

## After generation

1. `cd <vault_name>`
2. Open the folder in Obsidian (`Open folder as vault`) and trust the vault.
3. Enable Community plugins.
4. If you set a remote, push:

   ```bash
   git add .
   git commit -m "initial vault scaffold"
   git push -u origin master
   ```

5. Read `CONTRIBUTING.md` for branching conventions, the Zotero workflow, the LaTeX-Suite cheat sheet, and required external software.

## Updating the cookiecutter

Plugin releases drift quickly. When you want to bump the bundled plugins to their current versions:

1. Look up each plugin's repo (see `community-plugins.json` in [obsidianmd/obsidian-releases](https://github.com/obsidianmd/obsidian-releases)).
2. Fetch the latest `main.js`, `manifest.json`, `styles.css` from the release page into `{{cookiecutter.vault_name}}/.obsidian/plugins/<plugin-id>/`.
3. Same drill for the Minimal theme (`theme.css` + `manifest.json`) under `themes/Minimal/`.
4. Test:

   ```bash
   rm -rf /tmp/test-vault
   cookiecutter . -o /tmp --no-input vault_name=test-vault install_quarto_extensions=no
   ```

5. Commit and push.

`data.json` files inside each plugin folder hold settings — leave them alone unless you actually want to ship a new default.

## Editing the template

- `cookiecutter.json` — prompts and `_copy_without_render` (keeps minified JS out of Jinja).
- `hooks/post_gen_project.py` — git init, remote add, optional Quarto extension install.
- `{{cookiecutter.vault_name}}/` — everything that ends up in the generated vault.

Obsidian template tokens (`{{date}}`, `{{time}}`, `{{title}}`) inside the templates need to be wrapped in `{% raw %}…{% endraw %}` so cookiecutter doesn't try to render them as Jinja variables.
