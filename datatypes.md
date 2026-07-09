# Object types  / data types

-Numbers : 1234 , 3.14515 , 3+4j (complex numbers) , methods like : Decimal (),
Fraction() , 0b111 (0b type numbers)
-String : 'spam' , "Khadeeja's" , b'a\x01c' , u'sp\xc4m'(uni code ,smiley face code)
-List : [1, [2, 'three'], 4 , 5], list(range(10))
-Tuple : (1 ,'spam' , 4, 'U') , tple('spam') , namedtuple

# Python Data Types — My Notes

Basic idea: a data type is just what kind of value something is — a number, text, true/false, or a collection of things. Python figures out the type automatically based on what I write.

---

## 1. Numbers

### int — whole numbers
No decimal point, positive or negative.

### float — decimal numbers
Has a decimal point, even if it's .0

Quick rule: if even one number in an operation is a float, the whole result becomes a float.

---

## 2. str — text (strings)
Anything inside quotes, single ' ' or double " ".

Strings are immutable — once made, can't be edited in place. Any "change" makes a brand new string.

---

## 3. bool — true or false
Only two possible values: True or False (capital letters, always).

Used constantly in if conditions.

---

## 4. None — intentional "nothing"
Not zero, not empty string — literally no value at all.

Check it using `is None`, not `== None`.

---

## 5. Collections — groups of values

| Type  | Looks like       | Ordered? | Editable (mutable)? | Duplicates allowed? |
|-------|------------------|----------|----------------------|-----------------------|
| list  | [1, 2, 3]        | yes      | yes                  | yes                   |
| tuple | (1, 2, 3)        | yes      | no (locked)          | yes                   |
| dict  | {"key": "value"} | key-based| yes                  | keys must be unique   |
| set   | {1, 2, 3}        | no       | yes                  | no (auto-removes)     |

### list — like a numbered shelf, editable

### tuple — like a list, but locked forever
### dict — labeled drawers, access by name not position
### set — a bag of unique items, no order, no duplicates

---

## My simple way to pick a type

- Order matters + need to edit it -> list
- Order matters + should stay locked -> tuple
- Need to label things by name -> dict
- Just need unique items, order doesn't matter -> set

---

## Quick self-check
- type(5) -> int
- type(5.0) -> float
- type("hi") -> str
- type(True) -> bool
- type([1,2]) -> list
- type((1,2)) -> tuple
- type({"a":1}) -> dict
- type({1,2}) -> set
