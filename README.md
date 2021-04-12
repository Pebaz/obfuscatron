# Obfuscatron

Encrypt data by storing it within a Python script that pretends to just be
"obfuscated"

### Features

Right now, Obfuscatron is able to store data within the following Python syntax:

* Variables
* Class Names
* Function Names
* Type Hint Identifiers

### Installation

```bash
$ pip install obfuscatron
$ pip install "git+https://github.com/Pebaz/obfuscatron"
```

### Usage

```bash
$ obfuscatron FILE.py encode DATAFILE OUTFILE
$ obfuscatron OUTFILE.py decode DATAFILE
```

### Example

Given this Python file to store some data:

```python
custom_int_name = int


def function_add(first_number: custom_int_name, second_number: custom_int_name):
    return first_number + second_number


def function_sub(first_number: custom_int_name, second_number: custom_int_name):
    return first_number - second_number


def function_mul(first_number: custom_int_name, second_number: custom_int_name):
    return first_number * second_number


def function_div(first_number: custom_int_name, second_number: custom_int_name):
    return first_number / second_number


def function_mod(first_number: custom_int_name, second_number: custom_int_name):
    return first_number % second_number


def function_exp(first_number: custom_int_name, second_number: custom_int_name):
    return first_number ** second_number


custom_float_name = float


def func_float_add(first_num: custom_float_name, second_num: custom_float_name):
    return first_num + second_num


def func_float_sub(first_num: custom_float_name, second_num: custom_float_name):
    return first_num - second_num


def func_float_mul(first_num: custom_float_name, second_num: custom_float_name):
    return first_num * second_num


def func_float_div(first_num: custom_float_name, second_num: custom_float_name):
    return first_num / second_num


def func_float_mod(first_num: custom_float_name, second_num: custom_float_name):
    return first_num % second_num


def func_float_exp(first_num: custom_float_name, second_num: custom_float_name):
    return first_num ** second_num


custom_bool_name = bool


def function_and(first_bool: custom_bool_name, second_bool: custom_bool_name):
    return first_bool and second_bool


def function_or(first_bool: custom_bool_name, second_bool: custom_bool_name):
    return first_bool or second_bool


def function_xor(first_bool: custom_bool_name, second_bool: custom_bool_name):
    return first_bool != second_bool
```

Turn this data:

```
name = Earth
radius = 39000000
terrestrial = True
foo = "😂"

name = Mars
radius = 12349282382
terrestrial = True
foo = "😂😂"

name = Jupiter
radius = 4300012323
terrestrial = False
foo = "😂😂😂"
```

Into this "obfuscated" Python file containing that data:

```bash
$ obfuscatron python-file.py encode original-data.txt obfuscated-python-file.py
```

Result:

```python
_1bdf0020ac0e6cb = int


def _739d460d09a9(_ba3f70e5094d: _1bdf0020ac0e6cb, _90e68e0bb016d:
    _1bdf0020ac0e6cb):
    return _ba3f70e5094d + _90e68e0bb016d


def _fb4103c9b200(_ba3f70e5094d: _1bdf0020ac0e6cb, _90e68e0bb016d:
    _1bdf0020ac0e6cb):
    return _ba3f70e5094d - _90e68e0bb016d


def _0ba260174885(_ba3f70e5094d: _1bdf0020ac0e6cb, _90e68e0bb016d:
    _1bdf0020ac0e6cb):
    return _ba3f70e5094d * _90e68e0bb016d


def _f9d90a0d6672(_ba3f70e5094d: _1bdf0020ac0e6cb, _90e68e0bb016d:
    _1bdf0020ac0e6cb):
    return _ba3f70e5094d / _90e68e0bb016d


def _a3271bd8e033(_ba3f70e5094d: _1bdf0020ac0e6cb, _90e68e0bb016d:
    _1bdf0020ac0e6cb):
    return _ba3f70e5094d % _90e68e0bb016d


def _ec4dee8dd39d(_ba3f70e5094d: _1bdf0020ac0e6cb, _90e68e0bb016d:
    _1bdf0020ac0e6cb):
    return _ba3f70e5094d ** _90e68e0bb016d


_47bc061a1719dfeeb = float


def _ac6c1471eea643(_35f1426de: _47bc061a1719dfeeb, _24220208bf:
    _47bc061a1719dfeeb):
    return _35f1426de + _24220208bf


def _230ee4d679e58a(_35f1426de: _47bc061a1719dfeeb, _24220208bf:
    _47bc061a1719dfeeb):
    return _35f1426de - _24220208bf


def _d4dc6493bf79fe(_35f1426de: _47bc061a1719dfeeb, _24220208bf:
    _47bc061a1719dfeeb):
    return _35f1426de * _24220208bf


def _36599759ee0be1(_35f1426de: _47bc061a1719dfeeb, _24220208bf:
    _47bc061a1719dfeeb):
    return _35f1426de / _24220208bf


def _c098256f8e486f(_35f1426de: _47bc061a1719dfeeb, _24220208bf:
    _47bc061a1719dfeeb):
    return _35f1426de % _24220208bf


def _8edeab92c6b73c(_35f1426de: _47bc061a1719dfeeb, _24220208bf:
    _47bc061a1719dfeeb):
    return _35f1426de ** _24220208bf


_8709a8aa09751c5d = bool


def _653c1fd____b(_rp9q563626: _8709a8aa09751c5d, _0eqmvftj17s:
    _8709a8aa09751c5d):
    return _rp9q563626 and _0eqmvftj17s


def _pceiwy12s6f(_rp9q563626: _8709a8aa09751c5d, _0eqmvftj17s:
    _8709a8aa09751c5d):
    return _rp9q563626 or _0eqmvftj17s


def _9zleib3qmp0b(_rp9q563626: _8709a8aa09751c5d, _0eqmvftj17s:
    _8709a8aa09751c5d):
    return _rp9q563626 != _0eqmvftj17s
```

To get it back:

```bash
$ obfuscatron obfuscated-python-file.py decode get-original-data-back.txt
```
