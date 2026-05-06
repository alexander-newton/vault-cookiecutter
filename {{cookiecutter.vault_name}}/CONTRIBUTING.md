# Contributing to {{ cookiecutter.vault_name }}

This vault is an [Obsidian](https://obsidian.md) knowledge base with [Quarto](https://quarto.org) layered on top for rendered documents. It's organised around the [PARA method](https://fortelabs.com/blog/para/).

Maintainer: {{ cookiecutter.author_name }}.

## Repo layout

- `01_Projects/` — active work with a defined outcome and deadline. One folder per project.
- `02_Areas/` — ongoing responsibilities with no end date (e.g. "PhD", "Teaching", "Health").
- `03_Resources/` — reference material organised by topic. Includes `templates/`, used by Obsidian's Templates plugin.
- `04_Archive/` — anything finished or no longer relevant. Keep it; don't delete.
- `_quarto.yml` — Quarto project config. Rendered output lands in `{{ cookiecutter.quarto_output_dir }}/` (gitignored).
- `.obsidian/` — Obsidian config (gitignored, not synced via git). The cookiecutter ships a working setup at vault creation; tweak locally.

When something stops being a Project, move it to the right Area, Resource, or the Archive — don't leave dead folders in `01_Projects/`.

## Required software

1. **Obsidian** — https://obsidian.md
2. **Git** — for version control of vault contents
3. **Zotero** with the **Better BibTeX** extension — for citations
   - Zotero: https://www.zotero.org
   - Better BibTeX: https://retorque.re/zotero-better-bibtex/
4. **Quarto** — for rendering: https://quarto.org/docs/get-started/
5. **TeX Live** / **MacTeX** / **MikTeX** — needed by Quarto for PDF output. The easy path is `quarto install tinytex`.

## First-time setup

1. Clone the repo, then open the folder in Obsidian (`Open folder as vault`).
2. `.obsidian/` is gitignored, so a fresh clone has no plugins. Either:
   - regenerate from the cookiecutter into the same folder,
   - copy `.obsidian/` from another machine, or
   - install the plugins listed below manually.
3. In Obsidian, enable Community plugins and trust the vault.
4. Open Zotero (with Better BibTeX) before using citations.

## Plugins

| Plugin | Purpose | How to trigger |
|---|---|---|
| **obsidian-git** | Auto-commits and syncs the vault to a git remote. | Status bar icon, or the `Source Control` view. |
| **obsidian-minimal-settings** | Configures the Minimal theme (font, line width, accents). | `Settings → Minimal Settings`. |
| **obsidian-latex-suite** | Tab-triggered LaTeX snippets, auto fractions, matrix shortcuts. | Type a trigger in math mode; press Tab. |
| **obsidian-kanban** | Kanban boards stored as markdown. Useful for project task tracking. | Command palette → "Create new kanban board". |
| **obsidian-zotero-desktop-connector** | Inserts Pandoc citations from your Zotero library. | `Cmd+Shift+P` (bound in `.obsidian/hotkeys.json`). |
| **terminal** | Integrated terminal pane inside Obsidian. | Command palette → "Terminal: Open". |
| **obsidian-outliner** | Better bullet-list editing — drag, fold, swap, indent across lines. | Just edit a list. |
| **obsidian-custom-attachment-location** | Routes pasted images to `./attachments/` next to the current note. | Automatic. |

### LaTeX Suite — quick wins

Inside `$...$` or `$$...$$`:
- `mk` → inline math
- `dm` → display math block
- `//` → fraction
- `sr` → squared, `cb` → cubed
- `@a` → `\alpha`, `@b` → `\beta` (use `@` + Latin letter for Greek)
- `bmat`, `pmat`, `vmat` → matrix environments
- `lim`, `sum`, `int`, `tayl` → ready expansions
- `RR`, `ZZ`, `NN`, `CC` → blackboard-bold sets

Full snippet list lives in `.obsidian/plugins/obsidian-latex-suite/data.json`.

### Zotero workflow

1. Open Zotero (with Better BibTeX running).
2. In any note, hit `Cmd+Shift+P` / `Ctrl+Shift+P`.
3. Search and pick a reference; `[@citekey]` is inserted at the cursor.
4. Export your library to a `bibliography.bib` (Better BibTeX → Auto-export). Reference it from `_quarto.yml` or per-document front matter:

   ```yaml
   bibliography: bibliography.bib
   ```

5. Render with Quarto — Pandoc resolves the citations.

## Templates

Stored in `03_Resources/templates/`. Insert via Command palette → "Templates: Insert template".

Shipped:
- `daily-note.md` — daily journal
- `project.md` — project index page; drop one at the top of each `01_Projects/<project>/` folder
- `meeting.md` — agenda / decisions / actions
- `literature-note.md` — reading notes for a Zotero entry

Tokens `{% raw %}{{date}}{% endraw %}`, `{% raw %}{{time}}{% endraw %}`, `{% raw %}{{title}}{% endraw %}` are filled in on insert. Time format is `HHmm` (set in `.obsidian/templates.json`).

## Quarto

Quarto runs from the vault root, so any `.qmd` anywhere in the vault is renderable.

```bash
quarto render path/to/note.qmd     # one file
quarto render                       # whole project
quarto preview path/to/note.qmd     # live preview
```

Output goes to `{{ cookiecutter.quarto_output_dir }}/` (gitignored).

### Bundled extensions

If you opted in at cookiecutter time, three extensions from `alexander-newton` are pre-installed:

- `custom-amsthm-environments` — define and reuse `theorem`/`lemma`/`proof` environments
- `custom-equation-tags` — better numbering for tagged equations
- `econ-paper-template` — economics working paper format

Use in a `.qmd` front matter, e.g.

```yaml
format:
  econ-paper-template-pdf: default
```

To install (or re-install) later:

```bash
quarto add alexander-newton/custom-amsthm-environments
quarto add alexander-newton/custom-equation-tags
quarto add alexander-newton/econ-paper-template
```

## Conventions

- **Note IDs**: the Zettelkasten Prefixer plugin prepends `YYYY-MM-DD-HHmm` for atomic notes. Project / Area pages don't need a prefix.
- **Filenames**: lowercase-kebab where possible; PARA folders keep their `01_`/`02_` prefixes for sort stability — don't rename them.
- **Attachments**: paste images directly — they route to `./attachments/`.
- **Vim mode is on** (`.obsidian/app.json`). Disable in `Settings → Editor` if it bites you.
- **Don't commit `.obsidian/`.** It's gitignored. Settings drift per machine — sync them via a separate dotfiles repo if you want them shared.

## Branching

Everyone works on their own dedicated branch named after them (e.g. `alex`, `sam`). Cadence is tight:

1. Pull `master` into your branch every few minutes.
2. Make small edits.
3. Merge your branch back into `master` every few minutes.

This keeps divergence tiny and avoids gnarly merge conflicts on a vault where many notes change in parallel — file moves and link rewrites become painful to merge if `master` has drifted.

Auto-commit is **off** in obsidian-git by default; commit deliberately so messages are meaningful, but don't let work pile up locally — the cadence above only works if you push frequently.

Don't share a branch with someone else, and don't sit on a long-lived feature branch.

## Common pitfalls

- **`mk` / `dm` not firing.** You're outside math mode — trigger only fires inside `$...$`.
- **Quarto fails on PDF.** TeX missing; run `quarto install tinytex`.
- **Templates plugin can't find templates.** `.obsidian/templates.json` should point to `03_Resources/templates`.
- **Zotero hotkey does nothing.** Zotero must be running, with Better BibTeX active.
- **Pasted image goes to vault root instead of `./attachments/`.** Custom attachment location plugin disabled or `attachmentFolderPath` was overridden.

## Getting help

Ping {{ cookiecutter.author_name }} or open an issue on the repo remote (if one is configured).
