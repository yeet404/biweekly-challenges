# Week 4 - Seating Organizer

run with `python main-w4.py`

## Commands

Note: All user input is 1-indexed. `main()` converts it into being 0-indexed as needed.

`create`
- usage: `create <int:col> <int:row>`
- creates seating layout with given columns and rows (length by width format)

`add`
- usage: `add <int:row> <int:col> <str:name>`
- adds person at given row-column position

`rm`
- usage: `rm <int:row> <int:col>`
- removes person at given row-column position

`print`
- usage: `print`
- prints seating chart
- `0` signifies an empty seat

`exposed`
- usage: `exposed <int:row> <int:col>`
- finds people exposed to infected person at given row-column position

`save`
- usage: `save <str:name>`
- to "save as": savename must be unique
- to overwite previous save: savename must be the same as the desired previous save

`del`
- usage: `del <str:name>` or `del this`
- `<str:name>` deletes a saved seating chart
- `this` deletes the current unsaved seating chart (similar to closing a program without saving; all old saves still exist)

`end`
- usage: `end`
- exits program

## Implementation <s>and Bugs</s>:

### Command implmentation

The user commands basically interact with this pointer `p`. By default, `p` points to `None` (`p = None` or `p->None`). `p` may point to `SeatLayout` objects.

### Saving

Thus when saving, the object that `p` points to is saved in a dictionary, but `p` still points to said object.

### Deleting

The `del this` command just sets `p->None` (well kinda, it just does `del p`).

But if the user specifies a seating layout, then that layout, within the dictionary, is deleted. **This does not set `p->None`. `p` will still point to some `SeatLayoutObject` if it did previously.**

### Creating

`create` creates a new `SeatLayout` object for `p` to point to. Therefore if `p->SeatLayoutObject` and the user then uses `create`, it is equivalent to `del this` => `create ...`.

I'm guessing the garbage collector picks up the forgotten object? I have no idea lol.
