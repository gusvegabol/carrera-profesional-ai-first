---
name: pcs-obsidian-corrige-links
description: Use when editing Obsidian notes in this repo to replace raw document names, paths, or backticked references with `[[wikilinks]]`, especially in `boveda-entrevista-profesional` concept, pattern, friction, and playbook notes, and when verifying that no leftover document references remain.
---

# Obsidian Corrige Links

## Overview

Convert document references in project notes into wikilinks and leave the rest of the prose untouched.

## Workflow

1. Find candidate references with `rg`: backticked names, raw paths, quoted filenames, or repeated document stems.
2. Resolve each target against the actual note in `boveda-entrevista-profesional/**` with `rg --files`, first checking the backticked text with `.md` appended.
3. Replace only the reference text when it maps to a single existing note, using the file-based identifier that resolves from `rg --files`.
4. Keep already-linked text as-is.
5. If a target is ambiguous, does not resolve after appending `.md`, or cannot be matched to a single existing note, stop and leave it unchanged instead of guessing.
6. If the filesystem stem differs from the note heading, keep the filesystem stem as the wikilink target.

## Rules

- Use the file-based identifier that resolves in the vault, not the visible heading.
- Preserve accents, spaces, and surrounding punctuation.
- Process each unique file once, even if the user lists it twice.
- Prefer exact existing note names from this repo over invented titles.
- If the note path typed by the user does not exist, locate the real file before editing.
- If backticked text does not correspond to an existing note after adding `.md`, do not modify it.
- Do not substitute the visible heading for the file-based identifier.
- After each edit, re-scan for malformed leftovers such as stray backticks, raw `.md` paths, or unbalanced `[[[` / `]]]` introduced while replacing references near punctuation or at the start of a line.

## Quick Checks

- Search for leftovers with `rg -n '`[^`]+`|/[^/]+\.md|\\[\\[' <file>`.
- Review the patch with `git diff` before finishing.

## Common Conversions

- `` `CONCEPTO_TRANSICION_PROFESIONAL` `` -> `[[CONCEPTO_TRANSICION_PROFESIONAL]]` only if `CONCEPTO_TRANSICION_PROFESIONAL.md` exists
- `` `boveda-entrevista-profesional/08_fuentes/archivo.md` `` -> `[[archivo]]` only if that file exists
- raw repeated mention -> replace every occurrence in the note only after the reference resolves to an existing file
