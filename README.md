# SCD-Group-1-Refactoring

## Project Description
Refactoring of the Gilded Rose legacy Python code (Group 1) to improve internal design while preserving external behavior. Managed with Git/GitHub using feature branches, pull requests, and a tagged release.

## How to Run
'''
pip install pytest
python -m pytest
'''
## Group Members
- Hamza Sattar - SWEN241101064
- Muhammad Hayyan - SWEN241101105
- Aqsa Munir - SWEN241101063
- Zainab Shafiq - SWEN241101079

## Changelog
## Changelog

### v1.0.0
- refactor: replace magic numbers and strings with named constants (MAX_QUALITY, MIN_QUALITY, item name constants)
- refactor: decompose conditional logic in update_quality() into helper methods
- refactor: extract item-specific update handlers (Aged Brie, Sulfuras, Backstage passes, normal items)
- refactor: centralize quality bound enforcement in _adjust_quality()
- docs: add baseline analysis and UML before/after diagrams
- test: add 12 characterization tests
