# Formatter Assistant

## 1. Start venv

**Execute:**

```
source venv/bin/activate
```

## 2. Install requirements

**Execute:**

```
pip3 install -r requirements.txt
```

## 3. Run the build-script -> Need to rebuild when changes have been done in setup

**Execute:**

```
 ./build
```

# Usage

```
This application is used to create arrays and dictionaries from one or two lists.
When the script is run a vim editor opens and give you the opportunity
to add the lists straight into the document. There are some different kinds of
ways to input the lists and they respond with different flags.
```

# Scripts

### Create Array

```
create_array --variable_name
create_array -vn
```

Creates an array out of an list.
Variable name is the name of the future array.

```
DRIVER_UPDATE_ID = [
    'max-verstappen',
    'alexander-albon',
    'fernando-alonso',
    'valtteri-bottas',
    'pierre-gasly',
    'lewis-hamilton',
    'nico-hulkenberg',
    'nicholas-latifi',
    'charles-leclerc',
    'kevin-magnussen',
    'lando-norris',
    'esteban-ocon',
    'sergio-perez',
    'daniel-ricciardo',
    'george-russell',
    'carlos-sainz',
    'mick-schumacher',
    'lance-stroll',
    'yuki-tsunoda',
    'sebastian-vettel',
    'guanyu-zhou',
]

```

### Create Dictionaries

```
create_dict --variable_name
create_dict -vn
```

## Sorted lists

Creates a dictionary out of one or two lists.
Variable name is the name of the future array.

```
create_dict --variable_name --sorted_lists
create_dict --variable_name -sorted
create_dict -vn -s
```

This function take as an input the lists to be put un one on top of the other (that will be the keys), they should be separated with a space.

INPUT:

```
Austrian_Grand_Prix
French_Grand_Prix
Hungarian_Grand_Prix
Belgian_Grand_Prix
Dutch_Grand_Prix

Austria
France
Hungary
Belgium
Netherlands
```

OUTPUT:

```
GRAND_PRIX_DATA = {
    'Austrian_Grand_Prix': 'Austria',
    'French_Grand_Prix': 'France',
    'Hungarian_Grand_Prix': 'Hungary',
    'Belgian_Grand_Prix': 'Belgium',
    'Dutch_Grand_Prix': 'Netherlands',
}

```

## Every other line

Creates a dictionary out of two lists.
Variable name is the name of the future array.

```
create_dict --variable_name --every_other
create_dict -vn -eo
```

This function takes on list as an input where the value should be under the key.

INPUT:

```
Austrian_Grand_Prix
Austria
French_Grand_Prix
France
Hungarian_Grand_Prix
Hungary
Belgian_Grand_Prix
Belgium
Dutch_Grand_Prix
Netherlands
```

OUTPUT:

```
GRAND_PRIX_DATA = {
    'Austrian_Grand_Prix': 'Austria',
    'French_Grand_Prix': 'France',
    'Hungarian_Grand_Prix': 'Hungary',
    'Belgian_Grand_Prix': 'Belgium',
    'Dutch_Grand_Prix': 'Netherlands',
}

```

## Beside each other

Variable name is the name of the future array.

```
create_dict --variable_name --beside
create_dict -vn -b
```

This function takes on list as an input where the key and value should be on the same row separated by a comma, the key should be to the left.

INPUT:

```
Austrian_Grand_Prix, Austria
French_Grand_Prix, France
Hungarian_Grand_Prix, Hungary
Belgian_Grand_Prix, Belgium
Dutch_Grand_Prix, Netherlands
```

OUTPUT:

```
GRAND_PRIX_DATA = {
    'Austrian_Grand_Prix': 'Austria',
    'French_Grand_Prix': 'France',
    'Hungarian_Grand_Prix': 'Hungary',
    'Belgian_Grand_Prix': 'Belgium',
    'Dutch_Grand_Prix': 'Netherlands',
}

```
