---
name: pcs-obsidian-corrige-links
description: Use when editing Obsidian notes in this repo to replace raw document names, paths, or backticked references with `[[wikilinks]]`, especially in `boveda-entrevista-profesional` concept, pattern, friction, and playbook notes, and when verifying that no leftover document references remain.
---

# Obsidian Corrige Links

## Overview

Convert document references in project notes into wikilinks and leave the rest of the prose untouched.

## Workflow

1. Find candidate references with `rg`: backticked names, raw paths, quoted filenames, or repeated document stems.
2. Resolve each target against the actual note in `boveda-entrevista-profesional/**` with `rg --files`.
3. Replace only the reference text with `[[Exact note title]]`.
4. Keep already-linked text as-is.
5. If a target is ambiguous or cannot be matched to a single existing note, stop and ask before guessing.

## Rules

- Use the note title, not the filesystem path, in the wikilink.
- Preserve accents, spaces, and surrounding punctuation.
- Process each unique file once, even if the user lists it twice.
- Prefer exact existing note names from this repo over invented titles.
- If the note path typed by the user does not exist, locate the real file before editing.

## Quick Checks

- Search for leftovers with `rg -n '`[^`]+`|/[^/]+\.md|\\[\\[' <file>`.
- Review the patch with `git diff` before finishing.

## Common Conversions

- `` `CONCEPTO_TRANSICION_PROFESIONAL` `` -> `[[CONCEPTO_TRANSICION_PROFESIONAL]]`
- `` `boveda-entrevista-profesional/08_fuentes/archivo.md` `` -> `[[archivo]]`
- raw repeated mention -> replace every occurrence in the note
